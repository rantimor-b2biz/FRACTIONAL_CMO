# Recovery backlog — articles lost 2026-08-23 → 2026-09-13

Seven scheduled runs generated a full article and then discarded it: the site
publish step aborted on `anchor missing in Articles.tsx` (Lovable had moved the
article list to `src/lib/articles.ts` on 2026-08-20), and the failure killed the
run before anything was committed.

**The article text is not recoverable.** It only ever existed on the GitHub
Actions runner, which is wiped when the job ends; the run log records the topic,
title, length and Gatekeeper verdict, nothing more. Recovered here before the
logs expire (Actions keeps them 90 days — the 08-23 log goes on ~2026-11-21).

`B-brain/topic-history.json` was never written for any of these dates, so none of
these topics are marked as used and the dedup guard will not block regenerating
them.

| Date | Topic as researched | Title as written | Words | Gatekeeper | Run |
|------|--------------------|------------------|-------|-----------|-----|
| 2026-08-23 | The Credit Confession: Why SaaS 'Credit Pricing' Is a Positioning Failure Wearing a Billing Costume | The Credit Confession: What SaaS 'Credit Pricing' Is Really Hiding | 1632 | REVISED | [32621577325](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/32621577325) |
| 2026-08-27 | The Lean GTM Trap: AI Shrank Your Team, But It Didn't Shrink the Need for a Strategist | The Judgment Concentration Problem: AI Shrank Your GTM Team, Not the Cost of a Bad Strategic Call | 1524 | APPROVED | [33094339694](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/33094339694) |
| 2026-08-30 | The Budget Mismatch: Why Betting Your Marketing Budget on AI Speed Won't Fix a Buyer Who Has Less Money | The Budget Mismatch: Why Faster Marketing Won't Fix a Buyer With Less Money | 1586 | REVISED | [33310443296](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/33310443296) |
| 2026-09-03 | The Great SaaS Price Surge of 2025: Why Raising Prices Without Repositioning Is a Renewal Time Bomb | Borrowed Growth: Why 2025's SaaS Price Hikes Are a Bet Against Next Year's Renewals | 1747 | REVISED | [33753668925](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/33753668925) |
| 2026-09-06 | The Agentic Marketing Race: Why Handing Campaigns to Autonomous AI Won't Save a Startup With No Positioning | Machine-Speed Confusion: What Agentic AI Does to a Startup With No Positioning | 1479 | APPROVED | [34029384685](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/34029384685) |
| 2026-09-10 | The Negotiation Nobody's In the Room For: What Agent-to-Agent B2B Sales Means for Demand Gen | The Charm Discount Is Disappearing: What Agent-to-Agent Negotiation Means for B2B Sales | 1533 | REVISED | [34475893976](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/34475893976) |
| 2026-09-13 | The Retention Retreat: Why CMOs Are Gutting Loyalty Budgets to Chase AI-Fueled New Logos | The Retention Paradox: Why the Most AI-Mature Marketers Are the Ones Still Funding Customer Retention | 1555 | REVISED | [34752040125](https://github.com/rantimor-b2biz/FRACTIONAL_CMO/actions/runs/34752040125) |

Each posting day ran three times (the cron is deliberately redundant), and each
attempt re-ran the research, so the days above also produced two further topics
each. Only the first attempt per day is listed — the rest were near-duplicates.

## Reviving one

Once the fix is on `main`, re-run the workflow with the topic as an override:

```
Actions → Generate Article + LinkedIn Post → Run workflow
  topic: <paste the "Topic as researched" cell>
```

This re-researches against today's sources rather than replaying August's, so
the output will differ from what was lost — which is the point for the
time-bound ones. Judge staleness before reviving: the 09-03 price-surge angle is
pegged to 2025 hikes and the 08-23 credit-pricing news cycle has moved on, while
the agentic/agent-to-agent and retention angles still read current.

Do not revive more than one per posting slot — seven at once would flood the feed
and burn the topics against each other.
