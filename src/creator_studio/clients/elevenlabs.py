"""ElevenLabs client for voice cloning and multi-language dubbing."""

import os
from abc import ABC, abstractmethod
from typing import Dict


class ElevenLabsClient(ABC):
    @abstractmethod
    def synthesize(self, text: str, voice_id: str = "cloned") -> str:
        """Return path to generated audio file."""
        pass

    @abstractmethod
    def dub(self, audio_path: str, languages: list) -> Dict[str, str]:
        """Return dict of language -> audio path."""
        pass


class MockElevenLabsClient(ElevenLabsClient):
    def synthesize(self, text: str, voice_id: str = "cloned") -> str:
        path = f"output/voice_{hash(text) % 10000}.mp3"
        # In real system this would call ElevenLabs and save the file
        print(f"[Mock ElevenLabs] Synthesized voice audio → {path}")
        return path

    def dub(self, audio_path: str, languages: list) -> Dict[str, str]:
        results = {}
        for lang in languages:
            path = f"output/dub_{lang}_{hash(audio_path) % 10000}.mp3"
            print(f"[Mock ElevenLabs] Dubbed to {lang} → {path}")
            results[lang] = path
        return results


class RealElevenLabsClient(ElevenLabsClient):
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")

    def synthesize(self, text: str, voice_id: str = "cloned") -> str:
        if not self.api_key:
            return MockElevenLabsClient().synthesize(text, voice_id)
        # Real call would go here
        return MockElevenLabsClient().synthesize(text, voice_id)

    def dub(self, audio_path: str, languages: list) -> Dict[str, str]:
        return MockElevenLabsClient().dub(audio_path, languages)


def get_elevenlabs_client() -> ElevenLabsClient:
    return RealElevenLabsClient() if os.getenv("ELEVENLABS_API_KEY") else MockElevenLabsClient()
