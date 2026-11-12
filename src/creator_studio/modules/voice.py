"""Voice module: raw input → script → cloned voice."""

from ..clients.claude import get_claude_client
from ..clients.elevenlabs import get_elevenlabs_client
from ..models import ContentPiece, ApprovalStatus


def process_voice(raw_input: str, content: ContentPiece) -> ContentPiece:
    claude = get_claude_client()
    eleven = get_elevenlabs_client()

    print("\n=== Voice Module ===")
    print("Generating full script from raw input...")
    content.script = claude.generate_script(raw_input)
    print(f"Script ready ({len(content.script)} chars)")

    print("Synthesizing in your cloned voice...")
    content.voice_audio_path = eleven.synthesize(content.script)
    content.status = ApprovalStatus.PENDING
    print("Voice audio ready for approval.")

    return content
