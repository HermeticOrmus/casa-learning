<p align="center">
  <img src="https://ormus.solutions/mascot/pixellab_liquid_to_seed.gif" alt="CASA Learning" width="128" style="image-rendering: pixelated;" />
</p>

<h1 align="center">CASA Learning</h1>

<p align="center">
  <em>Capture, Anchor, Structure, Absorb -- AI-powered learning framework</em>
</p>

<p align="center">
  <a href="https://github.com/HermeticOrmus/casa-learning/stargazers"><img src="https://img.shields.io/github/stars/HermeticOrmus/casa-learning?style=flat-square&color=aa8142" alt="Stars" /></a>
  <a href="https://github.com/HermeticOrmus/casa-learning/blob/main/LICENSE"><img src="https://img.shields.io/github/license/HermeticOrmus/casa-learning?style=flat-square&color=aa8142" alt="License" /></a>
  <a href="https://github.com/HermeticOrmus/casa-learning/commits"><img src="https://img.shields.io/github/last-commit/HermeticOrmus/casa-learning?style=flat-square&color=aa8142" alt="Last Commit" /></a>
  <img src="https://img.shields.io/badge/Python-aa8142?style=flat-square&logo=python&logoColor=white" alt="Python" />
</p>

---

> A plug-and-play learning system that turns information into lasting knowledge through multi-modal reinforcement.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## The Problem

You consume content constantly—courses, tutorials, documentation, videos. A week later, you remember almost nothing. Notes sit untouched. Bookmarks pile up. The knowledge never becomes *yours*.

## The Solution

CASA is a 4-phase system that transforms passive consumption into active knowledge through:

1. **Immediate capture** before memory fades
2. **Personal anchoring** to your interests and projects
3. **Structured reference** for future retrieval
4. **Passive absorption** during downtime

```
CAPTURE → ANCHOR → STRUCTURE → ABSORB
   ↓         ↓          ↓          ↓
Instant   Personal   Reference   Passive
 grab     meaning     system    repetition
```

---

## Table of Contents

