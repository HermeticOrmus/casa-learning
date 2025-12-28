# CASA + n8n Automation Workflow

Fully automated knowledge pipeline using n8n for zero-friction learning.

---

## Why Automate?

Manual systems have friction. Friction kills consistency. Automation removes friction.

**What we're automating:**
- Capture parsing and structuring
- Card creation with AI assistance
- Spaced repetition scheduling
- Audio generation queuing
- Weekly digest delivery

---

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Capture   │────▶│   Process   │────▶│   Store     │
│  Channels   │     │   (AI)      │     │  (Notion/   │
│             │     │             │     │   Obsidian) │
└─────────────┘     └─────────────┘     └─────────────┘
       │                                       │
       │                                       ▼
       │                              ┌─────────────┐
       │                              │   Review    │
       │                              │  Scheduler  │
       └──────────────────────────────┤             │
                                      └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │   Audio     │
                                      │  Generator  │
                                      └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │   Deliver   │
                                      │  (Podcast/  │
                                      │   WhatsApp) │
                                      └─────────────┘
```

---

## Workflow 1: Telegram Capture → Notion

**Trigger**: New message in Telegram bot

**Flow**:
1. Receive message from personal Telegram bot
2. Parse capture format (term, ELI5, etc.)
3. Enhance with Claude API (expand ELI5, suggest tags)
4. Create Notion page in Inbox
5. Reply with confirmation

### n8n Nodes

```
[Telegram Trigger]
    → [Parse Message]
    → [Claude API - Enhance]
    → [Notion - Create Page]
    → [Telegram - Send Reply]
```

### Parse Message (Code Node)

```javascript
const text = $input.first().json.message.text;

// Parse capture format
const termMatch = text.match(/📖\s*(?:TERM)?:?\s*(.+?)(?=💡|🔗|⌨️|$)/is);
const eli5Match = text.match(/💡\s*(?:ELI5)?:?\s*(.+?)(?=🔗|⌨️|$)/is);
const projectsMatch = text.match(/🔗\s*(?:PROJECTS)?:?\s*(.+?)(?=⌨️|$)/is);
const actionMatch = text.match(/⌨️\s*(?:TRY NOW)?:?\s*(.+?)$/is);

return [{
  json: {
    term: termMatch ? termMatch[1].trim() : text.substring(0, 100),
    eli5: eli5Match ? eli5Match[1].trim() : '',
    projects: projectsMatch ? projectsMatch[1].trim() : '',
    action: actionMatch ? actionMatch[1].trim() : '',
    raw: text
  }
}];
```

### Claude Enhancement (HTTP Request)

```json
{
  "model": "claude-3-haiku-20240307",
  "max_tokens": 500,
  "messages": [{
    "role": "user",
    "content": "Enhance this learning capture. Add suggested tags and expand the ELI5 if it's too brief.\n\nTerm: {{$json.term}}\nELI5: {{$json.eli5}}\n\nRespond in JSON: {\"enhanced_eli5\": \"...\", \"suggested_tags\": [\"...\"], \"difficulty\": \"beginner|intermediate|advanced\"}"
  }]
}
```

---

## Workflow 2: Weekly Review Digest

**Trigger**: Schedule (Sunday 9am)

**Flow**:
1. Query Notion for cards needing review
2. Generate summary with Claude
3. Create audio digest
4. Send via WhatsApp/Email

### n8n Nodes

```
[Schedule Trigger]
    → [Notion - Query DB]
    → [Claude - Summarize]
    → [OpenAI TTS - Generate]
    → [WhatsApp - Send Audio]
```

### Query Cards for Review (Notion Node)

```json
{
  "filter": {
    "and": [
      {
        "property": "Last Reviewed",
        "date": {
          "before": "{{$today.minus({days: 7}).toISO()}}"
        }
      },
      {
        "property": "Status",
        "select": {
          "equals": "Active"
        }
      }
    ]
  },
  "sorts": [
    {
      "property": "Last Reviewed",
      "direction": "ascending"
    }
  ],
  "page_size": 10
}
```

---

## Workflow 3: Audio Generation Queue

**Trigger**: Webhook (manual) or Schedule

**Flow**:
1. Get unprocessed cards from topic
2. Generate narrative script with Claude
3. Generate audio with TTS
4. Upload to storage
5. Update card with audio link

### Script Generation Prompt

```
You are creating a learning audio script. Convert these flashcards into a
natural, conversational narrative suitable for listening during a commute.

Use the learner's personal anchors for analogies:
- Interests: {{$json.interests}}
- Projects: {{$json.projects}}
- Career goal: {{$json.career}}

Cards to include:
{{$json.cards}}

Create a 10-15 minute script with:
1. Hook (why this matters)
2. Foundation (simple explanation)
3. Deep dive (technical details with analogies)
4. Application (how to use in their projects)
5. Recap

Write in second person ("you"), conversational tone, with natural pauses.
```

---

## Workflow 4: Spaced Repetition Scheduler

**Trigger**: Daily at 8am

**Flow**:
1. Query cards by review interval
2. Calculate which cards are due
3. Send daily review list via preferred channel

### Interval Logic (Code Node)

```javascript
const cards = $input.all().map(item => item.json);

const intervals = [1, 3, 7, 14, 30, 90]; // days

const today = new Date();
const dueCards = cards.filter(card => {
  const lastReview = new Date(card.last_reviewed);
  const reviewCount = card.review_count || 0;
  const interval = intervals[Math.min(reviewCount, intervals.length - 1)];
  const dueDate = new Date(lastReview.getTime() + interval * 24 * 60 * 60 * 1000);
  return dueDate <= today;
});

return dueCards.map(card => ({ json: card }));
```

---

## Self-Hosted Setup

### Requirements

- n8n instance (Docker or npm)
- API keys: Claude, OpenAI (optional), Notion, Telegram

### Docker Compose

```yaml
version: '3'
services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=your-password
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - NOTION_API_KEY=${NOTION_API_KEY}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
```

### Environment Variables

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...
NOTION_API_KEY=secret_...
TELEGRAM_BOT_TOKEN=123456:ABC...
OPENAI_API_KEY=sk-...  # Optional, for TTS
ELEVENLABS_API_KEY=... # Optional, for premium TTS
```

---

## Cost Estimation

| Component | Monthly Cost |
|-----------|-------------|
| n8n (self-hosted) | $5-10 (VPS) |
| Claude API (Haiku) | ~$2-5 |
| OpenAI TTS | ~$5-10 |
| Notion | Free / $10 |
| Telegram | Free |
| **Total** | **~$15-30/month** |

---

## Workflow Templates

Import these JSON files into n8n:

- `telegram-capture.json` - Capture from Telegram
- `weekly-digest.json` - Sunday review summary
- `audio-generator.json` - Batch audio creation
- `spaced-repetition.json` - Daily review scheduler

*(Templates in `/workflows/n8n-automation/templates/`)*

---

## Tips

### Start Simple
Begin with just Telegram → Notion. Add complexity once that's stable.

### Monitor Failures
Set up error notifications. Broken automation is worse than no automation.

### Rate Limit APIs
Add delays between API calls to avoid hitting limits.

### Cache Expensive Calls
Store AI-generated content to avoid regenerating.

### Log Everything
Use n8n's execution history to debug issues.

---

*Automation is a multiplier. Get the manual workflow right first, then automate.*
