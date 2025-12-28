# CASA Mobile-First Workflow

Learn on the go. Capture anywhere. Never lose an insight.

---

## Why Mobile-First?

Learning doesn't happen at a desk. It happens:
- During commutes
- In waiting rooms
- Between meetings
- While walking
- Late at night in bed

Your capture system must be where you are.

---

## The Stack

| Phase | Tool | Why |
|-------|------|-----|
| Capture | Telegram Saved Messages | Instant, searchable, synced |
| Process | Weekly desktop session | Focused structuring time |
| Structure | Obsidian/Notion | Your choice |
| Absorb | Podcast app | Background listening |

---

## Setup

### 1. Telegram Saved Messages

Telegram's "Saved Messages" is a private chat with yourself that syncs across all devices.

**Setup**:
1. Open Telegram
2. Search "Saved Messages" or tap your profile → Saved Messages
3. Pin it to top of chat list
4. Add to home screen (iOS: Share → Add to Home Screen)

**Why Telegram over WhatsApp**:
- Better search
- Larger file support
- Desktop app that doesn't require phone
- Bot API for automation later

### 2. Pin the Capture Template

Send this to Saved Messages and pin it:

```
📖 TERM:

💡 ELI5:

🔗 PROJECTS:
•
•

⌨️ TRY:

🏷️ Tags:
📚 Source:
```

### 3. Create Capture Shortcut (iOS)

**iOS Shortcut**:
1. Open Shortcuts app
2. Create new shortcut
3. Add actions:
   - Ask for Input (Term)
   - Ask for Input (ELI5)
   - Text: Format the capture template
   - Send via Telegram (or copy to clipboard)
4. Add to Home Screen

**Android Alternative**:
Use Tasker or Macrodroid with similar flow.

### 4. Voice Capture Option

When typing isn't possible:

1. Open Voice Memos (iOS) or Recorder (Android)
2. Speak your capture naturally
3. Later: Transcribe with Whisper and process

```bash
# Transcribe voice memo
whisper audio.m4a --model base --output_format txt
```

---

## Daily Workflow

### During the Day

**When you learn something:**
1. Open Telegram Saved Messages (2 seconds)
2. Copy pinned template (2 seconds)
3. Fill in Term and ELI5 (20 seconds)
4. Send (1 second)

**Total: 25 seconds**

Don't overthink. Capture the essence. Move on.

### Commute Time

**Morning commute**:
- Listen to previous week's audio

**Evening commute**:
- Review the day's captures (just read, don't process)

### Weekly Processing (Desktop)

**Sunday, 30 minutes**:
1. Open Telegram desktop app
2. Search through week's captures
3. For each capture:
   - Create structured card in Obsidian/Notion
   - Expand with code examples
   - Add connections
4. Mark processed captures with ✅

---

## Audio Pipeline

### Generate Weekly

```bash
# Export week's cards
python export-cards.py --week-of 2024-01-15 > this-week.md

# Generate audio
python generate-audio.py this-week.md \
  --engine edge \
  --voice en-US-GuyNeural \
  --output podcast/week-03.mp3
```

### Podcast Feed

Create a simple podcast feed for your audio:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>My Learning Feed</title>
    <description>Weekly knowledge reviews</description>
    <item>
      <title>Week 3: Networking Fundamentals</title>
      <enclosure url="https://your-host.com/week-03.mp3" type="audio/mpeg"/>
      <pubDate>Sun, 21 Jan 2024 09:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>
```

Host on GitHub Pages, Netlify, or any static host.

Subscribe in your podcast app for automatic delivery.

---

## Tools Comparison

### Capture Apps

| App | Pros | Cons |
|-----|------|------|
| **Telegram** | Fast, synced, searchable, bots | Requires account |
| **Apple Notes** | Native, quick capture widget | Apple ecosystem only |
| **Google Keep** | Cross-platform, voice notes | Limited formatting |
| **Draft** | iOS, fast, actions | No Android |
| **Obsidian Mobile** | Direct to vault | Slower to open |

### Voice Transcription

| Tool | Pros | Cons |
|------|------|------|
| **Whisper (local)** | Free, private, accurate | Requires setup |
| **Whisper API** | Easy, accurate | $0.006/minute |
| **iOS Dictation** | Built-in, real-time | Less accurate |
| **Otter.ai** | Great UI, summaries | Subscription |

### Podcast Apps

| App | Pros | Cons |
|-----|------|------|
| **Pocket Casts** | Custom RSS, cross-platform | Paid |
| **Overcast** | Smart speed, iOS | iOS only |
| **AntennaPod** | Open source, Android | Android only |
| **Apple Podcasts** | Built-in | Limited custom feeds |

---

## Offline Mode

When you don't have internet:

### Capture
- Use Apple Notes or any offline-first app
- Transfer to Telegram when back online

### Listen
- Download audio episodes in advance
- Pocket Casts/Overcast have download features

### Review
- Use Obsidian with local vault
- Syncs when back online

---

## Quick Capture Variants

### Micro Capture (10 seconds)
Just the term and one-line ELI5:
```
📖 TCP RST = "hang up the phone immediately"
```

### Standard Capture (30 seconds)
Term, ELI5, one project connection:
```
📖 TCP RST
💡 Hanging up phone mid-sentence
🔗 Debug why my API connections drop
```

### Full Capture (60 seconds)
Complete template when you have time.

**All are valid.** Don't let perfect be the enemy of captured.

---

## Tips

### Batch Similar Captures
Learning a course? Send multiple captures back-to-back:
```
📖 Term 1...

📖 Term 2...

📖 Term 3...
```

### Use Voice When Moving
Walking or driving? Voice memo now, transcribe later.

### Review During Dead Time
Waiting for coffee? Open Telegram, read recent captures.

### Make It a Habit
Same trigger, same response:
- "I should remember this" → Open Telegram
- Not "I'll write this down later"

### Weekly Ritual
Same time every week. Process captures. Generate audio. Maintain the system.

---

## Minimal Viable Mobile

If all the tools feel like too much, start here:

1. **Text yourself** (any messaging app)
2. **Screenshot it** if you're lazy
3. **Voice note** if your hands are busy
4. **Weekly cleanup** into any notes app

The format matters less than the habit.

---

*The best capture system is the one you actually use.*
