"""Video + dubbing module."""

from ..clients.higgsfield import get_higgsfield_client
from ..clients.descript import get_descript_client
from ..clients.elevenlabs import get_elevenlabs_client
from ..models import ContentPiece, ApprovalStatus


def process_video(content: ContentPiece, image_paths: list, languages: list) -> ContentPiece:
    higgs = get_higgsfield_client()
    descript = get_descript_client()
    eleven = get_elevenlabs_client()

    print("\n=== Video & Dubbing Module ===")
    print(f"Generating video clips from {len(image_paths)} photos...")
    content.video_paths = higgs.generate_videos(image_paths)

    print("Editing with Descript (sync + captions)...")
    final_video = descript.edit_and_caption(content.video_paths, content.voice_audio_path)

    print(f"Dubbing into {len(languages)} languages...")
    content.dubbed_versions = eleven.dub(content.voice_audio_path, languages)
    content.dubbed_versions["en"] = final_video  # original
    content.status = ApprovalStatus.PENDING
    print("Video versions ready for approval.")

    return content
