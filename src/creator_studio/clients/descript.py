"""Descript client for editing, captioning, and sync."""

import os
from abc import ABC, abstractmethod


class DescriptClient(ABC):
    @abstractmethod
    def edit_and_caption(self, video_paths: list, voice_path: str) -> str:
        pass


class MockDescriptClient(DescriptClient):
    def edit_and_caption(self, video_paths: list, voice_path: str) -> str:
        final = f"output/final_edit_{hash(voice_path) % 10000}.mp4"
        print(f"[Mock Descript] Cut {len(video_paths)} clips to voice + captions → {final}")
        return final


class RealDescriptClient(DescriptClient):
    def __init__(self):
        self.api_key = os.getenv("DESCRIPT_API_KEY")

    def edit_and_caption(self, video_paths: list, voice_path: str) -> str:
        if not self.api_key:
            return MockDescriptClient().edit_and_caption(video_paths, voice_path)
        return MockDescriptClient().edit_and_caption(video_paths, voice_path)


def get_descript_client() -> DescriptClient:
    return RealDescriptClient() if os.getenv("DESCRIPT_API_KEY") else MockDescriptClient()
