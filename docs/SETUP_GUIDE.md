# Setup Guide: Mission Control for Piping Estimation

This guide walks through setting up OpenClaw Mission Control for your piping estimation business.

---

## Prerequisites

- Mac or Linux machine (Windows WSL2 also works)
- Python 3.11+
- Docker Desktop
- Node.js 18+ (for OpenClaw)
- Anthropic API key
- Email account (Gmail or Outlook)

---

## Step 1: Install OpenClaw

```bash
# Install OpenClaw globally
npm install -g openclaw

# Initialize your workspace
openclaw init

# Start the gateway daemon
openclaw gateway start
```

---

## Step 2: Install Piping Estimator Tool

```bash
# Clone the estimator tool
cd ~/Development
git clone https://github.com/scott-fed/piping-estimator.git
cd piping-estimator

# Set up Python environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your Anthropic API key

# Start database
docker-compose up -d

# Run migrations
alembic upgrade head

# Start the API (in background)
nohup uvicorn src.main:app --host 0.0.0.0 --port 8000 &
```

**Verify it works:**
```bash
curl http://localhost:8000/health
# Should return: {"status": "ok"}
```

---

## Step 3: Configure OpenClaw Workspace

```bash
cd ~/.openclaw/workspace
```

### Create SOUL.md
```markdown
# SOUL.md - Mission Control Team

We run a professional piping estimation business.

**Vibe:** Efficient, detail-oriented, client-focused. We deliver accurate estimates fast.

**Core Values:**
- Accuracy first (better to flag for review than miss a spec)
- Speed without sacrificing quality
- Proactive communication with clients
- Continuous improvement (learn from every project)

**Tone:** Professional but friendly. We're the reliable expert clients trust.
```

### Create USER.md
```markdown
# USER.md - Business Owner Profile

- **Name:** [Your friend's name]
- **Company:** [Company name]
- **Specialization:** Mechanical piping systems (industrial, commercial)
- **Timezone:** [His timezone]
- **Availability:** [His working hours]

## Preferences
- Review all estimates before sending (trust but verify)
- Conservative markup strategy (competitive but profitable)
- Quick turnaround wins contracts (respond within 24 hours)
- Maintain high accuracy (reputation is everything)

## Communication
- Telegram: [Phone number]
- Email: [Business email]
- Preferred notification times: [e.g., 8 AM - 6 PM weekdays]
```

### Create TOOLS.md
```markdown
# TOOLS.md - Business Tools

## Piping Estimator API
- **Endpoint:** http://localhost:8000/api
- **Health check:** curl http://localhost:8000/health
- **Upload PDF:** POST /api/upload
- **Get BOM:** GET /api/bom/{project_id}
- **Export:** GET /api/export/{project_id}?format=xlsx

## Email
- **Provider:** Gmail / Outlook
- **Address:** [Business email]
- **Integration:** [Configure email skill]

## File Storage
- **Local:** ~/Documents/Projects/
- **Cloud:** Google Drive / Dropbox
- **Backup:** Daily at 6 PM

## Pricing Sources
- McMaster-Carr: https://www.mcmaster.com
- Ferguson: https://www.ferguson.com
- [Add other vendors]

## Invoicing
- **Software:** QuickBooks / FreshBooks / [Other]
- **Payment terms:** Net 30
- **Late fee:** 1.5% per month after 30 days
```

### Create HEARTBEAT.md
```markdown
# HEARTBEAT.md - Agent Coordination

## Estimator (Every 2 hours, 9 AM - 5 PM)
- Check for new estimate requests (via Scout)
- Process pending drawings
- Generate BOMs and flag for review
- Send completed estimates

## Scout (Hourly, 8 AM - 6 PM)
- Monitor email inbox
- Extract estimate requests
- Route to Estimator
- Send scheduled follow-ups

## Bidmaster (Daily, 8 AM)
- Morning briefing: bids due today/this week
- Follow up on proposals sent >5 days ago
- Update pipeline status

## Scribe (Daily, 6 PM)
- Organize today's files
- Backup drawings and estimates
- Clean up temp files

## Ledger (Daily, 9 AM)
- Check for new payments
- Send reminders for overdue invoices
- Weekly financial summary (Fridays)

## Pricer (Weekly, Monday 9 AM)
- Update pricing database
- Check vendor emails for price changes
- Research new materials

## Watcher (Weekly, Thursday 10 AM)
- Scan bid boards for opportunities
- Industry news summary
- Competitor monitoring
```

---

## Step 4: Install Skills

```bash
cd ~/.openclaw/workspace/skills

# Create piping-estimator skill
mkdir -p piping-estimator
cat > piping-estimator/SKILL.md << 'EOF'
# Piping Estimator Skill

Control the piping estimator API.

## Commands

### Upload PDF
\`\`\`bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/drawing.pdf"
\`\`\`

### Get project status
\`\`\`bash
curl http://localhost:8000/api/projects/{id}
\`\`\`

### Get BOM
\`\`\`bash
curl http://localhost:8000/api/bom/{id}
\`\`\`

### Export to Excel
\`\`\`bash
curl http://localhost:8000/api/export/{id}?format=xlsx -o estimate.xlsx
\`\`\`

## Error Handling
- Check API health before upload: `curl http://localhost:8000/health`
- If timeout, the drawing is likely too large (split or resize)
- If confidence < 70%, flag items for manual review
EOF

# Install email skill (if not already installed)
openclaw skills install email

