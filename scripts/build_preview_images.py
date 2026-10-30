"""Create responsive WebP variants in a built preview (portable ImageMagick fallback)."""
import argparse
from pathlib import Path
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('site', type=Path)
args = parser.parse_args()
count = 0
for path in (args.site / 'assets/img').rglob('*'):
    if path.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.gif', '.tiff'}:
        continue
    with Image.open(path) as source:
        original = ImageOps.exif_transpose(source).convert('RGB')
        for width in (480, 800, 1400):
            target = path.with_name(f'{path.stem}-{width}.webp')
            image = original.copy()
            image.thumbnail((width, round(original.height * width / original.width)), Image.Resampling.LANCZOS)
            image.save(target, quality=85)
            count += 1
print(f'Generated {count} responsive images in {args.site}')
