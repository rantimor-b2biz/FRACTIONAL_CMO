#!/usr/bin/env python3
"""
Fractional CMO — Automated LinkedIn Post Generator
===================================================
3-stage pipeline, mirroring the agency workflow (Researcher -> Copywriter -> Gatekeeper):

  Stage 1  TRENDS RESEARCHER  (Sonnet + web search) — finds what's trending right now
           in B2B marketing / AI / GTM, picks the strongest angle for Ran's positioning.
  Stage 2  COPYWRITER         (Sonnet)              — drafts the post in Ran's voice,
           following the LinkedIn formula + voice DNA loaded from C-core/.
  Stage 3  GATEKEEPER         (Opus)                — final quality review against the
           voice checklist; approves or revises.

Output: O-output/auto-linkedin/YYYY-MM-DD-<slug>/
          research-brief.md, draft-v1.md, gatekeeper-review.md, final-post.md
        B-brain/topic-history.json is updated to avoid repeating topics.

Usage:
  python T-tools/scripts/generate_linkedin_post.py                # full auto
  python T-tools/scripts/generate_linkedin_post.py --topic "..."  # manual topic override

Requires: ANTHROPIC_API_KEY env var.  pip install anthropic
"""

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[2]  # FRACTIONAL_CMO/

RESEARCH_MODEL = "claude-sonnet-5"    # trend research + angle selection (needs web search)
DRAFT_MODEL = "claude-sonnet-5"       # content drafts (per agency model rules)
GATEKEEPER_MODEL = "claude-opus-4-8"  # final review (per agency model rules)

MAX_TOPIC_HISTORY = 40  # entries kept in topic-history.json
RECENT_TOPICS_SHOWN = 15  # entries shown to the researcher to avoid repeats

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
    """Pull the first JSON object out of a model response (handles fences and prose)."""
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        return json.loads(fence.group(1))
    start = text.find("{")
    if start == -1:
        raise ValueError(f"No JSON object found in response:\n{text[:500]}")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise ValueError("Unbalanced JSON in response")


def text_of(response) -> str:
    return "\n".join(b.text for b in response.content if b.type == "text")


def run_with_web_search(system: str, user_prompt: str, max_continuations: int = 5):
    """Messages call with the server-side web search tool; handles pause_turn."""
    messages = [{"role": "user", "content": user_prompt}]
    tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": 8}]
    for _ in range(max_continuations):
        response = client.messages.create(
            model=RESEARCH_MODEL,
            max_tokens=8000,
            system=system,
            tools=tools,
            messages=messages,
        )
        if response.stop_reason != "pause_turn":
            return response
        messages.append({"role": "assistant", "content": response.content})
    return response


