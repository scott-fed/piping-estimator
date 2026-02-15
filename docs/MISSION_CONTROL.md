# Mission Control for Piping Estimation Business

## Overview

Your friend runs a **company of one** doing piping estimates. Mission Control can automate most of his daily workflow, freeing him to focus on engineering work and client relationships.

---

## Recommended Agent Team

### 1. **Estimator** (The Core Agent)
**Role:** Runs the piping estimator tool and manages the estimation workflow

**Responsibilities:**
- Monitor incoming estimate requests (email, uploads)
- Process PDF drawings through the AI estimator
- Review AI-generated BOMs for accuracy
- Flag low-confidence items for manual review
- Generate cost estimates (when pricing is added)
- Create customer proposals
- Track estimate status (sent, pending, won, lost)

**Tools:**
- Piping estimator API
- Email integration (Gmail/Outlook)
- Calendar (track deadlines)
- File management (organize drawings)

**Heartbeat Tasks (Every 2 hours during business hours):**
- Check for new estimate requests
- Process pending drawings
- Send completed estimates to customers
- Follow up on proposals sent >3 days ago

---

### 2. **Bidmaster** (Project Tracker)
**Role:** Manages the sales pipeline and project tracking

**Responsibilities:**
- Track all bids/estimates (pipeline view)
- Monitor bid deadlines
- Follow up on pending proposals
- Track win/loss rate and reasons
- Manage project backlog (won bids → active projects)
- Send reminders for upcoming deadlines

**Tools:**
- Task management (lightweight CRM)
- Calendar integration
- Email automation

**Heartbeat Tasks (Daily at 8 AM):**
- Check for bid deadlines today/this week
- Follow up on proposals sent >5 days ago
- Update pipeline status
- Morning briefing: bids due, follow-ups needed

---

### 3. **Scribe** (Document Manager)
**Role:** Organizes drawings, estimates, and project files

**Responsibilities:**
- Auto-file incoming drawing PDFs
- Organize by project/client/date
- Version control for estimates
- Archive completed projects
- Search/retrieve old estimates quickly
- Backup critical files

**Tools:**
- File system automation
- Cloud storage (Google Drive, Dropbox)
- OCR for document search

**Heartbeat Tasks (Daily at 6 PM):**
- Organize today's files
- Backup new estimates/drawings
- Clean up temp files

---

### 4. **Pricer** (Cost Research)
**Role:** Maintains pricing database and researches material costs

**Responsibilities:**
- Update material pricing database (weekly)
- Research current prices from vendors (McMaster-Carr, Ferguson)
- Track price trends (alert on significant changes)
- Compare vendor pricing (find best deals)
- Monitor labor rate competitiveness

**Tools:**
- Web scraping (vendor websites)
- Pricing database
- Email (vendor newsletters)

**Heartbeat Tasks (Weekly on Mondays):**
- Update pricing database
- Check vendor emails for price changes
- Research any new materials/products

---

### 5. **Scout** (Email & Communication Manager)
**Role:** Handles customer communication and inbox triage

**Responsibilities:**
- Monitor email for estimate requests
- Extract project details from emails
- Auto-respond to inquiries (acknowledge receipt)
- Schedule follow-ups
- Draft proposal emails
- Track customer communication history

**Tools:**
- Email (Gmail/Outlook)
- Email templates
- Calendar

**Heartbeat Tasks (Every hour during business hours):**
- Check for new estimate requests
- Respond to urgent emails
- Queue low-priority emails for review
- Send scheduled follow-ups

---

### 6. **Ledger** (Finance & Invoicing)
**Role:** Handles invoicing and payment tracking

**Responsibilities:**
- Generate invoices from won estimates
- Track payment status (sent, paid, overdue)
- Send payment reminders
- Monitor cash flow
- Track expenses (subscriptions, tools, software)
- Prepare financial summaries (monthly)

**Tools:**
- Invoicing software (QuickBooks, FreshBooks, or custom)
- Bank account integration
- Email

**Heartbeat Tasks (Daily at 9 AM):**
- Check for new payments received
- Send reminders for invoices >30 days overdue
- Flag overdue invoices for follow-up

---

### 7. **Watcher** (Industry Monitor - Optional)
**Role:** Monitors industry trends and opportunities

**Responsibilities:**
- Monitor construction/project bid boards
- Track new construction projects (potential clients)
- Research competitors (pricing, services)
- Monitor industry news (new regulations, standards)
- Find networking/marketing opportunities

**Tools:**
- Web scraping (bid boards, news sites)
- RSS feeds
- Social media monitoring

**Heartbeat Tasks (Weekly on Thursdays):**
- Check bid boards for new opportunities
- Scan industry news
- Report interesting opportunities

---

## Minimal Viable Team (Start Here)

If your friend wants to start small, recommend **these 3 agents first**:

### Phase 1: Core Automation (2 weeks setup)
1. **Estimator** - Automates the PDF → BOM workflow
2. **Scout** - Handles email triage and customer communication
3. **Scribe** - Organizes files and drawings

