# CASA + Notion Workflow

A database-powered implementation of CASA using Notion's relational features.

---

## Why Notion?

- **Relational databases**: Link captures to cards to topics
- **Views**: Filter cards by status, topic, date
- **Mobile app**: Capture on the go
- **Templates**: One-click card creation
- **API**: Automate with n8n, Zapier, or scripts

---

## Database Structure

Create three linked databases:

### 1. Inbox (Captures)

| Property | Type | Purpose |
|----------|------|---------|
| Name | Title | The term/concept |
| ELI5 | Text | Your analogy |
| Projects | Multi-select | Which projects this applies to |
| Try Now | Text | Immediate action |
| Source | Text | Where you learned this |
| Status | Select | Unprocessed, Processing, Done |
| Created | Date | Auto-timestamp |
| → Card | Relation | Links to structured card |

### 2. Knowledge Base (Cards)

| Property | Type | Purpose |
|----------|------|---------|
| Name | Title | Card title |
| Question | Text | The Q |
| Answer | Text | The A |
| ELI5 | Text | Your analogy (from capture) |
| Commands | Text | Code/actions |
| Use Cases | Text | Applications |
| Topic | Select | Category |
| Tags | Multi-select | Searchable tags |
| Difficulty | Select | Beginner/Intermediate/Advanced |
| Status | Select | Draft, Active, Review, Archived |
| ← Capture | Relation | Original capture |
| → Related | Relation | Self-relation for connections |
| Last Reviewed | Date | Spaced repetition tracking |

### 3. Topics (Organization)

| Property | Type | Purpose |
|----------|------|---------|
| Name | Title | Topic name |
| Description | Text | What this covers |
| Icon | Text | Emoji for visual identification |
| Cards | Relation | All cards in this topic |
| Card Count | Rollup | Count of cards |

---

## Views to Create

### Inbox Views

**Unprocessed** (Default)
- Filter: Status = "Unprocessed"
- Sort: Created (newest first)

**This Week's Captures**
- Filter: Created is within past week
- Sort: Created (newest first)

### Knowledge Base Views

**By Topic** (Gallery)
- Group by: Topic
- Sort: Name A→Z

**Review Queue** (Table)
- Filter: Last Reviewed is before 7 days ago
- Sort: Last Reviewed (oldest first)

**Recently Added** (List)
- Filter: Status = "Active"
- Sort: Created (newest first)
- Limit: 20

**Search All** (Table)
- No filters
- Show all properties
- Enable search

---

## Templates

### Capture Template

Create a template in Inbox database:

```
Name: [Term]
Status: Unprocessed

---

📖 **TERM**: {cursor here}

💡 **ELI5**:


🔗 **PROJECTS**:


⌨️ **TRY NOW**:


📚 **SOURCE**:
```

### Card Template

Create a template in Knowledge Base:

```
Name: [Card Title]
Status: Draft
Topic: {select}

---

**Q**: {cursor}

**A**:

---

**ELI5:**


**Commands/Code:**
```
{code}
```

**Use Cases:**
-
-
-

**Connections:**
- Related to:
- Builds on:
- Leads to:
```

---

## Daily Workflow

### Capture (Throughout Day)

1. Open Notion mobile app
2. Quick Add → Inbox database
3. Use capture template
4. Fill in 30 seconds, move on

**Pro tip**: Add Inbox to mobile home screen widget

### Process (Evening, 15 min)

1. Open Inbox → Unprocessed view
2. For each capture:
   - Create linked Card in Knowledge Base
   - Expand ELI5, add code examples
   - Set Topic and Tags
   - Mark capture as "Done"

### Review (Weekly, 30 min)

1. Open Knowledge Base → Review Queue
2. For each card:
   - Read through
   - Add any new connections
   - Update "Last Reviewed" date
3. Check Topics view for gaps

---

## Automation Ideas

### Notion API + Python

```python
from notion_client import Client

notion = Client(auth="your-integration-token")

# Create capture programmatically
def quick_capture(term, eli5, source):
    notion.pages.create(
        parent={"database_id": "your-inbox-db-id"},
        properties={
            "Name": {"title": [{"text": {"content": term}}]},
            "ELI5": {"rich_text": [{"text": {"content": eli5}}]},
            "Source": {"rich_text": [{"text": {"content": source}}]},
            "Status": {"select": {"name": "Unprocessed"}}
        }
    )
```

### iOS Shortcuts

Create a shortcut that:
1. Prompts for Term
2. Prompts for ELI5
3. Calls Notion API to create capture
4. Confirms with haptic feedback

### Raycast Extension

Use Raycast's Notion integration for instant capture from anywhere on Mac.

---

## Export for Audio

### Manual Export

1. Open Knowledge Base → Filter by Topic
2. Export as Markdown
3. Run through `generate-audio.py`

### API Export

```python
def export_topic_for_audio(topic_name):
    # Query cards by topic
    results = notion.databases.query(
        database_id="knowledge-base-id",
        filter={
            "property": "Topic",
            "select": {"equals": topic_name}
        }
    )

    # Format as script
    script = f"# {topic_name}\n\n"
    for card in results["results"]:
        props = card["properties"]
        script += f"""
## {props["Name"]["title"][0]["text"]["content"]}

{props["Question"]["rich_text"][0]["text"]["content"]}

{props["Answer"]["rich_text"][0]["text"]["content"]}

{props["ELI5"]["rich_text"][0]["text"]["content"]}

---
"""
    return script
```

---

## Tips

### Use Database Templates
Every new capture should start from template - never blank.

### Leverage Filters
Create saved filters for common queries:
- "Networking cards I haven't reviewed"
- "Cards from TryHackMe"
- "Advanced difficulty"

### Link Everything
Notion's power is relations. Every card should link to:
- Its original capture
- Related cards (siblings)
- Prerequisite cards (parents)
- Advanced cards (children)

### Weekly Database Maintenance
- Archive old/irrelevant cards
- Merge duplicate captures
- Update topic organization
- Clean up unused tags

---

## Limitations

- **Offline**: Notion requires internet (use Obsidian for offline-first)
- **Speed**: Can feel slow compared to plain markdown
- **Lock-in**: Data export is good but not perfect
- **Cost**: Free tier has limits; Pro is $10/month

---

*Choose Notion if you value views, relations, and visual organization over speed and offline access.*