def slugify(topic: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    return slug[:50] or "post"


# ---------------------------------------------------------------- stage 1: research

def stage1_research(topic_override: str | None) -> dict:
    session_brief = read_file("C-core/session-brief.md")
    history = load_topic_history()
    recent = [h.get("topic", "") for h in history[-RECENT_TOPICS_SHOWN:]]

    system = f"""You are the Trends Researcher for Ran Timor's personal brand (Fractional CMO).

CLIENT BRIEF:
{session_brief}

CONTENT PILLARS (established by 23 published articles on rantimor.com):
1. AI vs Strategy — AI amplifies clarity or confusion; agentic AI/marketing; GEO
2. Positioning & GTM — positioning before performance, messaging, narrative gap
3. Founder-Led Marketing & Leadership — hiring, leadership bottleneck, fractional CMO model
4. Demand Generation — beyond leads, measuring what matters

YOUR JOB: find what B2B tech / marketing leaders are actually talking about THIS WEEK,
and pick ONE topic that (a) is genuinely trending right now, (b) fits one of the pillars,
and (c) lets Ran take a slightly contrarian, experience-backed angle for Israeli B2B
tech founders/CEOs. Use web search to verify the trend is real and recent — cite sources.

AVOID repeating these recently covered topics:
{json.dumps(recent, ensure_ascii=False, indent=2)}
"""

    if topic_override:
        task = (
            f"The topic for today's post has been chosen manually: \"{topic_override}\".\n"
            "Research current context, data points, and discussion around it (use web search), "
            "then produce the research brief."
        )
    else:
        task = (
            "Research what is trending right now (search for recent news, discussions, and data "
            "in B2B marketing, AI in marketing, GTM strategy, startup marketing). "
            "Consider 3 candidate topics, then pick the strongest one."
        )

    task += """

Return your final answer as a JSON object in a ```json fenced block:
{
  "topic": "short topic title",
  "pillar": "which content pillar",
  "angle": "Ran's specific contrarian/experience-backed angle, 2-3 sentences",
  "why_now": "why this is timely THIS week",
  "key_facts": [{"fact": "specific stat or development", "source": "url or publication name"}],
  "suggested_hook": "a first-2-lines hook idea (under 140 chars for the first line)",
  "candidates_considered": ["topic a", "topic b", "topic c"]
}"""

    print("Stage 1: researching trends...", flush=True)
    response = run_with_web_search(system, task)
    brief = extract_json(text_of(response))
    print(f"  -> topic: {brief.get('topic')}", flush=True)
    return brief


# ---------------------------------------------------------------- stage 2: draft

def stage2_draft(brief: dict) -> dict:
    voice_dna = read_file("C-core/voice-dna.md")

    system = f"""You are the Copywriter for Ran Timor's personal LinkedIn (Fractional CMO for
Israeli B2B tech startups). You write posts that sound exactly like RAN — never like an agency.

VOICE DNA (follow this precisely):
{voice_dna}

LINKEDIN POST FORMULA (mandatory structure):
1. HOOK — first 2 lines, contrarian or tension-based; first line under 140 characters
   (mobile truncation). No drama, no crisis exploitation.
2. ONE idea per post. Short lines, 1-2 sentences per paragraph, strategic white space.
3. Specific numbers/facts over vague claims — use the research brief's key_facts with
   the source named in-line ("According to <source>, ...").
4. Explain WHY the problem exists before any solution.
5. End with an INSIGHT (not a pitch), then an open engagement question.
6. Hashtags at the very end: 3-5, mix broad + niche + #FractionalCMO.
7. NO external links in the post body (link goes in first comment if relevant).
8. NO buzzwords: synergy, leverage, game-changer, revolutionize, best-in-class.
9. English. No exclamation marks. Emojis only if they add clarity (max 1-2).
"""

    task = f"""Write today's LinkedIn post from this research brief:

{json.dumps(brief, ensure_ascii=False, indent=2)}

Return JSON in a ```json fenced block:
{{
  "post_text": "the complete post, formatted with line breaks exactly as it should be published, hashtags included at the end",
  "first_comment": "suggested first comment (link to a relevant rantimor.com article if one fits, otherwise a value-add addendum)",
  "visual_prompt": "a detailed image-generation prompt for an executive-minimalist visual matching the post (navy/charcoal palette, clean, no text in image)",
  "self_check": "1-2 sentences: why this sounds like Ran and not like AI"
}}"""

    print("Stage 2: drafting post...", flush=True)
    response = client.messages.create(
        model=DRAFT_MODEL,
        max_tokens=4000,
        system=system,
        messages=[{"role": "user", "content": task}],
    )
    return extract_json(text_of(response))


# ---------------------------------------------------------------- stage 3: gatekeeper

def stage3_gatekeeper(brief: dict, draft: dict) -> dict:
    voice_dna = read_file("C-core/voice-dna.md")
    session_brief = read_file("C-core/session-brief.md")

    system = f"""You are the Gatekeeper for Ran Timor's personal brand. Nothing ships without
your approval. You are strict: a mediocre post damages a Fractional CMO's credibility more
than no post at all.

CLIENT BRIEF:
{session_brief}

FULL VOICE DNA (the standard you enforce):
{voice_dna}

CHECKLIST (all must pass):
1. Sounds like Ran — executive, crisp, slightly contrarian, grounded in experience
2. Hook lands in the first 2 lines; first line under 140 chars
3. One idea only; mobile-first formatting (short lines, white space)
4. Specific facts with named sources; no invented statistics
5. Serves the ICP (Israeli B2B tech founders/CEOs, Seed-Series C)
6. Insight close + engagement question; no salesy pitch
7. Zero buzzwords, zero hype, zero exclamation marks
8. Hashtags at end (3-5); no links in body

If the draft fails on anything, FIX IT yourself and return the revised version.
"""

    task = f"""Research brief:
{json.dumps(brief, ensure_ascii=False, indent=2)}

Draft to review:
{json.dumps(draft, ensure_ascii=False, indent=2)}

Return JSON in a ```json fenced block:
{{
  "verdict": "APPROVED" or "REVISED",
  "final_post": "the final publish-ready post text (the draft as-is if APPROVED, your corrected version if REVISED)",
  "first_comment": "final first comment",
  "review_notes": ["specific note per checklist item that needed attention, or 'clean pass'"]
}}"""

    print("Stage 3: gatekeeper review...", flush=True)
    response = client.messages.create(
        model=GATEKEEPER_MODEL,
        max_tokens=4000,
        system=system,
        messages=[{"role": "user", "content": task}],
    )
    return extract_json(text_of(response))


# ---------------------------------------------------------------- main

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an automated LinkedIn post for Fractional CMO")
    parser.add_argument("--topic", help="Manual topic override (skips trend selection)")
    parser.add_argument("--date", help="Date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    date = args.date or datetime.date.today().isoformat()

    brief = stage1_research(args.topic)
    draft = stage2_draft(brief)
    review = stage3_gatekeeper(brief, draft)

    # --- write outputs
    slug = slugify(brief.get("topic", "post"))
    outdir = ROOT / "O-output" / "auto-linkedin" / f"{date}-{slug}"
    outdir.mkdir(parents=True, exist_ok=True)

    (outdir / "research-brief.md").write_text(
        f"# Research Brief — {date}\n\n```json\n{json.dumps(brief, ensure_ascii=False, indent=2)}\n```\n",
        encoding="utf-8",
    )
    (outdir / "draft-v1.md").write_text(
        f"# Draft v1 — {date}\n\n{draft.get('post_text', '')}\n\n---\n\n"
        f"**First comment:** {draft.get('first_comment', '')}\n\n"
        f"**Visual prompt:** {draft.get('visual_prompt', '')}\n",
        encoding="utf-8",
    )
    (outdir / "gatekeeper-review.md").write_text(
        f"# Gatekeeper Review — {date}\n\n**Verdict:** {review.get('verdict')}\n\n"
        + "\n".join(f"- {n}" for n in review.get("review_notes", []))
        + "\n",
        encoding="utf-8",
    )
    (outdir / "final-post.md").write_text(
        f"# LinkedIn Post — {date} — {brief.get('topic')}\n\n"
        f"> Pillar: {brief.get('pillar')} · Gatekeeper: {review.get('verdict')}\n\n"
        f"## Post (copy-paste to LinkedIn)\n\n{review.get('final_post', '')}\n\n"
        f"## First comment\n\n{review.get('first_comment', '')}\n\n"
        f"## Visual prompt (optional — Replicate/nano-banana)\n\n{draft.get('visual_prompt', '')}\n",
        encoding="utf-8",
    )

    # --- update topic history
    history = load_topic_history()
    history.append({
        "date": date,
        "topic": brief.get("topic"),
        "pillar": brief.get("pillar"),
        "angle": brief.get("angle"),
    })
    save_topic_history(history)

    # --- expose paths to GitHub Actions
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"outdir={outdir.relative_to(ROOT)}\n")
            f.write(f"topic={brief.get('topic')}\n")
            f.write(f"verdict={review.get('verdict')}\n")

    print(f"\nDone. Output: {outdir}")
    print(f"Verdict: {review.get('verdict')}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except anthropic.APIStatusError as e:
        print(f"Anthropic API error {e.status_code}: {e.message}", file=sys.stderr)
        sys.exit(1)
