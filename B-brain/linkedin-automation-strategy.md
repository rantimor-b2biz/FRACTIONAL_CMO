# LinkedIn Automation Strategy — Fractional CMO

> Created: 2026-07-02 · Owner: Adam (system) · Modeled on the Pilgrim Prayers daily-email automation

## Goal
Position Ran Timor as the go-to Fractional CMO for Israeli B2B tech startups, with a
consistent LinkedIn presence that continues the content line of rantimor.com/articles —
**with near-zero ongoing effort from Ran** (~5 minutes per post: read → paste → publish).

## Content strategy (continuation of the existing line)
The 23 published articles define 4 pillars. Every automated post maps to one:

| Pillar | Existing anchors on rantimor.com |
|---|---|
| **AI vs Strategy** | 2026 Marketing Trap, Agentic Marketing ≠ Automation 2.0, GEO, Authenticity in an AI-Saturated Market |
| **Positioning & GTM** | Narrative Gap, Why B2B Messaging Fails, Speed vs Direction, Positioning Guide |
| **Founder-Led Marketing & Leadership** | Founder-Led Marketing 2026, Leadership Bottleneck, Hiring Marketing Too Early, How to Hire a Fractional CMO |
| **Demand Generation** | Beyond Lead Generation, AI-Powered Demand Gen, Measuring What Matters |

**Trend-driven, pillar-anchored:** each post starts from what's trending *this week*
(verified by live web search with cited sources) and connects it to a pillar with Ran's
slightly-contrarian, experience-backed angle. This keeps the feed timely without drifting
off-brand.

## The automation (article-first, since 2026-07-02)
Every LinkedIn post starts from a NEW full article published on rantimor.com.

- **Cadence:** 2 article+post pairs/week — Sunday and Thursday, ~08:30 Israel time (reduced from 3, per Ran 2026-07-02 — quality over volume).
- **Pipeline** (`T-tools/scripts/generate_article_and_post.py`):
  1. **Trends Researcher** (Sonnet + live web search) — trending topic + sourced facts, dedup via `B-brain/topic-history.json`
  2. **Thought Leader** (Sonnet) — full 1,500-2,200 word article in the site's exact schema, voice from `C-core/voice-dna.md`
  3. **Gatekeeper** (Opus) — reviews/revises the article AND writes the LinkedIn post that drives to it
  4. **Artist** (Replicate flux-1.1-pro) — hero image on the site's visual language (dark navy, one metaphor, teal/amber accents, no text)
  5. **Publish** — injects the article into `rantimor-b2biz/ran-timor-brand` (Lovable site repo) at the `AUTO-ARTICLES` anchors in `Articles.tsx` / `ArticleDetail.tsx` + hero asset, and pushes
- **Delivery:** GitHub Action (`.github/workflows/linkedin-post-generate.yml`) pushes the article to the site repo, commits process files to `O-output/auto-linkedin/`, and **opens a GitHub issue assigned to Ran** (email arrives automatically) with the post + publish checklist.
- **Ran's job (~5-7 min):** open Lovable → Publish/Update (makes the article live) → verify it renders → copy post to LinkedIn → paste first comment (article link) → close issue.
- **Manual override:** run the workflow manually with a `topic` input for reactive/news posts.
- **Secrets in the FRACTIONAL_CMO repo:** `ANTHROPIC_API_KEY`, `REPLICATE_API_TOKEN`, `SITE_PUSH_TOKEN` (PAT with push access to ran-timor-brand).

## Human-in-the-loop by design (not a limitation)
Like Pilgrim's daily prayer (auto-generate → manual send), publishing stays manual:
1. LinkedIn's API for personal-profile auto-posting requires app review and adds ban risk.
2. A 30-second human glance is the last authenticity gate — the brand IS Ran's credibility.
3. Posting from Ran's own account keeps engagement signals (first-hour replies) natural.

## Costs & models
~$0.25–0.40 per post (web search + Sonnet drafts + Opus review) ≈ **$4–5/month**.
Model selection follows the agency cost rules (Sonnet for drafts, Opus for Gatekeeper only).

## Metrics (review monthly, log to M-memory/learning-log.md)
- Impressions + engagement per post, per pillar → double down on winning pillars
- Profile views / connection requests from ICP (Israeli B2B founders)
- Inbound DMs or discovery calls attributable to LinkedIn

## Phase 2 (only if Phase 1 proves itself)
- Auto-generate the visual (Replicate nano-banana) and attach to the issue
- Weekly digest instead of per-post issues, if 3 emails/week is too noisy
- Comment/engagement suggestions (Trends Monitor agent) appended to each issue
- LinkedIn API auto-publish via a "2. Publish" manual-approval workflow (Pilgrim's send pattern)

## Setup requirement (one-time)
GitHub repo secret `ANTHROPIC_API_KEY` in `rantimor-b2biz/FRACTIONAL_CMO`
(Settings → Secrets and variables → Actions) — same as the Pilgrim repo.
