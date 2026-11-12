"""AI Sales Line module."""

from ..clients.claude import get_claude_client
from ..models import SalesLead


def handle_inquiry(inquiry: str) -> SalesLead:
    claude = get_claude_client()
    lead = SalesLead(id=f"lead_{hash(inquiry) % 10000}", inquiry=inquiry)

    print("\n=== AI Sales Line ===")
    print(f"Incoming inquiry: {inquiry[:80]}...")

    # In production this would be a full conversation agent
    lead.ai_response = (
        "Hi! I'm an AI assistant for the creator. "
        "I can answer questions about the course, coaching, or brand deals. "
        "What are you looking for?"
    )
    lead.qualified = "course" in inquiry.lower() or "coaching" in inquiry.lower() or "brand" in inquiry.lower()
    lead.value_score = 0.8 if lead.qualified else 0.2
    lead.routed_to = "checkout" if "buy" in inquiry.lower() else "call" if lead.value_score > 0.7 else "human"

    print(f"Qualified: {lead.qualified} | Value: {lead.value_score:.1f} | Routed to: {lead.routed_to}")
    return lead
