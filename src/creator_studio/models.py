"""Core data models for CreatorStudioAI."""

from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    REVISION_REQUESTED = "revision_requested"


class ContentPiece(BaseModel):
    id: str
    title: str
    raw_input: str
    script: Optional[str] = None
    voice_audio_path: Optional[str] = None
    video_paths: List[str] = Field(default_factory=list)
    dubbed_versions: Dict[str, str] = Field(default_factory=dict)  # lang -> path
    status: ApprovalStatus = ApprovalStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SalesLead(BaseModel):
    id: str
    inquiry: str
    qualified: bool = False
    value_score: float = 0.0
    routed_to: Optional[str] = None  # "checkout" | "call" | "human"
    ai_response: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RevenueEvent(BaseModel):
    id: str
    type: str  # "course_sale" | "coaching" | "brand_deal"
    amount: float
    currency: str = "USD"
    content_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class DailySummary(BaseModel):
    date: datetime
    revenue_total: float
    conversions: int
    content_recommendations: List[str]
    pending_approvals: int
    high_value_leads: List[SalesLead] = Field(default_factory=list)
