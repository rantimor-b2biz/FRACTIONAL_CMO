#!/usr/bin/env python3
"""
Fractional CMO — Automated Article + LinkedIn Post Generator
=============================================================
Extends the LinkedIn automation: every post starts from a NEW full article
published on rantimor.com (Lovable site, repo: rantimor-b2biz/ran-timor-brand).

Pipeline (mirrors the agency workflow):
  Stage 1  TRENDS RESEARCHER  (Sonnet + web search) — trending topic + sourced facts
  Stage 2  THOUGHT LEADER     (Sonnet)              — full 1,500-2,200 word article
           in the site's exact content schema, in Ran's voice
  Stage 3  GATEKEEPER         (Opus)                — reviews/revises article AND writes
           the final LinkedIn post that drives to it (link in first comment)
  Stage 4  ARTIST             (Replicate flux-1.1-pro) — hero image matching the site's
           visual language (dark navy, single conceptual metaphor, teal/amber accents)
  Stage 5  PUBLISH            — injects the article into the site repo working copy
           (Articles.tsx + ArticleDetail.tsx + hero asset) at the AUTO-ARTICLES anchors

Usage:
  python generate_article_and_post.py --site-repo <path-to-ran-timor-brand-checkout> [--topic "..."]

Requires: ANTHROPIC_API_KEY, REPLICATE_API_TOKEN.  pip install anthropic replicate
"""

import argparse
import datetime
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[2]  # FRACTIONAL_CMO/

RESEARCH_MODEL = "claude-sonnet-5"    # trend research (needs web search)
DRAFT_MODEL = "claude-sonnet-5"       # article + post drafts (per agency model rules)
GATEKEEPER_MODEL = "claude-opus-4-8"  # final review (per agency model rules)
IMAGE_MODEL = "black-forest-labs/flux-1.1-pro"

# Locked style suffix — keeps every hero on the site's existing visual language
HERO_STYLE = (
    "Dark editorial conceptual illustration, deep navy and charcoal background, "
    "single clear visual metaphor, minimal composition with generous negative space, "
    "subtle teal and amber accent tones, cinematic moody lighting, premium B2B "
    "editorial aesthetic, no text, no words, no letters, no logos, no people's faces"
)

MAX_TOPIC_HISTORY = 60
RECENT_TOPICS_SHOWN = 15

client = anthropic.Anthropic()


# ---------------------------------------------------------------- helpers

def read_file(rel_path: str) -> str:
    p = ROOT / rel_path
    return p.read_text(encoding="utf-8") if p.exists() else ""


