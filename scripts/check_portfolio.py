"""Check rendered portfolio links, IDs, images, metadata, and PDF structure."""
import argparse
from collections import Counter
from datetime import date
from hashlib import sha256
from html.parser import HTMLParser
import json
from math import isfinite
from pathlib import Path
from urllib.parse import unquote, urlsplit, urljoin
from zipfile import ZipFile
import xml.etree.ElementTree as ET

from PIL import Image
from pypdf import PdfReader
import yaml


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
        if attrs.get("data-model-url"):
            self.links.append(attrs["data-model-url"])
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
    model_folder = site / 'assets/models/artorius'
    report = json.loads((model_folder / 'preview-manifest.json').read_text())
    for key, filename in (('source', 'artorius.3mf'), ('preview', 'artorius-preview.3mf')):
        model = model_folder / filename
        if sha256(model.read_bytes()).hexdigest() != report[key + '_sha256']:
            errors.append(f'Model: {key} checksum does not match generated manifest')
    if report['preview_bytes'] >= report['source_bytes'] * 0.3:
        errors.append('Model: browser preview should be under 30% of the original download size')
    meshes, faces = 0, 0
    core = '{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}'
    with ZipFile(model_folder / 'artorius-preview.3mf') as archive:
        with archive.open('3D/3dmodel.model') as stream:
            for _, element in ET.iterparse(stream, events=('end',)):
                if element.tag != core + 'object':
                    continue
                mesh = element.find(core + 'mesh')
                if mesh is not None:
                    meshes += 1
                    vertices = mesh.find(core + 'vertices')
                    for vertex in vertices:
                        if not all(isfinite(float(vertex.get(k))) for k in ('x', 'y', 'z')):
                            errors.append('Model: non-finite vertex')
                    triangles = mesh.find(core + 'triangles')
                    faces += len(triangles)
                    if not len(triangles):
                        errors.append('Model: an assembly mesh disappeared')
                    for triangle in triangles:
                        if not all(0 <= int(triangle.get(k)) < len(vertices) for k in ('v1', 'v2', 'v3')):
                            errors.append('Model: invalid triangle indices')
                element.clear()
    if meshes != report['meshes'] or faces != report['preview_triangles']:
        errors.append('Model: preview mesh or triangle counts differ from the generation report')
    root = Path(__file__).resolve().parents[1]
    project_keys = {p.stem for p in (root / '_projects').glob('*.md')}
    for note in (root / '_notes').glob('*.md'):
        data = yaml.safe_load(note.read_text(encoding='utf-8').split('---', 2)[1])
        if data.get('published') is False:
            continue
        if not all(data.get(k) for k in ('title', 'description', 'date', 'project')):
            errors.append(f'{note.name}: notebook entry is missing required metadata')
        if data.get('project') not in project_keys or not isinstance(data.get('date'), date):
            errors.append(f'{note.name}: notebook entry needs a valid project and actual YAML date')
    pdf = PdfReader(site / "assets/pdf/Ethan_Mahajan_Portfolio.pdf")
    if len(pdf.pages) < 2:
        errors.append("Expected a compact portfolio with linked contents and project summaries")
    project_sources = (Path(__file__).resolve().parents[1] / "_projects").glob("*.md")
    expected_titles = [yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])["title"] for p in project_sources]
    outline = {item.title: pdf.get_destination_page_number(item) for item in pdf.outline if not isinstance(item, list)}
    if any(item.top is None or float(item.top) <= 0 for item in pdf.outline if not isinstance(item, list)):
        errors.append("PDF: project bookmarks must target their headings")
    for title in expected_titles:
        if title not in outline:
            errors.append(f"PDF: missing project bookmark {title}")
        elif title not in pdf.pages[outline[title]].extract_text():
            errors.append(f"PDF: project bookmark points to wrong page: {title}")
        if title not in pdf.pages[0].extract_text():
            errors.append(f"PDF: project missing from contents: {title}")
    internal_links = [annotation.get_object() for p in pdf.pages for annotation in p.get("/Annots", []) if annotation.get_object().get("/Dest")]
    if len(internal_links) < len(expected_titles):
        errors.append("PDF: contents must link internally to every project")
    for index, page in enumerate(pdf.pages):
        if len(page.extract_text()) < 200:
            errors.append(f"PDF page {index + 1}: missing text")
        if not page.get("/Annots"):
            errors.append(f"PDF page {index + 1}: missing links")
    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(f"PASS: {len(pages)} pages, local links and anchors, image descriptions, share cards, notebook metadata, browser model, and linked {len(pdf.pages)}-page PDF")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path, nargs="?", default=Path("_site"))
    check(parser.parse_args().site)
