"""Record intrinsic image dimensions so figures reserve space before loading."""
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def build_image_metadata():
    dimensions = {}
    for path in sorted((ROOT / "assets/img").rglob("*")):
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".tiff"}:
            continue
        with Image.open(path) as image:
            dimensions[path.relative_to(ROOT).as_posix()] = {"width": image.width, "height": image.height}
    (ROOT / "_data/image_dimensions.json").write_text(json.dumps(dimensions, indent=2) + "\n", encoding="utf-8")
    print(f"Recorded intrinsic dimensions for {len(dimensions)} images")


if __name__ == "__main__":
    build_image_metadata()
