#!/usr/bin/env python3
"""Generate a daily one-page summary."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from creator_studio.orchestrator import CreatorStudioOrchestrator
from creator_studio.models import RevenueEvent, SalesLead
from datetime import datetime

def main():
    studio = CreatorStudioOrchestrator()

    # Sample data
    studio.record_sale(1240.0, "vid001", "course_sale")
    studio.record_sale(750.0, "vid002", "coaching")
    studio.leads.append(SalesLead(
        id="lead1",
        inquiry="Brand deal for AI tools",
        qualified=True,
        value_score=0.9,
        routed_to="call"
    ))

    summary = studio.daily_summary()

    print("\n" + "="*50)
    print(f"# CreatorStudioAI Daily Summary — {summary.date.strftime('%Y-%m-%d')}")
    print("="*50)
    print(f"\n## Revenue")
    print(f"- Total: ${summary.revenue_total:,.2f}")
    print(f"- Conversions: {summary.conversions}")
    print(f"\n## Recommendation")
    print(f"- {summary.content_recommendations[0]}")
    print(f"\n## Pending Approvals: {summary.pending_approvals}")
    print(f"## High-Value Leads: {len(summary.high_value_leads)}")

if __name__ == "__main__":
    main()