**Impact:** Saves ~20 hours/week

### Phase 2: Business Management (1 week setup)
4. **Bidmaster** - Tracks pipeline and deadlines
5. **Ledger** - Invoicing and payment tracking

**Impact:** Adds ~10 hours/week savings

### Phase 3: Growth (1 week setup)
6. **Pricer** - Automated pricing updates
7. **Watcher** - Finds new opportunities

**Impact:** Enables scaling beyond one-person capacity

---

## Workflow Example: New Estimate Request

### Before Mission Control (Manual - 4+ hours)
1. Check email for estimate request
2. Download drawing PDFs
3. Read 100+ pages manually
4. Extract pipe specs to spreadsheet
5. Calculate quantities
6. Look up material prices
7. Create estimate document
8. Email proposal to customer
9. Set reminder to follow up

### After Mission Control (Automated - 15 minutes)
1. **Scout** detects estimate request email → extracts details → pings Estimator
2. **Estimator** downloads PDFs → runs AI analysis → generates BOM
3. **Pricer** applies current pricing → calculates total cost
4. **Estimator** generates proposal PDF → sends to your friend for quick review
5. Your friend reviews (5 min) → approves
6. **Scout** sends proposal to customer → schedules follow-up
7. **Bidmaster** adds to pipeline → tracks deadline
8. **Scribe** files drawings and estimate

**Human time:** 5-15 minutes (just review and approve)  
**Agent time:** ~10 minutes automated processing

---

## OpenClaw Configuration

### Workspace Structure
```
~/.openclaw/workspace/
├── AGENTS.md              # Standard Mission Control guide
├── SOUL.md                # Team personality (professional, efficient)
├── USER.md                # Your friend's profile
├── TOOLS.md               # Piping estimator tool config
├── HEARTBEAT.md           # Heartbeat schedule
├── MEMORY.md              # Long-term memory (client notes, lessons learned)
├── memory/
│   └── YYYY-MM-DD.md      # Daily logs
├── data/
│   ├── estimates.json     # Estimate tracking
│   ├── pipeline.json      # Sales pipeline
│   ├── pricing.json       # Material pricing database
│   └── clients.json       # Client database
└── skills/
    ├── piping-estimator/  # The tool we just built
    ├── email/             # Email integration
    ├── calendar/          # Calendar integration
    └── invoicing/         # Invoicing tools
```

### Agent Definitions (agents.json)
```json
{
  "agents": [
    {
      "id": "estimator",
      "name": "Estimator",
      "emoji": "🔧",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Runs piping estimator and manages estimation workflow",
      "heartbeat": "0 */2 9-17 * * *",
      "tools": ["piping-estimator", "email", "calendar", "files"]
    },
    {
      "id": "scout",
      "name": "Scout",
      "emoji": "📧",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Email triage and customer communication",
      "heartbeat": "0 */1 8-18 * * *",
      "tools": ["email", "calendar", "templates"]
    },
    {
      "id": "scribe",
      "name": "Scribe",
      "emoji": "📁",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Document management and file organization",
      "heartbeat": "0 18 * * *",
      "tools": ["files", "cloud-storage", "search"]
    },
    {
      "id": "bidmaster",
      "name": "Bidmaster",
      "emoji": "📊",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Sales pipeline and project tracking",
      "heartbeat": "0 8 * * *",
      "tools": ["tasks", "email", "calendar"]
    },
    {
      "id": "ledger",
      "name": "Ledger",
      "emoji": "💰",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Invoicing and payment tracking",
      "heartbeat": "0 9 * * *",
      "tools": ["invoicing", "email", "accounting"]
    },
    {
      "id": "pricer",
      "name": "Pricer",
      "emoji": "💵",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Pricing research and database maintenance",
      "heartbeat": "0 9 * * 1",
      "tools": ["web-scraping", "pricing-db", "email"]
    },
    {
      "id": "watcher",
      "name": "Watcher",
      "emoji": "👀",
      "model": "anthropic/claude-sonnet-4-5",
      "description": "Industry monitoring and opportunity finding",
      "heartbeat": "0 10 * * 4",
      "tools": ["web-scraping", "rss", "social-media"]
    }
  ]
}
```

---

## Integration with Piping Estimator Tool

### Skill Definition (skills/piping-estimator/SKILL.md)
```markdown
# Piping Estimator Skill

## Tool
**Command:** `piping-estimator`
**Path:** `~/Development/piping-estimator`
**API:** `http://localhost:8000/api`

## Usage

