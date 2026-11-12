"""Posting module."""

from ..clients.metricool import get_metricool_client
from ..models import ContentPiece, ApprovalStatus


def schedule_content(content: ContentPiece, platforms: list = None) -> dict:
    if platforms is None:
        platforms = ["youtube", "tiktok", "instagram", "facebook"]

    metricool = get_metricool_client()
    results = {}

    print("\n=== Posting Module ===")
    for lang, path in content.dubbed_versions.items():
        print(f"Scheduling {lang} version...")
        results[lang] = metricool.schedule_post(path, platforms, language=lang)

    content.status = ApprovalStatus.APPROVED
    print("All versions scheduled.")
    return results
