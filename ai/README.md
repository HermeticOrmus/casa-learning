# AI Integration Guide

CASA is designed to work with any AI assistant. This guide shows you how to integrate with popular tools.

---

## Quick Comparison

| Tool | Setup Time | Persistence | Best For |
|------|-----------|-------------|----------|
| **Claude Code** | 2 min | Automatic | Developers, terminal users |
| **Cursor** | 2 min | Automatic | Coding + learning |
| **ChatGPT Custom GPT** | 10 min | Permanent | Non-technical users |
| **Claude.ai Projects** | 5 min | Per-project | Research, long-form |
| **Any AI (manual)** | 1 min | Per-chat | Quick use |

---

## Claude Code (Recommended for Devs)

Claude Code automatically reads `CLAUDE.md` in your project root.

### Setup

1. Clone CASA repo (or copy to your project)
2. Fill out `config.yaml` with your profile
3. That's it—Claude Code reads both files automatically

### Usage

```bash
# In terminal with Claude Code
claude

# Then just ask
> explain kubernetes pods
> /capture kubernetes pods
> /card kubernetes networking
```

### What Happens

Claude Code reads:
- `CLAUDE.md` → Instructions on how to help you learn
- `config.yaml` → Your personal profile for analogies

Every explanation automatically uses your interests and connects to your projects.

---

## Cursor

Cursor reads `.cursorrules` in your project root.

### Setup

1. Copy `.cursorrules` to your project
2. Fill out `config.yaml`
3. Open project in Cursor

### Usage

Just chat with Cursor's AI:

```
explain docker networking in CASA style
```

Or use commands:

```
/learn docker volumes
/capture what I just learned about kubernetes
```

---

## ChatGPT Custom GPT

Create a permanent learning companion in ChatGPT.

### Setup

1. Go to ChatGPT → Explore GPTs → Create
2. Name: "CASA Learning Companion"
3. Description: "Personalized learning using the CASA system"
4. Instructions: Copy from `ai/SYSTEM_PROMPT.md` (the full prompt section)
5. Fill in YOUR profile in the instructions
6. Save and publish (private)

### Usage

Open your Custom GPT and chat normally. It remembers your profile across conversations.

### Advanced: With Actions

Add ability to save captures:

1. Create a simple webhook (n8n, Zapier, or custom)
2. Add as an Action in GPT settings
3. GPT can now save captures to your notes automatically

---

## Claude.ai Projects

Claude Projects maintain context across conversations.

### Setup

1. Create a new Project in Claude.ai
2. Upload `CLAUDE.md` and `config.yaml` to project files
3. Add project instructions:

```
You are my CASA learning companion. Read the uploaded CLAUDE.md for instructions and config.yaml for my profile. Always personalize explanations using my interests and connect to my projects.
```

### Usage

Every conversation in that project uses your learning profile.

---

## Gemini

Google Gemini doesn't have persistent instructions, but you can use Gems.

### Setup (Gemini Advanced with Gems)

1. Create a new Gem
2. Paste the system prompt from `ai/SYSTEM_PROMPT.md`
3. Fill in your profile
4. Save

### Setup (Basic)

Paste the system prompt at the start of each conversation.

---

## Local LLMs (Ollama, LM Studio)

For privacy-focused learning with local models.

### Ollama

Create a Modelfile:

```dockerfile
FROM llama3

SYSTEM """
You are my personalized learning companion using the CASA system.

MY PROFILE:
- Interests: [your interests]
- Projects: [your projects]
- Career goal: [your goal]

[rest of system prompt from SYSTEM_PROMPT.md]
"""
```

Then:

```bash
ollama create casa-learner -f Modelfile
ollama run casa-learner
```

### LM Studio

1. Go to Settings → System Prompt
2. Paste the CASA system prompt
3. Save as preset

---

## API Integration

For building your own tools using AI APIs.

### Python + Claude API

```python
import anthropic
import yaml

# Load config
with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Build system prompt from config
system_prompt = f"""
You are a CASA learning companion.

User's interests (for analogies): {config['profile']['interests']}
User's projects: {[p['name'] for p in config['profile']['projects']]}
User's career goal: {config['profile']['career']['target']}

Always use their interests for analogies, connect to their projects,
and frame relevance to their career. Follow CASA format for captures.
"""

client = anthropic.Anthropic()

def learn(topic):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {"role": "user", "content": f"Explain {topic} using my personal anchors"}
        ]
    )
    return response.content[0].text

# Usage
print(learn("TCP three-way handshake"))
```

### Python + OpenAI API

```python
from openai import OpenAI
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

system_prompt = f"""
You are a CASA learning companion.
User's interests: {config['profile']['interests']}
User's projects: {[p['name'] for p in config['profile']['projects']]}
Career goal: {config['profile']['career']['target']}
Always personalize using their interests and projects.
"""

client = OpenAI()

def learn(topic):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Explain {topic}"}
        ]
    )
    return response.choices[0].message.content

print(learn("Kubernetes pods"))
```

---

## n8n AI Workflow

Automate learning with n8n + AI.

### Capture Enhancement Flow

```
[Telegram Message]
    → [Parse Capture]
    → [Claude API: Enhance with config.yaml profile]
    → [Save to Notion/Obsidian]
    → [Reply with enhanced capture]
```

See `workflows/n8n-automation/` for full workflow JSON.

---

## Testing Your Setup

After configuring any AI, test with this prompt:

> "Explain how DNS works"

**Check for**:
- ✅ Uses analogy from YOUR interests (not generic)
- ✅ Mentions YOUR specific project
- ✅ Connects to YOUR career goal
- ✅ Includes practical action you can try

**If generic**, remind it:
> "Remember to use my specific interests for analogies and connect to my projects"

---

## Files Reference

| File | Purpose | Used By |
|------|---------|---------|
| `config.yaml` | Your personal profile | All tools |
| `CLAUDE.md` | Claude Code instructions | Claude Code |
| `.cursorrules` | Cursor AI rules | Cursor |
| `ai/SYSTEM_PROMPT.md` | Universal prompt | ChatGPT, Claude.ai, Gemini, etc. |

---

*The AI is a learning multiplier. The better your profile, the better your learning.*