### Upload and analyze PDF
\`\`\`bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@drawing.pdf" \
  -o response.json
\`\`\`

### Get BOM
\`\`\`bash
curl http://localhost:8000/api/bom/<project_id> | jq
\`\`\`

### Export to Excel
\`\`\`bash
curl http://localhost:8000/api/export/<project_id>?format=xlsx \
  -o estimate.xlsx
\`\`\`

## Workflow

1. **Estimator agent** detects new estimate request (via Scout)
2. Downloads PDF from email attachment
3. Uploads to piping estimator API
4. Waits for analysis (polls status endpoint)
5. Reviews BOM and confidence scores
6. Flags low-confidence items (<70%) for manual review
7. Generates estimate with pricing (via Pricer)
8. Creates proposal document
9. Sends to customer (via Scout)
10. Tracks in pipeline (via Bidmaster)

## Error Handling

- **PDF too large:** Split into chunks or resize
- **Low accuracy:** Flag for manual review
- **API timeout:** Retry with exponential backoff
- **Missing specs:** Request clarification from customer
```

---

## Daily Workflow (After Setup)

### Morning (8:00 AM)
- **Bidmaster:** Daily briefing (bids due, follow-ups, pipeline status)
- **Ledger:** Payment check (new payments, overdue invoices)

### Throughout Day (9 AM - 5 PM)
- **Scout:** Email monitoring (hourly) → routes estimate requests to Estimator
- **Estimator:** Process drawings (every 2 hours) → generate estimates
- Notifications sent to Telegram/SMS when action needed

### Evening (6:00 PM)
- **Scribe:** File organization and backup

### Weekly (Monday 9 AM)
- **Pricer:** Update pricing database

### Weekly (Thursday 10 AM)
- **Watcher:** Industry scan and opportunity report

---

## Human-in-the-Loop Points

Your friend still makes these decisions (agents prepare, he approves):

1. **Estimate Review:** Agent generates BOM, he reviews before sending proposal
2. **Pricing Strategy:** Agent suggests price, he adjusts markup/margin
3. **Customer Communication:** Agent drafts emails, he reviews tone/content
4. **Bid Selection:** Agent finds opportunities, he decides which to pursue
5. **Quality Control:** Agent flags issues, he investigates root cause

**Goal:** Agents do the tedious work, human focuses on judgment and relationships.

---

## Setup Checklist

### Phase 1: Core Tools (Week 1)
- [ ] Install OpenClaw on his machine
- [ ] Set up piping estimator tool (docker-compose up)
- [ ] Configure email integration (Gmail/Outlook)
- [ ] Configure cloud storage (Google Drive/Dropbox)
- [ ] Create agent definitions (Estimator, Scout, Scribe)
- [ ] Test end-to-end workflow with sample drawing
- [ ] Train him on reviewing AI-generated BOMs

### Phase 2: Business Tools (Week 2)
- [ ] Set up pipeline tracking (Bidmaster)
- [ ] Configure invoicing integration (Ledger)
- [ ] Import existing client data
- [ ] Create email templates
- [ ] Set up Telegram/SMS notifications

### Phase 3: Automation (Week 3)
- [ ] Build pricing scraper (Pricer)
- [ ] Set up industry monitoring (Watcher)
- [ ] Configure all heartbeat schedules
- [ ] Optimize agent coordination
- [ ] Fine-tune prompts based on usage

---

## Success Metrics

Track these to measure Mission Control impact:

**Time Savings:**
- Estimate time: Before (4+ hours) → After (15 min)
- Weekly hours saved: 20-30 hours
- More estimates per week: 2x-3x increase

**Business Growth:**
- Win rate (% of bids won)
- Average proposal turnaround time
- Customer satisfaction (faster responses)
- Revenue increase (more bids → more wins)

**Quality:**
- BOM accuracy (95%+ target)
- Estimate errors (should decrease)
- Missed deadlines (should be zero with Bidmaster)

---

## Cost Estimate

**AI API Costs:**
- Anthropic Claude: ~$0.10-0.50 per drawing page
- 10 estimates/week × 100 pages avg = 1,000 pages/week
- **Weekly API cost:** ~$100-500
- **Monthly:** ~$400-2,000

**OpenClaw Hosting:**
- Self-hosted on his machine: $0
- Cloud hosting (optional): $50-100/month

**Total Monthly Cost:** $400-2,100

**ROI Calculation:**
- Hours saved per month: ~100 hours
- Value at $100/hour: **$10,000/month**
- **ROI: 500%+**

Even at the high end of API costs, this pays for itself many times over.

---

## Future Enhancements

Once core system is running smoothly:

1. **Mobile App:** Upload drawings from job site
2. **Client Portal:** Customers track estimate status
3. **Proposal Templates:** Branded, professional proposals
4. **Learning:** Train custom model on his historical drawings
5. **Integration:** Connect to QuickBooks, Procore, etc.
6. **Team Expansion:** If he hires help, agents coordinate team

---

## Next Steps

1. ✅ PRD and project structure created
2. ⏳ Get sample drawings from your friend
3. ⏳ Answer questions in docs/QUESTIONS.md
4. ⏳ Build MVP piping estimator (2-3 weeks)
5. ⏳ Set up Mission Control on his machine
6. ⏳ Configure agents and workflows
7. ⏳ Test with real projects
8. ⏳ Train him on the system
9. ⏳ Launch and iterate

---

**This setup will transform his one-person company into a highly efficient operation that can compete with larger firms while maintaining quality and personal service.** 🚀
