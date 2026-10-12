"""Check rendered portfolio links, IDs, images, metadata, and PDF structure."""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit, urljoin

from PIL import Image
from pypdf import PdfReader


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.images, self.meta = [], [], [], {}
        self.headings, self.iframes = [], []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag in ("a", "link") and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)
        if tag == "iframe":
            self.iframes.append(attrs)
        if tag == "h1":
            self.headings.append(tag)
        if tag == "meta":
            self.meta[attrs.get("property", attrs.get("name"))] = attrs.get("content")


def check(site):
    errors = []
    pages = {p.relative_to(site).as_posix(): Page(p) for p in site.rglob("*.html") if "assets/" not in p.relative_to(site).as_posix()}
    for name, page in pages.items():
        for key, count in Counter(page.ids).items():
            if count > 1:
                errors.append(f"{name}: duplicate ID {key}")
        if len(page.headings) != 1:
            errors.append(f"{name}: expected exactly one h1")
        for iframe in page.iframes:
            if not iframe.get("title"):
                errors.append(f"{name}: iframe without title")
        for img in page.images:
            if "alt" not in img:
                errors.append(f"{name}: image missing alt text")
        references = page.links + [i.get("src", "") for i in page.images]
        references += [page.meta.get("og:image", "")]
        for reference in references:
            if not reference or reference.startswith(("mailto:", "tel:", "data:")):
                continue
            parts = urlsplit(reference)
            if parts.netloc and parts.netloc != "ethanmahajan.github.io":
                continue
            resolved = urlsplit(urljoin("https://ethanmahajan.github.io/" + name, reference))
            target_name = unquote(resolved.path).lstrip("/")
            if not target_name or target_name.endswith("/"):
                target_name += "index.html"
            target = site / target_name
            if not target.exists():
                errors.append(f"{name}: missing local reference {reference}")
            elif resolved.fragment and target_name in pages and unquote(resolved.fragment) not in pages[target_name].ids:
                errors.append(f"{name}: missing anchor {reference}")
        if not page.meta.get("description") or not page.meta.get("og:image"):
            errors.append(f"{name}: missing description or share image")
    for name in ("portfolio", "artorius", "phone_mount", "air_purifier", "laser_engraved_chess_board", "shape_machine"):
        path = site / "assets/img/social" / (name + ".png")
        with Image.open(path) as image:
            if image.size != (1200, 630):
                errors.append(f"{path}: incorrect share-image size")
    pdf = PdfReader(site / "assets/pdf/Ethan_Mahajan_Portfolio.pdf")
    if len(pdf.pages) < 2:
        errors.append("Expected a cover and at least one selected project in the PDF")
    for index, page in enumerate(pdf.pages):
        if len(page.extract_text()) < 200:
            errors.append(f"PDF page {index + 1}: missing text")
        if not page.get("/Annots"):
            errors.append(f"PDF page {index + 1}: missing links")
    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(f"PASS: {len(pages)} pages, local links and anchors, image descriptions, share cards, and linked {len(pdf.pages)}-page PDF")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path, nargs="?", default=Path("_site"))
    check(parser.parse_args().site)
