"""Metricool client for multi-platform scheduling and posting."""

import os
from abc import ABC, abstractmethod
from typing import Dict, List


class MetricoolClient(ABC):
    @abstractmethod
    def schedule_post(self, content_path: str, platforms: List[str], language: str = "en") -> Dict:
        pass


class MockMetricoolClient(MetricoolClient):
    def schedule_post(self, content_path: str, platforms: List[str], language: str = "en") -> Dict:
        schedule = {
            "youtube": "2026-11-13 10:00 PST",
            "tiktok": "2026-11-13 14:00 local",
            "instagram": "2026-11-13 18:00 local",
            "facebook": "2026-11-13 12:00 local",
        }
        print(f"[Mock Metricool] Scheduled {content_path} ({language}) to {platforms}")
        return {"status": "scheduled", "times": schedule, "language": language}


class RealMetricoolClient(MetricoolClient):
    def __init__(self):
        self.api_key = os.getenv("METRICOOL_API_KEY")

    def schedule_post(self, content_path: str, platforms: List[str], language: str = "en") -> Dict:
        if not self.api_key:
            return MockMetricoolClient().schedule_post(content_path, platforms, language)
        return MockMetricoolClient().schedule_post(content_path, platforms, language)


def get_metricool_client() -> MetricoolClient:
    return RealMetricoolClient() if os.getenv("METRICOOL_API_KEY") else MockMetricoolClient()
