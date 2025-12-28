# CASA + Obsidian Workflow

A complete implementation of the CASA learning system using Obsidian as the central hub.

## Why Obsidian?

- **Free**: No subscription required
- **Local-first**: Your data stays on your device
- **Markdown**: Portable, future-proof format
- **Extensible**: Massive plugin ecosystem
- **Graph view**: Visualize knowledge connections

---

## Setup

### 1. Vault Structure

Create this folder structure in your Obsidian vault:

```
Your-Vault/
├── 00-Inbox/           # Captures land here
├── 01-Processing/      # Cards being structured
├── 02-Knowledge-Base/  # Finished cards by topic
│   ├── programming/
│   ├── security/
│   ├── devops/
│   └── ...
├── 03-Audio/           # Generated audio files
├── Templates/          # CASA templates
└── _config/            # Configuration files
```

### 2. Required Plugins

Install via Settings → Community Plugins:

| Plugin | Purpose |
|--------|---------|
| **Templater** | Advanced templates with variables |
| **QuickAdd** | Hotkey-triggered capture |
| **Dataview** | Query and filter cards |
| **Calendar** | Daily notes for captures |

Optional but recommended:

| Plugin | Purpose |
|--------|---------|
| **Periodic Notes** | Weekly reviews |
| **Tag Wrangler** | Manage tag taxonomy |
| **Kanban** | Track card processing |
| **Excalidraw** | Visual explanations |

### 3. Install Templates

Copy these files to your `Templates/` folder:

**Templates/CASA-Capture.md**
```markdown
---
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
status: unprocessed
tags: [inbox]
---

📖 **TERM**: <% tp.file.cursor() %>

💡 **ELI5**:


🔗 **MY PROJECTS**:
•
•
•

⌨️ **TRY NOW**:
```

```

🏷️ **Tags**:

📚 **Source**:
```

**Templates/CASA-Card.md**
```markdown
---
created: <% tp.date.now("YYYY-MM-DD") %>
source:
tags: []
status: active
---

### <% tp.file.title %>

**Q**: <% tp.file.cursor() %>

**A**:

**ELI5:**


**Commands/Code:**
```bash

```

**Use Cases:**
-
-
-

**Connections:**
- Related to: [[]]
- Builds on: [[]]
- Leads to: [[]]
```

### 4. Configure QuickAdd

Settings → QuickAdd → Add Choice:

**Capture (Template)**
- Name: "CASA Capture"
- Template Path: `Templates/CASA-Capture.md`
- File Name Format: `{{DATE:YYYYMMDD}}-{{VALUE:Term}}`
- Folder: `00-Inbox`

**Hotkey**: Set to `Cmd/Ctrl + Shift + C`

---

## Daily Workflow

### Morning (5 min)

1. Open Obsidian
2. Check `00-Inbox` for unprocessed captures
3. Move 2-3 to `01-Processing`

### During Learning

1. Hit `Cmd+Shift+C` when you learn something
2. Fill in the template quickly (30 seconds max)
3. Continue learning

### Evening (15 min)

1. Open `01-Processing`
2. Expand each capture into a full card
3. Move completed cards to `02-Knowledge-Base/{topic}/`
4. Update connections/links

### Weekly (30 min)

1. Review week's cards using Dataview
2. Identify gaps and connections
3. Generate audio for new cards
4. Listen during next week's commute

---

## Dataview Queries

Add these to your dashboard note:

### Unprocessed Captures

```dataview
TABLE created, source
FROM "00-Inbox"
WHERE status = "unprocessed"
SORT created DESC
LIMIT 10
```

### Recent Cards

```dataview
TABLE tags, source
FROM "02-Knowledge-Base"
WHERE status = "active"
SORT created DESC
LIMIT 20
```

### Cards by Tag

```dataview
TABLE file.folder as Topic, source
FROM "02-Knowledge-Base"
WHERE contains(tags, "#networking")
SORT created DESC
```

### Cards Without Connections

```dataview
LIST
FROM "02-Knowledge-Base"
WHERE !contains(file.outlinks, "")
LIMIT 10
```

---

## Audio Generation

### Option 1: CLI Script

```bash
# Generate audio for a knowledge base folder
python scripts/generate-audio.py \
  "vault/02-Knowledge-Base/security/nmap-basics.md" \
  --engine kokoro \
  --voice am_adam \
  --output "vault/03-Audio/nmap-basics.mp3"
```

### Option 2: Obsidian Shell Commands Plugin

Install "Shell commands" plugin and create:

```
Name: Generate Audio
Command: python /path/to/scripts/generate-audio.py "{{file_path:absolute}}" -o "{{vault_path}}/03-Audio/{{file_name}}.mp3"
```

Trigger from command palette: "Shell: Generate Audio"

---

## Tips

### Capture Fast, Structure Later

The capture template is intentionally minimal. Don't stop your learning flow to write perfect notes. Capture the essence in 30 seconds, refine later.

### Use Your Own Analogies

The ELI5 field is the most important part. Don't copy generic explanations. Use references from YOUR interests. "It's like in Zelda when..." will stick better than any textbook definition.

### Link Aggressively

Every card should link to:
- Prerequisites it builds on
- Related concepts
- Advanced topics it leads to

This creates the graph that makes Obsidian powerful.

### Review the Graph

Periodically open Graph View filtered to your knowledge base. Look for:
- Orphan nodes (cards with no connections)
- Clusters (dense topic areas)
- Bridges (concepts connecting different domains)

### Tag Consistently

Use a consistent tag taxonomy:

```
#domain/programming
#domain/security
#domain/networking

#type/concept
#type/command
#type/pattern
#type/tool

#status/active
#status/review
#status/archived
```

---

## Troubleshooting

**QuickAdd not creating files**
- Check template path is correct
- Ensure folder exists
- Try restarting Obsidian

**Dataview queries not working**
- Enable JavaScript queries in Dataview settings
- Check frontmatter YAML syntax
- Ensure files are in the queried folder

**Audio generation fails**
- Install TTS dependencies: `pip install kokoro-onnx soundfile`
- Check file paths use absolute paths
- Ensure Python is in your PATH

---

## Example Card

```markdown
---
created: 2024-01-15
source: TryHackMe - Nmap Basics
tags: [security, networking, scanning]
status: active
---

### Nmap SYN Scan

**Q**: Why does SYN scan require root privileges while TCP Connect doesn't?

**A**: SYN scan uses raw sockets to craft custom packets, which requires elevated privileges. TCP Connect uses the OS networking stack through standard system calls.

**ELI5:**
It's like the difference between writing your own letter (SYN - need special access to the mailroom) versus using the office mail system (Connect - anyone can drop a letter in the outbox). Raw sockets let you craft packets exactly how you want, but the OS protects that power.

**Commands/Code:**
```bash
# SYN scan (requires sudo)
sudo nmap -sS target_ip

# TCP Connect (no sudo needed)
nmap -sT target_ip

# Check if you have raw socket access
getcap $(which nmap)
```

**Use Cases:**
- Stealthier scanning (SYN doesn't complete handshake)
- When you only have unprivileged access (use -sT)
- Understanding scan detection in SOC work

**Connections:**
- Related to: [[TCP Three-Way Handshake]]
- Builds on: [[Network Privileges]]
- Leads to: [[Firewall Evasion Techniques]]
```

---

*Happy learning!*
