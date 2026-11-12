"""Reporting and daily summary."""

from datetime import datetime
from ..clients.claude import get_claude_client
from ..models import DailySummary, RevenueEvent, SalesLead


def generate_daily_summary(
    revenue_events: list,
    leads: list,
    pending_approvals: int = 0
) -> DailySummary:
    claude = get_claude_client()

    analysis = claude.analyze_revenue([e.model_dump() for e in revenue_events])
    recommendation = claude.recommend_next_content(analysis)

    high_value = [l for l in leads if l.value_score >= 0.7]

    summary = DailySummary(
        date=datetime.utcnow(),
        revenue_total=analysis.get("total", 0),
        conversions=len([e for e in revenue_events if e.amount > 0]),
        content_recommendations=[recommendation],
        pending_approvals=pending_approvals,
        high_value_leads=high_value
    )

    print("\n=== Daily Summary ===")
    print(f"Revenue: ${summary.revenue_total:,.2f}")
    print(f"Conversions: {summary.conversions}")
    print(f"Recommendation: {recommendation}")
    print(f"High-value leads waiting: {len(high_value)}")

    return summary
