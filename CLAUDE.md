# FRACTIONAL_CMO - AI Agent Team for B2B Tech Marketing

## Session Start Protocol (MANDATORY)

When starting ANY new conversation from this folder, ALWAYS read these files first before responding:

### 1. Core Files (C-core/) - WHO IS RAN?
- `C-core/project-brief.md` - What Ran does, who he serves, business goals
- `C-core/voice-dna.md` - **CRITICAL** - How Ran speaks (executive, crisp, contrarian)
- `C-core/icp-profile.md` - Who we're targeting (Technical Founder Tom, Growth-Stage CEO Sarah)

### 2. Memory Files (M-memory/) - WHAT HAVE WE LEARNED?
- `M-memory/learning-log.md` - What content has worked (and what hasn't)
- `M-memory/decisions.md` - Strategic choices made (why we prioritize certain topics)
- `M-memory/feedback.md` - Audience signals (engagement patterns, lead generation)

### 3. Current State (B-brain/) - WHERE ARE WE NOW?
- `B-brain/content-calendar.md` - Quarterly plan and upcoming topics

### 4. Agent Definitions (A-agents/) - HOW DO WE WORK?
- Review agent roles when you need to coordinate multi-agent workflows

---

## How This System Works

**FRACTIONAL_CMO** is a multi-agent content system designed to position Ran Timor as a B2B tech marketing thought leader.

**Goal:** Generate 3 LinkedIn posts/week + 1 long-form article every 2-3 weeks, all in Ran's voice, serving his ICP, and driving qualified inbound leads.

**The agents (8 active):**
1. **CMO Orchestrator** - Strategic coordinator (breaks down plans, assigns work)
2. **Content Strategy Agent** - Quarterly planning specialist
3. **LinkedIn Generator** - Writes LinkedIn posts (3/week) + LinkedIn Copywriting Skill
4. **Thought Leader Agent** - Writes long-form articles (1 every 2-3 weeks)
5. **Trends Monitor** ⭐ - Tracks trending topics, identifies engagement opportunities (daily) + LinkedIn Engagement Strategy Skill
6. **Brand Monitor** - Tracks cross-channel performance and provides insights
7. **LinkedIn Analytics Agent** - Deep-dive LinkedIn data analysis (reports to Brand Monitor)
8. **Gatekeeper** - Quality control (reviews all content before publication)

**Note:** Engagement Agent consolidated into Trends Monitor (Feb 26, 2026)

---

## Quick Commands

Use these to quickly activate the right agent(s) for common tasks:

### 📝 Content Creation
- **"Create a LinkedIn post about [topic]"**
  → LinkedIn Generator + LinkedIn Copywriting Skill → Gatekeeper

- **"Create LinkedIn post based on [article/insight]"**
  → LinkedIn Generator + LinkedIn Copywriting Skill → Gatekeeper

- **"Write an article about [topic]"**
  → Thought Leader Agent → Gatekeeper

### 📊 Performance & Analytics
- **"How did last week's content perform?"**
  → Brand Monitor (provides broad summary)

- **"Deep-dive LinkedIn analytics"**
  → LinkedIn Analytics Agent → reports to Brand Monitor

- **"What topics are resonating with our ICP?"**
  → Reads M-memory/learning-log.md (performance patterns)

### 📅 Strategic Planning
- **"What should I post this week?"**
  → CMO Orchestrator reviews content calendar + assigns 3 topics

- **"Create Q[X] 2026 content strategy"**
  → Content Strategy Agent (analyzes goals, ICP, past performance)

- **"Plan next month's content"**
  → CMO Orchestrator + Content Strategy Agent

### 🔥 Engagement & Trends
- **"What's trending in B2B marketing this week?"**
  → Trends Monitor (identifies hot topics + strategic engagement angles)

- **"Find engagement opportunities for today"**
  → Trends Monitor + LinkedIn Engagement Strategy Skill (suggests 3-5 posts to engage on)

- **"Draft a thoughtful comment on [specific post]"**
  → Trends Monitor + LinkedIn Engagement Strategy Skill (in Ran's voice, adds value)

### ✅ Quality Control
- **"Review this post against brand standards"**
  → Gatekeeper (checks: voice, ICP relevance, specificity, quality)

- **"Does this sound like Ran?"**
  → Gatekeeper compares to C-core/voice-dna.md

---

## Auto-Learning Protocol

After completing significant work, update the relevant memory file:

### When to Update M-memory/learning-log.md
- After publishing content → Record performance (likes, comments, DMs)
- When noticing patterns → "Posts with specific numbers get 2x engagement"
- After trying new formats → What worked, what didn't

### When to Update M-memory/feedback.md
- After receiving DMs or inquiries → What triggered the conversation?
- When noticing engagement patterns → Which personas are responding?
- After lead generation → Which content drove the inquiry?

### When to Update M-memory/decisions.md
- When making strategic choices → "Focusing on AI vs Strategy theme for Q2"
- When adjusting approach → "Prioritizing contrarian takes over frameworks"
- When learning from mistakes → "Topic X didn't resonate because Y"

---

## Content Quality Standards

**Every piece must:**
1. ✅ Sound like Ran (read C-core/voice-dna.md first)
2. ✅ Serve the ICP (Technical Founder Tom, Growth-Stage CEO Sarah)
3. ✅ Reinforce positioning ("clarity before speed")
4. ✅ Be specific (numbers, examples, not vague claims)
5. ✅ Pass Gatekeeper review before publication

**Voice checklist:**
- Executive-level (not fluffy marketing speak)
- Direct and crisp (short sentences)
- Slightly contrarian (challenges conventional wisdom)
- Grounded in experience (not just theory)
- NO buzzwords (synergy, disruptive, game-changer)

---

## File Organization

### O-output/ (Generated Content)
Save all content in numbered project folders:

```
O-output/
├── 01-linkedin-post-ai-positioning/
│   ├── draft-v1.md
│   ├── gatekeeper-review.md
│   └── final-post.md
├── 02-article-positioning-before-performance/
│   └── article-final.md
```

**Rules:**
- Never save directly in `O-output/` - always use folders
- Folder naming: `[number]-[slug]`
- File naming: `draft-v1.md`, `gatekeeper-review.md`, `final-post.md`

---

## Common Workflows

### Workflow 1: Create Weekly LinkedIn Posts

```
1. CMO Orchestrator reviews content calendar
2. Assigns 3 topics to LinkedIn Generator
3. LinkedIn Generator writes drafts
4. Gatekeeper reviews each draft
5. Revisions if needed
6. Final posts saved to O-output/
7. Brand Monitor tracks performance
```

### Workflow 2: Write Thought Leadership Article

```
1. CMO Orchestrator identifies article topic
2. Briefs Thought Leader Agent
3. Thought Leader writes 1500-2500 word article
4. Gatekeeper reviews for voice + depth
5. Final article ready for rantimor.com
6. LinkedIn Generator creates promotional posts
```

### Workflow 3: Quarterly Planning

```
1. Content Strategy Agent analyzes:
   - Business goals
   - ICP pain points
   - Past performance (M-memory/)
2. Creates quarterly themes and topic roadmap
3. CMO Orchestrator reviews and approves
4. Plan saved to B-brain/content-calendar.md
5. Weekly execution begins
```

---

## Critical Reminders

### ALWAYS Read C-core/ First
Before writing ANY content, read:
- `C-core/voice-dna.md` - How Ran speaks
- `C-core/icp-profile.md` - Who we're serving

### NEVER Skip Gatekeeper Review
All content goes through Gatekeeper before publication.

### UPDATE M-memory After Publishing
Capture learnings so the system gets smarter over time.

### ONE AGENT AT A TIME
Don't try to be multiple agents at once. Activate the right specialist for the job.

---

## Special Skills

For enhanced capability, agents reference these specialized skills:

### For LinkedIn Generator
- `T-tools/skills/linkedin-copywriting-skill.md` - Templates, hooks, structure, examples

### For Trends Monitor
- `T-tools/skills/linkedin-engagement-strategy-skill.md` - Decision tree, timing, comment formulas

### For Brand Monitor & LinkedIn Analytics
- Uses M-memory/ files for learning patterns and past performance

---

## Prompts Library

For common tasks, use the prompt templates in `T-tools/prompts/`:

- `01-quarterly-content-plan.md` - Create strategic quarterly plan
- `02-create-linkedin-post.md` - Generate single LinkedIn post
- `03-create-thought-leadership-article.md` - Write long-form article
- `04-identify-engagement-opportunities.md` - Find conversations to join
- `05-analyze-performance.md` - Review content performance

---

## Success Metrics

**We're winning when:**
- Qualified inbound leads from B2B tech founders
- High engagement from ICP personas (not just generic likes)
- Thought leadership recognition (speaking invitations, advisory roles)
- Content quality improving (Gatekeeper approval rate rising)
- System learning (M-memory capturing valuable patterns)

---

## Need Help?

**For strategy:** Activate CMO Orchestrator or Content Strategy Agent
**For writing:** Activate LinkedIn Generator or Thought Leader Agent
**For quality:** Activate Gatekeeper
**For insights:** Activate Brand Monitor

**Remember:** Each agent has a specific job. Use the right specialist for the task.

---

## System Updates (Feb 26-27, 2026)

- ✅ Consolidated Engagement Agent into Trends Monitor (Feb 26)
- ✅ Clarified Brand Monitor vs LinkedIn Analytics Agent roles (Feb 26)
- ✅ Created LinkedIn Copywriting Skill (Feb 26)
- ✅ Created LinkedIn Engagement Strategy Skill (Feb 26)
- ✅ Added Quick Commands for faster agent activation (Feb 27)
- ✅ Updated agent list with new skills references (Feb 27)

---

*Last updated: 2026-02-27*

---

> **© Ran Timor**
> Website: [rantimor.com](https://rantimor.com)
> LinkedIn: [Ran Timor on LinkedIn](https://www.linkedin.com/in/ran-timor/)
