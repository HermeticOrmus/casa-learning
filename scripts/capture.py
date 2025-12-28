#!/usr/bin/env python3
"""
CASA Learning System - Quick Capture

Quickly capture knowledge to your inbox for later processing.

Usage:
    python capture.py "TCP handshake is like a DBZ power-up exchange"
    python capture.py --interactive
    python capture.py --template

Environment:
    CASA_INBOX: Path to inbox folder (default: ./inbox)
"""

import argparse
import os
from datetime import datetime
from pathlib import Path


CAPTURE_TEMPLATE = """📖 **TERM**: {term}

💡 **ELI5**:
{eli5}

🔗 **MY PROJECTS**:
• {project1}
• {project2}
• {project3}

⌨️ **TRY NOW**:
```
{action}
```

🏷️ **Tags**: {tags}

📚 **Source**: {source}

---
*Captured: {timestamp}*
"""


def get_inbox_path() -> Path:
    """Get inbox path from environment or default."""
    inbox = os.getenv("CASA_INBOX", "./inbox")
    path = Path(inbox)
    path.mkdir(parents=True, exist_ok=True)
    return path


def quick_capture(text: str) -> str:
    """Quick one-liner capture."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".md"

    content = f"""📖 **QUICK CAPTURE**

{text}

---
*Captured: {timestamp}*
*Status: Unprocessed*
"""

    inbox = get_inbox_path()
    filepath = inbox / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return str(filepath)


def interactive_capture() -> str:
    """Guided interactive capture."""
    print("\n=== CASA Quick Capture ===\n")

    term = input("📖 Term/Concept: ").strip()
    eli5 = input("💡 ELI5 (your analogy): ").strip()

    print("\n🔗 Project connections (press Enter to skip):")
    project1 = input("   Project 1: ").strip() or "[connection 1]"
    project2 = input("   Project 2: ").strip() or "[connection 2]"
    project3 = input("   Project 3: ").strip() or "[connection 3]"

    action = input("\n⌨️ Try now (command/action): ").strip() or "[action]"
    tags = input("🏷️ Tags (comma-separated): ").strip() or "unprocessed"
    source = input("📚 Source: ").strip() or "manual capture"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    content = CAPTURE_TEMPLATE.format(
        term=term,
        eli5=eli5,
        project1=project1,
        project2=project2,
        project3=project3,
        action=action,
        tags=tags,
        source=source,
        timestamp=timestamp
    )

    # Generate filename from term
    safe_term = "".join(c if c.isalnum() else "_" for c in term.lower())[:30]
    filename = f"{datetime.now().strftime('%Y%m%d')}_{safe_term}.md"

    inbox = get_inbox_path()
    filepath = inbox / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Saved to: {filepath}")
    return str(filepath)


def show_template():
    """Display the capture template."""
    print("\n=== CASA Capture Template ===\n")
    print(CAPTURE_TEMPLATE.format(
        term="[TERM]",
        eli5="[Your analogy using YOUR interests]",
        project1="[How this applies to Project 1]",
        project2="[How this applies to Project 2]",
        project3="[How this applies to Career Goal]",
        action="[command or action]",
        tags="#topic #type",
        source="[Course - Section]",
        timestamp="[auto-generated]"
    ))


def list_unprocessed():
    """List unprocessed captures."""
    inbox = get_inbox_path()
    files = sorted(inbox.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)

    if not files:
        print("No captures in inbox.")
        return

    print(f"\n=== Inbox ({len(files)} captures) ===\n")
    for f in files[:10]:  # Show last 10
        # Read first line to get term
        with open(f, 'r', encoding='utf-8') as file:
            first_lines = file.read(200)
            term_match = first_lines.split('\n')[0] if first_lines else "Unknown"

        mtime = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        print(f"  {mtime} | {f.name}")

    if len(files) > 10:
        print(f"\n  ... and {len(files) - 10} more")


def main():
    parser = argparse.ArgumentParser(description="CASA Quick Capture")
    parser.add_argument("text", nargs="?", help="Quick capture text")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive guided capture")
    parser.add_argument("--template", "-t", action="store_true",
                        help="Show capture template")
    parser.add_argument("--list", "-l", action="store_true",
                        help="List unprocessed captures")

    args = parser.parse_args()

    if args.template:
        show_template()
    elif args.list:
        list_unprocessed()
    elif args.interactive:
        interactive_capture()
    elif args.text:
        filepath = quick_capture(args.text)
        print(f"✅ Captured to: {filepath}")
    else:
        # Default to interactive
        interactive_capture()


if __name__ == "__main__":
    main()
