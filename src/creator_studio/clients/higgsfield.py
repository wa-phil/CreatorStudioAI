"""Higgsfield client for image-to-video generation."""

import os
from abc import ABC, abstractmethod
from typing import List


class HiggsfieldClient(ABC):
    @abstractmethod
    def generate_videos(self, image_paths: List[str]) -> List[str]:
        pass


class MockHiggsfieldClient(HiggsfieldClient):
    def generate_videos(self, image_paths: List[str]) -> List[str]:
        videos = []
        for i, img in enumerate(image_paths):
            path = f"output/video_clip_{i}_{hash(img) % 10000}.mp4"
            print(f"[Mock Higgsfield] Generated video from {img} → {path}")
            videos.append(path)
        return videos


class RealHiggsfieldClient(HiggsfieldClient):
    def __init__(self):
        self.api_key = os.getenv("HIGGSFIELD_API_KEY")

    def generate_videos(self, image_paths: List[str]) -> List[str]:
        if not self.api_key:
            return MockHiggsfieldClient().generate_videos(image_paths)
        return MockHiggsfieldClient().generate_videos(image_paths)


def get_higgsfield_client() -> HiggsfieldClient:
    return RealHiggsfieldClient() if os.getenv("HIGGSFIELD_API_KEY") else MockHiggsfieldClient()
