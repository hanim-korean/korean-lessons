#!/usr/bin/env python3
"""Validate repository-specific rules for the Hanim Korean content manifest."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "data" / "content-manifest.draft.json"
PUBLIC_RIGHTS = {"owned", "licensed"}


def duplicate_values(values: list[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def main() -> int:
    manifest_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_MANIFEST
    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}")
        return 1

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    items = data.get("items")
    if not isinstance(items, list):
        print("ERROR: top-level 'items' must be an array")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    ids = [item.get("id", "") for item in items]
    slugs = [item.get("slug", "") for item in items]

    for value in duplicate_values(ids):
        errors.append(f"duplicate id: {value}")
    for value in duplicate_values(slugs):
        errors.append(f"duplicate slug: {value}")

    known_ids = set(ids)
    for index, item in enumerate(items):
        label = item.get("id") or f"item[{index}]"
        source_path = item.get("source_path")
        if not source_path:
            errors.append(f"{label}: missing source_path")
        elif not (ROOT / source_path).is_file():
            errors.append(f"{label}: source_path does not exist: {source_path}")

        tags = item.get("tags", [])
        normalized_tags = [str(tag).strip().casefold() for tag in tags]
        if len(normalized_tags) != len(set(normalized_tags)):
            errors.append(f"{label}: duplicate tags after normalization")
        if any(not str(tag).strip() for tag in tags):
            errors.append(f"{label}: blank tag")

        canonical_id = item.get("canonical_id")
        if canonical_id and canonical_id not in known_ids:
            errors.append(f"{label}: unknown canonical_id: {canonical_id}")
        if item.get("canonical") is False and not canonical_id:
            warnings.append(f"{label}: non-canonical item has no canonical_id")

        if item.get("status") == "published" and item.get("visibility") == "public":
            if not item.get("canonical"):
                errors.append(f"{label}: public published item must be canonical")
            if item.get("rights_status") not in PUBLIC_RIGHTS:
                errors.append(f"{label}: public published item needs owned/licensed rights")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    print(f"Checked {len(items)} manifest items: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
