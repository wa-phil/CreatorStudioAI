"""Main orchestrator — Claude Code style workflow manager."""

import uuid
from typing import List, Optional
from .models import ContentPiece, ApprovalStatus, SalesLead, RevenueEvent
from .modules.voice import process_voice
from .modules.video import process_video
from .modules.sales import handle_inquiry
from .modules.posting import schedule_content
from .modules.reporting import generate_daily_summary


class CreatorStudioOrchestrator:
    def __init__(self):
        self.content_pieces: List[ContentPiece] = []
        self.leads: List[SalesLead] = []
        self.revenue_events: List[RevenueEvent] = []
        self.languages = ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "zh", "ar"]

    def create_content_from_voice(self, raw_input: str, title: str = "New Video") -> ContentPiece:
        content = ContentPiece(
            id=str(uuid.uuid4())[:8],
            title=title,
            raw_input=raw_input
        )
        content = process_voice(raw_input, content)
        self.content_pieces.append(content)
        return content

    def add_video(self, content_id: str, image_paths: List[str]) -> Optional[ContentPiece]:
        content = self._get_content(content_id)
        if not content or content.status != ApprovalStatus.APPROVED:
            print("Voice must be approved before video generation.")
            return None
        return process_video(content, image_paths, self.languages)

    def approve(self, content_id: str) -> bool:
        content = self._get_content(content_id)
        if content:
            content.status = ApprovalStatus.APPROVED
            print(f"Approved content {content_id}")
            return True
        return False

    def post(self, content_id: str) -> dict:
        content = self._get_content(content_id)
        if not content or content.status != ApprovalStatus.APPROVED:
            print("Content must be fully approved before posting.")
            return {}
        return schedule_content(content)

    def handle_sales_inquiry(self, inquiry: str) -> SalesLead:
        lead = handle_inquiry(inquiry)
        self.leads.append(lead)
        return lead

    def record_sale(self, amount: float, content_id: Optional[str] = None, type_: str = "course_sale"):
        event = RevenueEvent(
            id=str(uuid.uuid4())[:8],
            type=type_,
            amount=amount,
            content_id=content_id
        )
        self.revenue_events.append(event)
        return event

    def daily_summary(self):
        pending = len([c for c in self.content_pieces if c.status == ApprovalStatus.PENDING])
        return generate_daily_summary(self.revenue_events, self.leads, pending)

    def _get_content(self, content_id: str) -> Optional[ContentPiece]:
        for c in self.content_pieces:
            if c.id == content_id:
                return c
        return None