def load_topic_history() -> list:
    p = ROOT / "B-brain" / "topic-history.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def save_topic_history(history: list) -> None:
    p = ROOT / "B-brain" / "topic-history.json"
    p.write_text(
        json.dumps(history[-MAX_TOPIC_HISTORY:], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def extract_json(text: str) -> dict:
    fence = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if fence:
        return json.loads(fence.group(1))
    start = text.find("{")
    if start == -1:
        raise ValueError(f"No JSON object found in response:\n{text[:500]}")
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        c = text[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise ValueError("Unbalanced JSON in response")


def text_of(response) -> str:
    return "\n".join(b.text for b in response.content if b.type == "text")


def call_model(model: str, system: str, user_prompt: str, max_tokens: int = 8000):
    with client.messages.stream(
        model=model, max_tokens=max_tokens, system=system,
        messages=[{"role": "user", "content": user_prompt}],
    ) as stream:
        return stream.get_final_message()


def run_with_web_search(system: str, user_prompt: str, max_continuations: int = 5):
    messages = [{"role": "user", "content": user_prompt}]
    tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": 8}]
    for _ in range(max_continuations):
        response = client.messages.create(
            model=RESEARCH_MODEL, max_tokens=8000, system=system,
            tools=tools, messages=messages,
        )
        if response.stop_reason != "pause_turn":
            return response
        messages.append({"role": "assistant", "content": response.content})
    return response


def slugify(topic: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    return slug[:60] or "article"


def camelize(slug: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", slug)
    parts = [p for p in parts if p]
    name = parts[0].lower() + "".join(p.capitalize() for p in parts[1:])
    if name and name[0].isdigit():
        name = "a" + name
    return name


def word_count(article: dict) -> int:
    def words(x):
        if isinstance(x, str):
            return len(x.split())
        if isinstance(x, list):
            return sum(words(i) for i in x)
        if isinstance(x, dict):
            return sum(words(v) for v in x.values())
        return 0
    return words(article.get("content", {}))


# ---------------------------------------------------------------- stage 1: research

def stage1_research(topic_override: str | None) -> dict:
    session_brief = read_file("C-core/session-brief.md")
    history = load_topic_history()
    recent = [h.get("topic", "") for h in history[-RECENT_TOPICS_SHOWN:]]

    system = f"""You are the Trends Researcher for Ran Timor's personal brand (Fractional CMO).

CLIENT BRIEF:
{session_brief}

CONTENT PILLARS (established by the published articles on rantimor.com):
1. AI vs Strategy — AI amplifies clarity or confusion; agentic AI/marketing; GEO
2. Positioning & GTM — positioning before performance, messaging, narrative gap
3. Founder-Led Marketing & Leadership — hiring, leadership bottleneck, fractional CMO model
4. Demand Generation — beyond leads, measuring what matters

YOUR JOB: find what B2B tech / marketing leaders are actually talking about THIS WEEK,
and pick ONE topic that (a) is genuinely trending right now, (b) fits one of the pillars,
and (c) supports a full thought-leadership article (1,500-2,200 words) with a slightly
contrarian, experience-backed angle for Israeli B2B tech founders/CEOs.
Use web search to verify the trend is real and recent — collect 4-6 concrete facts,
stats, or developments WITH named sources.

AVOID repeating these recently covered topics:
{json.dumps(recent, ensure_ascii=False, indent=2)}
"""

    if topic_override:
        task = (
            f'The topic has been chosen manually: "{topic_override}".\n'
            "Research current context, data points, and discussion around it (use web search), "
            "then produce the research brief."
        )
    else:
        task = (
            "Research what is trending right now (recent news, discussions, and data in "
            "B2B marketing, AI in marketing, GTM strategy, startup marketing). "
            "Consider 3 candidate topics, then pick the strongest one."
        )

    task += """

Return your final answer as a JSON object in a ```json fenced block:
{
  "topic": "short topic title",
  "pillar": "which content pillar",
  "angle": "Ran's specific contrarian/experience-backed angle, 2-3 sentences",
  "why_now": "why this is timely THIS week",
  "key_facts": [{"fact": "specific stat or development", "source": "publication name + url"}],
  "article_outline": ["working section heading 1", "...", "4-6 sections"],
  "candidates_considered": ["topic a", "topic b", "topic c"]
}"""

    print("Stage 1: researching trends...", flush=True)
    response = run_with_web_search(system, task)
    brief = extract_json(text_of(response))
    print(f"  -> topic: {brief.get('topic')}", flush=True)
    return brief


# ---------------------------------------------------------------- stage 2: article

ARTICLE_SCHEMA = """{
  "title": "article title (like the existing rantimor.com titles: bold claim or named concept)",
  "subtitle": "one-line subtitle or empty string",
  "excerpt": "2-3 sentence teaser for the articles index page",
  "category": "e.g. 'Strategy & AI', 'Leadership & GTM' — match the site's category style",
  "slug": "url-slug-lowercase-hyphens",
  "seo": {
    "titleTag": "SEO title, under 60 chars",
    "metaDescription": "SEO description, under 160 chars",
    "ogTitle": "og title",
    "ogDescription": "og description"
  },
  "content": {
    "intro": "3-5 opening paragraphs separated by \\n\\n — hook, name the problem, promise of the article. May use **bold**.",
    "pullQuote": "one quotable sentence from the article",
    "sections": [
      {
        "heading": "section heading",
        "paragraphs": ["paragraph 1", "paragraph 2", "..."],
        "bullets": ["optional bullet list — omit the key entirely if not needed"]
      }
    ],
    "finalThought": "closing paragraph connecting to Ran's fractional CMO practice, first person",
    "cta": {
      "heading": "short CTA question aimed at founders/CEOs",
      "text": "Let's Talk Strategy",
      "description": "1-2 sentences inviting a conversation, no hard sell"
    }
  },
  "heroPrompt": "an image-generation prompt: ONE clear visual metaphor for the article's core idea, described concretely (objects, composition). Style is added separately — describe only the metaphor and composition."
}"""


def stage2_article(brief: dict) -> dict:
    voice_dna = read_file("C-core/voice-dna.md")
    recent_titles = [h.get("topic", "") for h in load_topic_history()[-RECENT_TOPICS_SHOWN:]]

    system = f"""You are the Thought Leader writer for Ran Timor (Fractional CMO for Israeli
B2B tech startups). You write long-form articles for rantimor.com that sound exactly like
RAN — an operator with scar tissue, never a content marketer.

VOICE DNA (follow precisely — including sentence rhythm and the buzzword blacklist):
{voice_dna}

TITLE RULE (mandatory): do NOT reuse naming formulas already on the site. "The X Trap"
is banned (already used twice: The Branding Trap, The 2026 Marketing Trap). Vary the
pattern — bold claims, named concepts, questions, contrasts. Recent titles to avoid
echoing:
{json.dumps(recent_titles, ensure_ascii=False, indent=2)}

ARTICLE STANDARDS (from the 24 published articles):
- 1,500-2,200 words. 4-6 sections with clear headings.
- Executive depth: frameworks, patterns from real engagements, practical application.
- Specific numbers/facts with named in-line sources ("According to <source>, ...").
- Explain WHY problems exist before prescribing. One core idea, fully developed.
- First person where natural. English. No exclamation marks. No hype.
- Text supports **bold** and \\n line breaks inside paragraph strings."""

    task = f"""Write today's article from this research brief:

{json.dumps(brief, ensure_ascii=False, indent=2)}

Return the article as JSON in a ```json fenced block, exactly this schema:
{ARTICLE_SCHEMA}"""

    print("Stage 2: writing article...", flush=True)
    response = call_model(DRAFT_MODEL, system, task, max_tokens=16000)
    article = extract_json(text_of(response))
    print(f"  -> {article.get('title')} ({word_count(article)} words)", flush=True)
    return article


# ---------------------------------------------------------------- stage 3: gatekeeper + post

def stage3_gatekeeper(brief: dict, article: dict) -> dict:
    voice_dna = read_file("C-core/voice-dna.md")
    session_brief = read_file("C-core/session-brief.md")

    system = f"""You are the Gatekeeper for Ran Timor's personal brand. Nothing ships without
your approval. A mediocre article damages a Fractional CMO's credibility more than no
article at all.

CLIENT BRIEF:
{session_brief}

FULL VOICE DNA (the standard you enforce):
{voice_dna}

YOU HAVE TWO JOBS:
A) Review the article against the checklist below. Fix any failure yourself — return the
   full corrected article JSON (same schema). Do not shorten it below 1,500 words.
   1. Sounds like Ran — executive, crisp, slightly contrarian, grounded in experience
   2. One core idea, fully developed; real frameworks, not listicle filler
   3. Facts have named sources; nothing invented
   4. Serves the ICP (Israeli B2B tech founders/CEOs, Seed-Series C)
   5. Zero buzzwords, zero hype, zero exclamation marks
   6. finalThought connects naturally to fractional CMO work; CTA is soft
   7. Title does NOT recycle a naming formula from existing articles — "The X Trap"
      is banned (used twice already). If it does, rename it yourself.

B) Write the LinkedIn post that drives readers to this article:
   - Hook in first 2 lines (first line under 140 chars), contrarian or tension-based
   - Tease the article's core insight WITHOUT giving the whole framework away
   - Mobile-first: short lines, white space; one specific stat with named source
   - Close with insight + explicit pointer: "Full breakdown in the first comment." then
     an open engagement question
   - 3-5 hashtags at the end incl. #FractionalCMO; NO links in the post body
   - No buzzwords, no exclamation marks"""

    task = f"""Research brief:
{json.dumps(brief, ensure_ascii=False, indent=2)}

Article to review (full JSON):
{json.dumps(article, ensure_ascii=False, indent=2)}

Return JSON in a ```json fenced block:
{{
  "verdict": "APPROVED" or "REVISED",
  "review_notes": ["note per checklist item that needed attention, or 'clean pass'"],
  "article": {{ ...the full final article JSON, same schema as given... }},
  "post_text": "the complete LinkedIn post, formatted exactly as it should be published",
  "first_comment": "Full article: https://rantimor.com/articles/<slug> + one value-add line"
}}"""

    print("Stage 3: gatekeeper review + LinkedIn post...", flush=True)
    response = call_model(GATEKEEPER_MODEL, system, task, max_tokens=24000)
    result = extract_json(text_of(response))
    print(f"  -> verdict: {result.get('verdict')}", flush=True)
    return result


# ---------------------------------------------------------------- stage 4: hero image

def stage4_hero_image(article: dict, out_path: Path) -> bool:
    try:
        import replicate
    except ImportError:
        print("  replicate package missing — skipping image", flush=True)
        return False

    prompt = f"{article.get('heroPrompt', article.get('title'))}. {HERO_STYLE}"
    print(f"Stage 4: generating hero image ({IMAGE_MODEL})...", flush=True)
    try:
        output = replicate.run(
            IMAGE_MODEL,
            input={
                "prompt": prompt,
                "aspect_ratio": "16:9",
                "output_format": "jpg",
                "output_quality": 90,
            },
        )
        url = None
        if isinstance(output, list) and output:
            url = str(output[0])
        elif isinstance(output, str):
            url = output
        elif hasattr(output, "url"):
            url = output.url
        if not url:
            print("  no image returned", flush=True)
            return False
        out_path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, str(out_path))
        print(f"  -> saved {out_path.name}", flush=True)
        return True
    except Exception as e:
        print(f"  image generation failed: {e}", flush=True)
        return False


# ---------------------------------------------------------------- stage 5: publish to site repo

def js_str(s) -> str:
    return json.dumps(s if s is not None else "", ensure_ascii=False)


def render_sections(sections: list, indent: str) -> str:
    out = []
    for s in sections:
        lines = [f"{indent}{{"]
        lines.append(f"{indent}  heading: {js_str(s.get('heading'))},")
        paras = s.get("paragraphs") or []
        lines.append(f"{indent}  paragraphs: [")
        for p in paras:
            lines.append(f"{indent}    {js_str(p)},")
        lines.append(f"{indent}  ],")
        if s.get("bullets"):
            lines.append(f"{indent}  bullets: [")
            for b in s["bullets"]:
                lines.append(f"{indent}    {js_str(b)},")
            lines.append(f"{indent}  ],")
        lines.append(f"{indent}}},")
        out.append("\n".join(lines))
    return "\n".join(out)


def publish_to_site(site_repo: Path, article: dict, date: str, hero_ok: bool) -> None:
    slug = article["slug"]
    camel = camelize(slug) + "Hero"
    hero_file = f"{slug}-hero.jpg"
    wc = word_count(article)
    read_time = f"{max(4, round(wc / 200))} min read"
    article["readTime"] = read_time

    # fallback hero: reuse an existing on-brand asset if generation failed
    hero_import_file = hero_file if hero_ok else "2026-marketing-trap-hero.jpg"
    import_line = f'import {camel} from "@/assets/articles/{hero_import_file}";'

    c = article["content"]
    seo = article.get("seo", {})
    cta = c.get("cta", {})

    list_entry = f"""    {{
      title: {js_str(article["title"])},
      excerpt: {js_str(article["excerpt"])},
      date: {js_str(date)},
      category: {js_str(article["category"])},
      readTime: {js_str(read_time)},
      slug: {js_str(slug)},
      heroImage: {camel},
    }},"""

    detail_entry = f"""  {js_str(slug)}: {{
    title: {js_str(article["title"])},
    subtitle: {js_str(article.get("subtitle", ""))},
    date: {js_str(date)},
    category: {js_str(article["category"])},
    readTime: {js_str(read_time)},
    heroImage: {camel},
    seo: {{
      titleTag: {js_str(seo.get("titleTag", article["title"]))},
      metaDescription: {js_str(seo.get("metaDescription", article["excerpt"]))},
      ogTitle: {js_str(seo.get("ogTitle", article["title"]))},
      ogDescription: {js_str(seo.get("ogDescription", article["excerpt"]))},
    }},
    content: {{
      intro: {js_str(c.get("intro", ""))},
      pullQuote: {js_str(c.get("pullQuote", ""))},
      sections: [
{render_sections(c.get("sections", []), "        ")}
      ],
      finalThought: {js_str(c.get("finalThought", ""))},
      cta: {{
        heading: {js_str(cta.get("heading", "Is your GTM built on strategy?"))},
        text: {js_str(cta.get("text", "Let's Talk Strategy"))},
        description: {js_str(cta.get("description", ""))},
      }},
    }},
  }},"""

    IMPORTS_ANCHOR = "// AUTO-ARTICLES:IMPORTS"
    LIST_ANCHOR = "// AUTO-ARTICLES:LIST"
    DETAIL_ANCHOR = "// AUTO-ARTICLES:DETAIL"

    for page, anchor, entry in (
        ("Articles.tsx", LIST_ANCHOR, list_entry),
        ("ArticleDetail.tsx", DETAIL_ANCHOR, detail_entry),
    ):
        p = site_repo / "src" / "pages" / page
        t = p.read_text(encoding="utf-8")
        if anchor not in t or IMPORTS_ANCHOR not in t:
            raise RuntimeError(f"anchor missing in {page} — aborting publish")
        if f'"{slug}"' in t or f"slug: {js_str(slug)}" in t:
            raise RuntimeError(f"slug '{slug}' already exists in {page} — aborting publish")
        # import goes ABOVE the imports anchor; entry goes BELOW its anchor line
        t = t.replace(IMPORTS_ANCHOR, f"{import_line}\n{IMPORTS_ANCHOR}", 1)
        anchor_line_end = t.index("\n", t.index(anchor))
        t = t[: anchor_line_end + 1] + entry + "\n" + t[anchor_line_end + 1 :]
        p.write_text(t, encoding="utf-8")

    print(f"Stage 5: article injected into site repo (slug: {slug})", flush=True)


# ---------------------------------------------------------------- main

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate article + LinkedIn post for Fractional CMO")
    parser.add_argument("--site-repo", required=True, help="Path to a ran-timor-brand checkout")
    parser.add_argument("--topic", help="Manual topic override")
    parser.add_argument("--date", help="Date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    site_repo = Path(args.site_repo).resolve()
    if not (site_repo / "src" / "pages" / "ArticleDetail.tsx").exists():
        print(f"site repo not found at {site_repo}", file=sys.stderr)
        return 1

    date = args.date or datetime.date.today().isoformat()

    brief = stage1_research(args.topic)
    article_draft = stage2_article(brief)
    review = stage3_gatekeeper(brief, article_draft)
    article = review.get("article") or article_draft
    if "slug" not in article or not article["slug"]:
        article["slug"] = slugify(article.get("title", brief.get("topic", "article")))
    slug = article["slug"]
    article_url = f"https://rantimor.com/articles/{slug}"

    # hero image straight into the site repo assets
    hero_path = site_repo / "src" / "assets" / "articles" / f"{slug}-hero.jpg"
    hero_ok = stage4_hero_image(article, hero_path)

    publish_to_site(site_repo, article, date, hero_ok)

    # ensure the first comment carries the real URL
    first_comment = review.get("first_comment", "")
    if slug not in first_comment:
        first_comment = f"Full article: {article_url}\n\n{first_comment}"

    # --- write outputs to O-output
    outdir = ROOT / "O-output" / "auto-linkedin" / f"{date}-{slugify(brief.get('topic', 'post'))[:50]}"
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "research-brief.md").write_text(
        f"# Research Brief — {date}\n\n```json\n{json.dumps(brief, ensure_ascii=False, indent=2)}\n```\n",
        encoding="utf-8",
    )
    (outdir / "article.json").write_text(
        json.dumps(article, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (outdir / "gatekeeper-review.md").write_text(
        f"# Gatekeeper Review — {date}\n\n**Verdict:** {review.get('verdict')}\n\n"
        + "\n".join(f"- {n}" for n in review.get("review_notes", [])) + "\n",
        encoding="utf-8",
    )
    (outdir / "final-post.md").write_text(
        f"# LinkedIn Post — {date} — {brief.get('topic')}\n\n"
        f"> Pillar: {brief.get('pillar')} · Gatekeeper: {review.get('verdict')} · "
        f"Article: {article_url} · Hero: {'generated' if hero_ok else 'FALLBACK (reused asset) — generate manually'}\n\n"
        f"## Post (copy-paste to LinkedIn)\n\n{review.get('post_text', '')}\n\n"
        f"## First comment\n\n{first_comment}\n",
        encoding="utf-8",
    )

    history = load_topic_history()
    history.append({
        "date": date,
        "topic": brief.get("topic"),
        "pillar": brief.get("pillar"),
        "angle": brief.get("angle"),
        "article_slug": slug,
    })
    save_topic_history(history)

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"outdir={outdir.relative_to(ROOT)}\n")
            f.write(f"topic={brief.get('topic')}\n")
            f.write(f"verdict={review.get('verdict')}\n")
            f.write(f"slug={slug}\n")
            f.write(f"article_url={article_url}\n")

    print(f"\nDone. Article: {article_url}")
    print(f"Output: {outdir}")
    print(f"Verdict: {review.get('verdict')}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except anthropic.APIStatusError as e:
        print(f"Anthropic API error {e.status_code}: {e.message}", file=sys.stderr)
        sys.exit(1)
