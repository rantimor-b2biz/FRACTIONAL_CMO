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

## The automation (mirrors Pilgrim's pattern)
- **Cadence:** 3 posts/week — Sunday, Tuesday, Thursday, ~08:30 Israel time.
- **Pipeline** (`T-tools/scripts/generate_linkedin_post.py`):
  1. **Trends Researcher** (Sonnet + live web search) — picks a trending topic, avoids repeats via `B-brain/topic-history.json`
  2. **Copywriter** (Sonnet) — drafts in Ran's voice, loaded live from `C-core/voice-dna.md`
  3. **Gatekeeper** (Opus) — enforces the full voice checklist; revises if needed
- **Delivery:** GitHub Action (`.github/workflows/linkedin-post-generate.yml`) commits the
  post to `O-output/auto-linkedin/` and **opens a GitHub issue** with the publish-ready text
  → Ran gets an email notification automatically.
- **Ran's only job:** open the email/issue → copy the post to LinkedIn → paste the first
  comment → close the issue. Optional: generate the visual with the included prompt
  (`T-tools/scripts/generate-replicate.py`).
- **Manual override:** run the workflow manually with a `topic` input for reactive/news posts.

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