# Install calendar skill
openclaw skills install calendar
```

---

## Step 5: Create Agent Definitions

Create `~/.openclaw/agents.json`:

```json
{
  "agents": [
    {
      "id": "estimator",
      "name": "Estimator",
      "emoji": "🔧",
      "model": "anthropic/claude-sonnet-4-5",
      "sessionType": "isolated",
      "heartbeat": {
        "enabled": true,
        "schedule": "0 */2 9-17 * * 1-5",
        "prompt": "Check for new estimate requests and process pending drawings. Follow HEARTBEAT.md instructions for Estimator."
      }
    },
    {
      "id": "scout",
      "name": "Scout",
      "emoji": "📧",
      "model": "anthropic/claude-sonnet-4-5",
      "sessionType": "isolated",
      "heartbeat": {
        "enabled": true,
        "schedule": "0 */1 8-18 * * 1-5",
        "prompt": "Monitor email for estimate requests and customer communication. Follow HEARTBEAT.md instructions for Scout."
      }
    },
    {
      "id": "scribe",
      "name": "Scribe",
      "emoji": "📁",
      "model": "anthropic/claude-sonnet-4-5",
      "sessionType": "isolated",
      "heartbeat": {
        "enabled": true,
        "schedule": "0 18 * * 1-5",
        "prompt": "Organize files and backup drawings/estimates. Follow HEARTBEAT.md instructions for Scribe."
      }
    },
    {
      "id": "bidmaster",
      "name": "Bidmaster",
      "emoji": "📊",
      "model": "anthropic/claude-sonnet-4-5",
      "sessionType": "isolated",
      "heartbeat": {
        "enabled": true,
        "schedule": "0 8 * * 1-5",
        "prompt": "Provide daily briefing and manage sales pipeline. Follow HEARTBEAT.md instructions for Bidmaster."
      }
    },
    {
      "id": "ledger",
      "name": "Ledger",
      "emoji": "💰",
      "model": "anthropic/claude-sonnet-4-5",
      "sessionType": "isolated",
      "heartbeat": {
        "enabled": true,
        "schedule": "0 9 * * 1-5",
        "prompt": "Check payments and manage invoices. Follow HEARTBEAT.md instructions for Ledger."
      }
    }
  ]
}
```

---

## Step 6: Set Up Data Files

```bash
cd ~/.openclaw/workspace/data
mkdir -p estimates pipeline pricing clients

# Initialize estimate tracking
cat > estimates.json << 'EOF'
{
  "estimates": [],
  "nextId": 1
}
EOF

# Initialize pipeline
cat > pipeline.json << 'EOF'
{
  "stages": ["inbox", "analyzing", "pricing", "sent", "won", "lost"],
  "deals": []
}
EOF

# Initialize client database
cat > clients.json << 'EOF'
{
  "clients": []
}
EOF
```

---

## Step 7: Configure Notifications

Edit `~/.openclaw/openclaw.json` and add Telegram:

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowedUsers": ["YOUR_TELEGRAM_ID"]
    }
  }
}
```

**Get a Telegram bot:**
1. Message @BotFather on Telegram
2. Create new bot: `/newbot`
3. Copy the token
4. Get your Telegram ID: message @userinfobot

---

## Step 8: Test the System

### Test 1: Upload a sample drawing
```bash
# Place a sample PDF in ~/Downloads/test-drawing.pdf
curl -X POST http://localhost:8000/api/upload \
  -F "file=@$HOME/Downloads/test-drawing.pdf" | jq
```

### Test 2: Trigger Estimator manually
```bash
openclaw agent run estimator "Process the test drawing and show me the BOM"
```

### Test 3: Test Scout (email monitoring)
```bash
openclaw agent run scout "Check email for new estimate requests from the last 24 hours"
```

### Test 4: Test full workflow
1. Email yourself with subject "New Estimate Request"
2. Attach a sample drawing PDF
3. Wait for Scout's next heartbeat (or trigger manually)
4. Scout should detect it and route to Estimator
5. Estimator processes and notifies you on Telegram
6. Review BOM and approve
7. Estimate sent to customer

---

## Step 9: Go Live

### Week 1: Monitor Mode
- Let agents run but review everything they do
- Fine-tune prompts and workflows
- Adjust heartbeat schedules if needed

### Week 2: Trust & Verify
- Agents handle routine tasks autonomously
- You review outputs before sending to clients
- Track time savings and accuracy

### Week 3: Full Automation
- Agents trusted for most tasks
- You focus on exceptions and client relationships
- Measure business impact (more estimates, faster turnaround)

---

## Troubleshooting

### Piping estimator API not responding
```bash
# Check if it's running
curl http://localhost:8000/health

# Restart if needed
cd ~/Development/piping-estimator
docker-compose restart
uvicorn src.main:app --reload
```

### Agent not running on heartbeat
```bash
# Check gateway status
openclaw gateway status

# View agent logs
openclaw logs estimator

# Test agent manually
openclaw agent run estimator "Test message"
```

### Email integration not working
```bash
# Verify email skill installed
openclaw skills list

# Test email access
openclaw agent run scout "List the last 5 emails"
```

### Low BOM accuracy
- Check drawing quality (enhance scans if blurry)
- Review AI vision prompts (may need examples)
- Adjust confidence thresholds
- Add manual review step for critical projects

---

## Maintenance

### Daily
- Review agent activity (morning briefing from Bidmaster)
- Approve estimates before sending
- Check for errors or stuck tasks

### Weekly
- Review pricing updates (Pricer runs Mondays)
- Check opportunity reports (Watcher runs Thursdays)
- Backup workspace files

### Monthly
- Review API costs and usage
- Analyze time savings and ROI
- Optimize workflows based on patterns
- Update agent prompts if needed

---

## Support

- **OpenClaw Docs:** https://docs.openclaw.ai
- **Piping Estimator:** https://github.com/scott-fed/piping-estimator
- **Discord Community:** https://discord.com/invite/clawd

---

**You're all set! Mission Control will now handle the tedious parts of estimation, freeing you to focus on engineering and growing the business.** 🚀
