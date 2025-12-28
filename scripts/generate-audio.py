#!/usr/bin/env python3
"""
CASA Learning System - Audio Generator

Converts structured markdown cards into narrative audio using various TTS engines.

Usage:
    python generate-audio.py input.md --engine kokoro --voice am_adam
    python generate-audio.py input.md --engine openai --voice nova
    python generate-audio.py input.md --engine edge --voice en-US-GuyNeural

Supported Engines:
    - kokoro: Free, local, good quality (requires: pip install kokoro-onnx)
    - edge: Free, cloud, good quality (requires: pip install edge-tts)
    - openai: Paid, cloud, great quality (requires: pip install openai)
    - elevenlabs: Paid, cloud, excellent quality (requires: pip install elevenlabs)
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Optional


def parse_markdown_to_script(md_path: str) -> str:
    """Convert structured cards to narrative script."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract cards
    cards = re.findall(r'### Card \d+ - (.+?)\n(.+?)(?=### Card|\Z)', content, re.DOTALL)

    if not cards:
        # Maybe it's already a script
        return content

    # Build narrative
    script_parts = []

    for title, body in cards:
        # Extract Q&A
        q_match = re.search(r'\*\*?Q\*?\*?:\s*(.+)', body)
        a_match = re.search(r'\*\*?A\*?\*?:\s*(.+)', body)
        eli5_match = re.search(r'\*\*ELI5:\*\*\s*(.+?)(?=\*\*|\Z)', body, re.DOTALL)

        question = q_match.group(1).strip() if q_match else ""
        answer = a_match.group(1).strip() if a_match else ""
        eli5 = eli5_match.group(1).strip() if eli5_match else ""

        # Build narrative section
        section = f"""
Let's talk about {title}.

{question}

{answer}

{eli5}

"""
        script_parts.append(section)

    return "\n".join(script_parts)


def generate_with_kokoro(text: str, output_path: str, voice: str = "am_adam"):
    """Generate audio using Kokoro (free, local)."""
    try:
        from kokoro_onnx import Kokoro
        import soundfile as sf
    except ImportError:
        print("Install kokoro: pip install kokoro-onnx soundfile")
        sys.exit(1)

    print(f"Generating with Kokoro (voice: {voice})...")

    kokoro = Kokoro("kokoro-v0_19.onnx", "voices.bin")
    samples, sample_rate = kokoro.create(text, voice=voice, speed=1.0)

    sf.write(output_path, samples, sample_rate)
    print(f"Saved to: {output_path}")


def generate_with_edge(text: str, output_path: str, voice: str = "en-US-GuyNeural"):
    """Generate audio using Edge TTS (free, cloud)."""
    try:
        import asyncio
        import edge_tts
    except ImportError:
        print("Install edge-tts: pip install edge-tts")
        sys.exit(1)

    print(f"Generating with Edge TTS (voice: {voice})...")

    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)

    asyncio.run(_generate())
    print(f"Saved to: {output_path}")


def generate_with_openai(text: str, output_path: str, voice: str = "nova"):
    """Generate audio using OpenAI TTS (paid, cloud)."""
    try:
        from openai import OpenAI
    except ImportError:
        print("Install openai: pip install openai")
        sys.exit(1)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable")
        sys.exit(1)

    print(f"Generating with OpenAI (voice: {voice})...")

    client = OpenAI(api_key=api_key)

    # OpenAI has a 4096 character limit, chunk if needed
    max_chars = 4000
    chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

    audio_segments = []
    for i, chunk in enumerate(chunks):
        print(f"  Processing chunk {i+1}/{len(chunks)}...")
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=chunk
        )
        audio_segments.append(response.content)

    # Combine chunks
    with open(output_path, 'wb') as f:
        for segment in audio_segments:
            f.write(segment)

    print(f"Saved to: {output_path}")


def generate_with_elevenlabs(text: str, output_path: str, voice: str = "pqHfZKP75CvOlQylNhV4"):
    """Generate audio using ElevenLabs (paid, cloud)."""
    try:
        from elevenlabs import generate, save, set_api_key
    except ImportError:
        print("Install elevenlabs: pip install elevenlabs")
        sys.exit(1)

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("Set ELEVENLABS_API_KEY environment variable")
        sys.exit(1)

    print(f"Generating with ElevenLabs (voice: {voice})...")

    set_api_key(api_key)
    audio = generate(text=text, voice=voice, model="eleven_monolingual_v1")
    save(audio, output_path)

    print(f"Saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="CASA Audio Generator")
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument("--engine", choices=["kokoro", "edge", "openai", "elevenlabs"],
                        default="kokoro", help="TTS engine to use")
    parser.add_argument("--voice", help="Voice ID (engine-specific)")
    parser.add_argument("--output", "-o", help="Output file path")

    args = parser.parse_args()

    # Validate input
    if not os.path.exists(args.input):
        print(f"File not found: {args.input}")
        sys.exit(1)

    # Parse to script
    script = parse_markdown_to_script(args.input)

    # Set output path
    if args.output:
        output_path = args.output
    else:
        input_stem = Path(args.input).stem
        output_path = f"{input_stem}.mp3"

    # Set default voices
    default_voices = {
        "kokoro": "am_adam",
        "edge": "en-US-GuyNeural",
        "openai": "nova",
        "elevenlabs": "pqHfZKP75CvOlQylNhV4"
    }
    voice = args.voice or default_voices[args.engine]

    # Generate
    generators = {
        "kokoro": generate_with_kokoro,
        "edge": generate_with_edge,
        "openai": generate_with_openai,
        "elevenlabs": generate_with_elevenlabs
    }

    generators[args.engine](script, output_path, voice)

    print("Done!")


if __name__ == "__main__":
    main()
