#!/usr/bin/env python3
"""Full end-to-end demo of CreatorStudioAI (uses mocks)."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from creator_studio.orchestrator import CreatorStudioOrchestrator
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    console.print(Panel.fit("[bold cyan]CreatorStudioAI[/bold cyan]\nOne-person AI Creator Studio Demo", border_style="cyan"))

    studio = CreatorStudioOrchestrator()

    # 1. Voice Module
    raw = """
    I built this entire system so I can create content without employees.
    Just talk for two minutes, Claude writes the script, ElevenLabs does my voice.
    Photos become video, it gets dubbed into 10 languages, and Metricool posts everything.
    My AI sales line handles the inquiries so I only talk to serious people.
    Every morning I get a one-page summary of what actually made money.
    """
    content = studio.create_content_from_voice(raw.strip(), title="How I Run a Creator Studio With Zero Employees")
    console.print(f"\n[green]Content created:[/green] {content.id}")

    # Simulate approval
    studio.approve(content.id)

    # 2. Video Module
    images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
    content = studio.add_video(content.id, images)
    studio.approve(content.id)

    # 3. Posting
    studio.post(content.id)

    # 4. Sales Line
    studio.handle_sales_inquiry("I want to buy your course on building AI systems")
    studio.handle_sales_inquiry("Interested in a brand deal for my company")

    # 5. Record some revenue
    studio.record_sale(497.0, content.id, "course_sale")
    studio.record_sale(1500.0, None, "coaching")

    # 6. Daily Summary
    summary = studio.daily_summary()

    console.print("\n[bold green]Demo complete![/bold green]")
    console.print("All modules executed with human approval gates.")
    console.print("Check the output/ directory for generated assets (mock).")

if __name__ == "__main__":
    main()
