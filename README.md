# CreatorStudioAI

**AI-powered Creator Studio for a one-person company with zero employees.**

This repository implements the fully automated AI content creation, translation, publishing, and sales system demonstrated in the ReStructure AI YouTube Short.

Nothing goes public until you explicitly approve it. Claude Code (or any LLM agent) orchestrates the entire workflow while tracking **revenue**, not just views.

## Modules

### 1. Voice Module
- Speak into your phone for ~2 minutes (or provide a transcript/audio file).
- Claude turns the raw input into a polished full script.
- ElevenLabs synthesizes the script in **your cloned voice**.
- You listen and approve.

### 2. Video & Dubbing Module
- Snap a few photos (or provide image paths).
- Higgsfield AI generates video clips from the photos.
- Descript syncs everything to your voice, adds captions, and prepares the edit.
- ElevenLabs dubs the final video into **10 languages** while preserving your voice.
- You approve the versions.

### 3. Multi-Platform Posting
- Metricool (or equivalent) schedules and posts approved content to:
  - YouTube
  - TikTok
  - Instagram
  - Facebook
- Optimal posting times per country/language (Spain, Brazil, etc.).

### 4. AI Sales Line
- An AI version of **you** handles inbound inquiries for courses, coaching, or brand deals.
- It clearly identifies itself as AI.
- Answers questions, qualifies leads, and routes to checkout or books a call.
- You only engage on high-value opportunities.

### 5. Daily Orchestration & Revenue Tracking
- Claude Code manages the full pipeline.
- Tracks actual revenue (sales, not vanity metrics).
- Every morning: a one-page summary of what converted and what video to make next.

## Architecture

```
src/creator_studio/
├── orchestrator.py          # Main agent loop (Claude Code style)
├── modules/
│   ├── voice.py
│   ├── video.py
│   ├── sales.py
│   ├── posting.py
│   └── reporting.py
├── clients/                 # Real + Mock implementations
│   ├── claude.py
│   ├── elevenlabs.py
│   ├── higgsfield.py
│   ├── descript.py
│   └── metricool.py
└── models.py
```

All external services have **mock implementations** so you can run the entire demo end-to-end without API keys. Drop in real credentials via environment variables or `config/settings.yaml` to go live.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/wa-phil/CreatorStudioAI.git
cd CreatorStudioAI
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run the full demo pipeline (uses mocks)
python scripts/run_pipeline.py

# Generate a daily revenue summary
python scripts/generate_daily_summary.py
```

## Configuration

Copy the example config:

```bash
cp config/settings.example.yaml config/settings.yaml
```

Set environment variables for production:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export ELEVENLABS_API_KEY=...
export HIGGSFIELD_API_KEY=...
# etc.
```

## Human Approval Gates

Every stage that produces public content requires explicit approval:

1. Script + Voice audio
2. Final video (original + dubbed versions)
3. Posting schedule
4. Sales responses that involve pricing/commitment

The orchestrator pauses and waits for your sign-off (CLI prompt, webhook, or future UI).

## Daily Summary Example

```markdown
# CreatorStudioAI Daily Summary — 2026-11-12

## Revenue (Last 24h)
- Course sales: $1,240 (3 conversions)
- Coaching calls booked: 2
- Brand deal inquiries qualified: 1

## Content Performance
- "How I Built This System" (ES): 12.4k views, 3 sales
- Recommendation: Make a follow-up on the AI sales line in Portuguese

## Next Actions
1. Approve pending video #47
2. Review 2 high-value sales leads
```

## Roadmap

- [ ] Web UI for approvals and monitoring
- [ ] Real Metricool / Buffer integration
- [ ] Local voice cloning fallback
- [ ] Cost tracking per video (token + API spend)
- [ ] Multi-creator support

## License

MIT

---

Inspired by the ReStructure AI short: [I Built an Entire AI Creator Studio With 0 Employees](https://www.youtube.com/shorts/KigUHSCgDNo)