- [Quick Start](#quick-start)
- [The Four Phases](#the-four-phases)
- [Implementation Options](#implementation-options)
- [Workflow Examples](#workflow-examples)
- [Templates](#templates)
- [Tool Recommendations](#tool-recommendations)
- [Configuration](#configuration)
- [AI Integration](#ai-integration)
- [The Science](#the-science)
- [Philosophy](#philosophy)
- [Contributing](#contributing)

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/casa-learning.git
cd casa-learning

# Copy the configuration template
cp config.example.yaml config.yaml

# Edit with your personal anchors
# - Your interests (games, shows, hobbies)
# - Your active projects
# - Your career goals
```

Create your first capture:

```markdown
📖 TERM: [What you just learned]

💡 ELI5: [Explain using YOUR analogy]

🔗 MY PROJECTS:
• [How this applies to Project A]
• [How this applies to Project B]

⌨️ TRY NOW:
[One command or action to apply this immediately]
```

---

## The Four Phases

### Phase 1: CAPTURE

**Goal**: Grab knowledge within 30 seconds of learning it.

| Principle | Rationale |
|-----------|-----------|
| Immediate | Working memory decays exponentially |
| Frictionless | One action maximum |
| Mobile-ready | Learning happens everywhere |

**Trigger**: The moment you think "I should remember this."

**Anti-pattern**: "I'll write this down later." (You won't.)

---

### Phase 2: ANCHOR

**Goal**: Connect new knowledge to existing mental models.

The brain doesn't store isolated facts—it stores *relationships*. By explicitly connecting new concepts to things you already know deeply (games, shows, hobbies, projects), you create multiple retrieval paths.

**The Anchor Formula**:

```markdown
📖 TERM: [Concept Name]

💡 ELI5:
[Analogy from YOUR world—not generic examples]

🔗 PROJECT CONNECTIONS:
• Project A: [Specific application]
• Project B: [Specific application]
• Career Goal: [Why this matters for your path]

⌨️ IMMEDIATE ACTION:
[Command, code snippet, or action to try RIGHT NOW]

🏷️ Tags: #topic #subtopic #skill
```

**Key Insight**: Generic analogies ("it's like a filing cabinet") don't stick. Personal analogies ("it's like the Materia system in Final Fantasy VII") create emotional hooks that persist.

---

### Phase 3: STRUCTURE

**Goal**: Create searchable, reviewable reference material.

Raw captures are messy. Structure transforms them into a knowledge base you'll actually use.

**Card Format**:

```markdown
### Card N - [Term]
Q: [Question that tests understanding]
A: [Concise answer]

**ELI5:** [Your personal analogy]

**Commands/Code:**
```bash
# Practical, copy-paste ready
command --with flags
```

**Use Cases:**
- Real application 1
- Real application 2
- Real application 3

Tags: tag1, tag2, tag3
Source: [Course/Book/Video - Section]
```

**File Organization**:

```
knowledge-base/
├── cybersecurity/
│   ├── networking-fundamentals.md
│   ├── nmap-scanning.md
│   └── wireshark-analysis.md
├── programming/
│   ├── python-patterns.md
│   └── typescript-advanced.md
└── _templates/
    ├── capture-template.md
    └── card-template.md
```

---

### Phase 4: ABSORB

**Goal**: Passive reinforcement during downtime.

Convert structured cards into narrative audio for listening during:
- Commutes
- Workouts
- Gaming sessions
- Household chores
- Walking

**Audio Style Guidelines**:

| Do | Don't |
|----|-------|
| Narrative storytelling | Bullet point reading |
| Conversational tone | Lecture format |
| Personal references | Generic examples |
| 10-30 minute episodes | 2-minute clips |
| Mentor voice | Robotic TTS |

**Script Structure**:

```
1. Hook: Why this matters to YOU
2. Foundation: Core concept explained simply
3. Deep dive: Technical details with analogies
4. Application: How to use this in your projects
5. Callback: Reinforce the key insight
```

---

## Implementation Options

### Capture Tools

| Tool | Best For | Setup Complexity |
|------|----------|------------------|
| **WhatsApp** | Mobile-first, always available | Low |
| **Telegram** | Bots, saved messages, search | Low |
| **Discord** | Personal server with channels | Medium |
| **Obsidian** | Integrated with structure phase | Low |
| **Apple Notes** | iOS ecosystem, voice capture | Low |
| **CLI Script** | Terminal-native workflows | Medium |
| **Voice Memo → Whisper** | Hands-free capture | Medium |
| **Raycast/Alfred** | macOS quick capture | Low |

### Structure Tools

| Tool | Strengths | Export Options |
|------|-----------|----------------|
| **Obsidian** | Local-first, graph view, plugins | Markdown |
| **Notion** | Databases, views, collaboration | Markdown, CSV |
| **Logseq** | Outliner, bidirectional links | Markdown, JSON |
| **VS Code** | Developer-friendly, git native | Markdown |
| **GitHub** | Version control, collaboration | Markdown |
| **Anki** | Spaced repetition built-in | APKG |

### Audio Generation Tools

| Tool | Cost | Quality | Local/Cloud |
|------|------|---------|-------------|
| **Kokoro** | Free | Good | Local |
| **Edge TTS** | Free | Good | Cloud |
| **OpenAI TTS** | $0.015/1K chars | Great | Cloud |
| **ElevenLabs** | $0.24/1K chars | Excellent | Cloud |
| **Coqui TTS** | Free | Good | Local |
| **Bark** | Free | Great | Local (GPU) |

---

## Workflow Examples

### Workflow 1: CLI-Native (Developer)

```bash
# Capture: Quick terminal command
casa capture "TCP three-way handshake is like..."

# Structure: Generate card from capture
casa structure --source captures/2024-01-15.md

# Absorb: Generate audio from structured cards
casa audio --input cards/networking.md --voice narrator
```

**Tools**: Custom bash scripts, Obsidian, Kokoro TTS

**Best for**: Developers, terminal power users

---

### Workflow 2: Obsidian-Centric

```
Capture: Obsidian Quick Add plugin → Daily note
Structure: Templates plugin → Card format
Review: Dataview plugin → Query by tags
Absorb: Export → TTS script
```

**Plugins Required**:
- Quick Add (capture hotkey)
- Templates (card generation)
- Dataview (queries and views)

**Best for**: Knowledge workers, writers, researchers

---

### Workflow 3: Mobile-First

```
Capture: WhatsApp message to self/bot
Structure: Weekly review → Notion database
Absorb: Podcast app with generated episodes
```

**Tools**: WhatsApp/Telegram, Notion, ElevenLabs

**Best for**: Commuters, mobile learners, busy professionals

---

### Workflow 4: Automation-Heavy (n8n/Zapier)

```yaml
Trigger: New message in capture channel
Actions:
  1. Parse message with AI (extract term, analogy, tags)
  2. Create structured card in Notion/Obsidian
  3. Add to audio generation queue
  4. Weekly: Batch generate audio episodes
  5. Upload to private podcast feed
```

**Tools**: n8n/Zapier, Claude API, Notion API, TTS API

**Best for**: System builders, automation enthusiasts

---

### Workflow 5: Voice-First

```
Capture: Voice memo while walking/driving
Transcribe: Whisper (local) or cloud API
Structure: AI-assisted formatting
Absorb: Generated audio for review
```

**Tools**: Voice Memos app, Whisper, Claude, TTS

**Best for**: Auditory learners, hands-free contexts

---

## Templates

### Capture Template

```markdown
📖 TERM:

💡 ELI5:


🔗 MY PROJECTS:
•
•
•

⌨️ TRY NOW:


🏷️ Tags:
```

### Card Template

```markdown
### Card N - [Term]
Q:
A:

**ELI5:**

**Commands/Code:**
```
[code block]
```

**Use Cases:**
-
-
-

Tags:
Source:
```

### Audio Script Template

```markdown
# Episode: [Topic]

## Hook (30 seconds)
[Why should the listener care? Personal relevance.]

## Foundation (2-3 minutes)
[Core concept, simple explanation, first analogy.]

## Deep Dive (5-10 minutes)
[Technical details, multiple examples, more analogies.]

## Application (3-5 minutes)
[How to use this. Specific to listener's projects.]

## Recap (1 minute)
[Key takeaways, callback to hook.]
```

---

## Tool Recommendations

### Minimum Viable Setup (Free)

| Phase | Tool | Cost |
|-------|------|------|
| Capture | Telegram Saved Messages | Free |
| Structure | Obsidian | Free |
| Absorb | Kokoro TTS | Free |

### Recommended Setup (Low Cost)

| Phase | Tool | Cost |
|-------|------|------|
| Capture | Obsidian + Quick Add | Free |
| Structure | Obsidian + Dataview | Free |
| Absorb | OpenAI TTS | ~$5/month |

### Power User Setup

| Phase | Tool | Cost |
|-------|------|------|
| Capture | Custom CLI + Raycast | Free |
| Structure | Obsidian + Git sync | Free |
| AI Assist | Claude API | ~$20/month |
| Absorb | ElevenLabs | ~$22/month |
| Automation | n8n self-hosted | Free |

---

## Configuration

### config.yaml

```yaml
# CASA Learning System Configuration

# Your personal anchor sources
anchors:
  interests:
    - "Dragon Ball Z"
    - "Kingdom Hearts"
    - "roguelike games"
    - "90s movies"

  projects:
    - name: "Personal Portfolio"
      context: "Next.js web app"
    - name: "Home Lab"
      context: "Proxmox server setup"
    - name: "Side Project"
      context: "SaaS MVP"

  career:
    current: "Software Developer"
    target: "Senior Engineer at FAANG"
    skills_focus:
      - "System Design"
      - "Distributed Systems"

# Capture configuration
capture:
  tool: "obsidian"  # obsidian | telegram | whatsapp | cli
  location: "00-Inbox/"
  hotkey: "Cmd+Shift+C"

# Structure configuration
structure:
  tool: "obsidian"
  location: "knowledge-base/"
  card_format: "standard"  # standard | anki | notion

# Audio configuration
audio:
  tool: "kokoro"  # kokoro | elevenlabs | openai | edge
  voice: "af_sky"  # tool-specific voice ID
  output_dir: "audio/"
  episode_length: "15min"  # 5min | 15min | 30min

# Review schedule (optional)
review:
  daily_new_cards: 5
  weekly_review_day: "Sunday"
```

---

## AI Integration

CASA is designed to work with AI assistants. Fill out `config.yaml` once, and AI personalizes every learning interaction.

### Supported Tools

| Tool | Setup | Files Used |
|------|-------|-----------|
| **Claude Code** | Automatic | `CLAUDE.md` + `config.yaml` |
| **Cursor** | Automatic | `.cursorrules` + `config.yaml` |
| **ChatGPT** | Custom GPT | `ai/chatgpt-custom-gpt.md` |
| **Claude.ai** | Project files | `CLAUDE.md` + `config.yaml` |
| **Any AI** | Paste prompt | `ai/SYSTEM_PROMPT.md` |

### Quick Setup (Claude Code / Cursor)

```bash
# 1. Clone and enter
git clone https://github.com/yourusername/casa-learning.git
cd casa-learning

# 2. Fill out your profile
# Edit config.yaml with your interests, projects, career goal

# 3. Start learning (Claude Code)
claude
> explain kubernetes pods
> /capture what I just learned
```

### Commands (When Using AI)

| Command | What It Does |
|---------|--------------|
| `/learn [topic]` | Teach using your personal anchors |
| `/capture [topic]` | Create a CASA-formatted capture |
| `/card [topic]` | Generate a full knowledge card |
| `/review` | Quiz on recent captures |
| `/connect [topic]` | Map connections to your projects |

### How It Works

```yaml
# Your config.yaml
profile:
  interests: ["Dragon Ball Z", "cooking"]
  projects: [{name: "Home Lab", context: "Proxmox cluster"}]
  career:
    target: "Senior DevOps Engineer"
```

**Without CASA AI**: "TCP uses a three-way handshake like a phone call..."

**With CASA AI**: "TCP is like the power-up acknowledgment in Dragon Ball Z. Before Goku and Vegeta fight, they both power up and confirm they see each other's level. In your Home Lab, this is happening every time your VMs establish a connection..."

### Full AI Setup Guide

See [`ai/README.md`](ai/README.md) for:
- Detailed setup for each platform
- API integration examples (Python + Claude/OpenAI)
- n8n automation workflows
- Local LLM configuration

---

## The Science

### Why CASA Works

**1. Encoding Specificity** (Tulving & Thomson, 1973)
> Memory retrieval is most effective when the context at retrieval matches the context at encoding.

Personal analogies create unique, emotionally-charged encoding contexts that are easier to retrieve than generic examples.

**2. Elaborative Interrogation** (Pressley et al., 1987)
> Asking "why" and "how" questions during learning significantly improves retention.

The anchor phase forces elaborative processing: "How does this connect to my project? Why does this matter for my career?"

**3. Dual Coding Theory** (Paivio, 1971)
> Information encoded both visually and verbally creates stronger memory traces.

Structure (visual/text) + Absorb (audio) = redundant encoding pathways.

**4. Spacing Effect** (Ebbinghaus, 1885)
> Distributed practice over time beats massed practice.

The four phases naturally distribute exposure: immediate capture, same-day structuring, later audio listening, periodic review.

**5. Generation Effect** (Slamecka & Graf, 1978)
> Self-generated information is remembered better than passively received information.

Writing your own analogies and project connections requires generation, not just consumption.

---

## Directory Structure

```
casa-learning/
├── README.md                    # You are here
├── CLAUDE.md                    # Claude Code instructions
├── .cursorrules                 # Cursor AI rules
├── LICENSE
├── config.yaml                  # Your personal profile (edit this!)
├── config.example.yaml          # Example configuration
│
├── ai/                          # AI integration
│   ├── README.md                # Full AI setup guide
│   ├── SYSTEM_PROMPT.md         # Universal prompt for any AI
│   └── chatgpt-custom-gpt.md    # ChatGPT Custom GPT setup
│
├── docs/                        # Documentation
│   ├── getting-started.md       # 10-minute quick start
│   ├── philosophy.md            # The "why" behind CASA
│   └── research.md              # Cognitive science backing
│
├── scripts/                     # Automation scripts
│   ├── capture.py               # CLI capture tool
│   └── generate-audio.py        # Multi-engine TTS
│
├── templates/                   # CASA formats
│   ├── capture.md               # Quick capture template
│   ├── card.md                  # Structured card template
│   └── audio-script.md          # Narrative audio template
│
└── workflows/                   # Tool-specific guides
    ├── obsidian/README.md       # Obsidian setup + plugins
    ├── notion/README.md         # Notion databases + API
    ├── n8n-automation/README.md # Full automation pipeline
    └── mobile-first/README.md   # Telegram + voice capture
```

---

## Philosophy

CASA is built on a simple premise: **the goal isn't to collect knowledge—it's to become someone who knows.**

Most learning systems optimize for collection. More notes. More bookmarks. More saved articles. But collection without transformation is just hoarding.

CASA optimizes for **connection**:
- Connect new concepts to what you already know (your interests)
- Connect new skills to what you're building (your projects)
- Connect new capabilities to who you're becoming (your career)

### Core Beliefs

1. **Personal beats generic**: Your analogy using Dragon Ball Z will stick better than any textbook explanation.

2. **Active beats passive**: Writing your own explanation strengthens memory more than reading someone else's.

3. **Multi-modal beats single-channel**: Reading + hearing + doing = durable knowledge.

4. **Imperfect capture beats perfect organization**: A messy note that exists is infinitely more valuable than a perfect system you never use.

5. **Transformation is the goal**: You're not building a knowledge base. You're building a different version of yourself.

For the full philosophy, see [`docs/philosophy.md`](docs/philosophy.md).

For the cognitive science research backing CASA, see [`docs/research.md`](docs/research.md).

---

## Contributing

This system is intentionally minimal. Contributions should:

1. **Add workflow examples** for different tools/contexts
2. **Improve templates** based on real usage
3. **Share anchor libraries** (gaming terms, movie analogies, etc.)
4. **Build integrations** (scripts, plugins, automations)

Please don't add complexity for its own sake. The power is in the simplicity.

---

## License

MIT License - Use it, modify it, share it.

---

## Acknowledgments

This system emerged from real daily practice, not theory. It combines:
- Spaced repetition research
- Personal knowledge management (PKM) principles
- Multi-modal learning theory
- Practical friction reduction

Built for learners who are tired of forgetting what they learn.

---

*"The goal isn't to collect knowledge. It's to become someone who knows."*
