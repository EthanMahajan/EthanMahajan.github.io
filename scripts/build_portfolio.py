"""Generate a portfolio PDF and link previews from the website's project data."""
from html import escape
from pathlib import Path
import re
from shutil import copyfile
import yaml
from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
ACCENT, INK, MUTED, SURFACE = "#24563d", "#202c34", "#596773", "#f3f6f5"
WIDTH, HEIGHT, MARGIN = 612, 792, 48
CONTENT = WIDTH - 2 * MARGIN


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
    if not match:
        raise ValueError(f"Missing front matter: {path}")
    return yaml.safe_load(match.group(1))


def paragraph(pdf, text, top, size=11, color=INK, bold=False):
    style = ParagraphStyle("portfolio", fontName="Helvetica-Bold" if bold else "Helvetica",
                           fontSize=size, leading=size * 1.5, textColor=colors.HexColor(color))
    flow = Paragraph(escape(str(text)), style)
    _, height = flow.wrap(CONTENT, HEIGHT)
    bottom = top - height
    if bottom < 60:
        raise ValueError("Content exceeds a portfolio page; shorten its source highlights.")
    flow.drawOn(pdf, MARGIN, bottom)
    return bottom


def image(pdf, path, bottom, height):
    source = ROOT / path.lstrip("/")
    if not source.is_file():
        raise FileNotFoundError(source)
    pdf.setFillColor(colors.HexColor(SURFACE))
    pdf.roundRect(MARGIN, bottom, CONTENT, height, 8, stroke=0, fill=1)
    pdf.drawImage(ImageReader(str(source)), MARGIN + 12, bottom + 12,
                  width=CONTENT - 24, height=height - 24,
                  preserveAspectRatio=True, anchor="c", mask="auto")


def footer(pdf, number, total, base):
    pdf.setStrokeColor(colors.HexColor("#dbe3e1"))
    pdf.line(MARGIN, 43, WIDTH - MARGIN, 43)
    pdf.setFont("Helvetica", 8)
    pdf.setFillColor(colors.HexColor(MUTED))
    pdf.drawString(MARGIN, 28, "Ethan Mahajan | Engineering portfolio")
    pdf.linkURL(base + "/projects/", (MARGIN, 24, 360, 38), relative=0)
    pdf.drawRightString(WIDTH - MARGIN, 28, f"{number} / {total}")


def build_pdf(config, socials, projects):
    destination = ROOT / "assets/pdf/Ethan_Mahajan_Portfolio.pdf"
    destination.parent.mkdir(parents=True, exist_ok=True)
    base = config["url"].rstrip("/") + (config.get("baseurl") or "")
    pdf = canvas.Canvas(str(destination), pagesize=(WIDTH, HEIGHT), invariant=1)
    pdf.setTitle("Ethan Mahajan: Selected Engineering Work")
    pdf.setAuthor("Ethan Mahajan")
    total = len(projects) + 1
    top = paragraph(pdf, "SELECTED ENGINEERING WORK", 735, 10, ACCENT, True)
    top = paragraph(pdf, "Ethan Mahajan", top - 20, 32, INK, True)
    top = paragraph(pdf, config["description"].strip(), top - 12, 13, MUTED)
    image(pdf, projects[0][1]["hero"]["image"], 330, 235)
    top = paragraph(pdf, "A closer look at the work", 303, 17, INK, True)
    for _, project in projects:
        top = paragraph(pdf, project["title"], top - 14, 12, ACCENT, True)
        top = paragraph(pdf, project["project_summary"]["result"], top - 4, 10, MUTED)
    top = paragraph(pdf, socials["email"], top - 22, 11, ACCENT)
    pdf.linkURL("mailto:" + socials["email"], (MARGIN, top, 320, top + 17), relative=0)
    top = paragraph(pdf, base.replace("https://", ""), top - 7, 10, MUTED)
    pdf.linkURL(base, (MARGIN, top, 380, top + 15), relative=0)
    latest = max(str(p["documentation_updated"]) for _, p in projects)
    paragraph(pdf, "Project documentation updated " + latest, top - 12, 8, MUTED)
    footer(pdf, 1, total, base)
    pdf.showPage()
    for index, (path, project) in enumerate(projects, 2):
        top = paragraph(pdf, project.get("card_label", project["category"]).upper(), 735, 9, ACCENT, True)
        top = paragraph(pdf, project["title"], top - 12, 25, INK, True)
        top = paragraph(pdf, project["description"], top - 8, 11, MUTED)
        img_top = top - 20
        image(pdf, project["hero"]["image"], img_top - 225, 225)
        top = paragraph(pdf, project["hero"]["caption"], img_top - 235, 9, MUTED)
        for label, key in [("Role", "role"), ("Tools", "tools"), ("Status", "status")]:
            top = paragraph(pdf, label + ": " + project["project_summary"][key], top - 10, 10)
        top = paragraph(pdf, "Build highlights", top - 20, 14, INK, True)
        for highlight in project["portfolio_highlights"]:
            top = paragraph(pdf, "• " + highlight, top - 9, 10)
        top = paragraph(pdf, "Explore the full case study and demonstration", top - 20, 11, ACCENT, True)
        pdf.linkURL(base + "/projects/" + path.stem + ".html", (MARGIN, top, WIDTH - MARGIN, top + 17), relative=0)
        footer(pdf, index, total, base)
        pdf.showPage()
    pdf.save()
    print(f"Generated {destination.relative_to(ROOT)} ({total} pages)")


def font(size, bold=False):
    candidates = [Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
                  Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


def card(slug, title, subtitle, source):
    destination = ROOT / "assets/img/social" / f"{slug}.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    preview = PILImage.new("RGB", (1200, 630), SURFACE)
    draw = ImageDraw.Draw(preview)
    draw.rectangle((0, 0, 1200, 12), fill=ACCENT)
    draw.text((60, 66), "ETHAN MAHAJAN", fill=ACCENT, font=font(24, True))
    lines, line = [], ""
    for word in title.split():
        candidate = (line + " " + word).strip()
        if draw.textlength(candidate, font=font(45, True)) > 515 and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    lines.append(line)
    y = 158
    for line in lines:
        draw.text((60, y), line, fill=INK, font=font(45, True))
        y += 58
    draw.text((60, y + 30), subtitle, fill=MUTED, font=font(23))
    draw.text((60, 550), "ethanmahajan.github.io", fill=ACCENT, font=font(23))
    with PILImage.open(ROOT / source.lstrip("/")) as original:
        photo = original.convert("RGBA")
        photo.thumbnail((490, 460), PILImage.Resampling.LANCZOS)
        preview.paste(photo, (660 + (490 - photo.width) // 2, 85 + (460 - photo.height) // 2), photo)
    preview.save(destination, optimize=True)


def main():
    # Keep the original source asset while publishing it with a standard PNG extension.
    copyfile(ROOT / "assets/img/PurifierPCB", ROOT / "assets/img/PurifierPCB.png")
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    socials = yaml.safe_load((ROOT / "_data/socials.yml").read_text(encoding="utf-8"))
    projects = [(path, frontmatter(path)) for path in sorted((ROOT / "_projects").glob("*.md"))]
    selected = sorted([(path, project) for path, project in projects if project.get("portfolio")], key=lambda item: item[1]["importance"])
    if not selected:
        raise ValueError("No projects selected for the portfolio PDF")
    build_pdf(config, socials, selected)
    card("portfolio", "Design. Build. Test. Refine.", "Mechanical engineering at Georgia Tech", selected[0][1]["hero"]["image"])
    for path, project in projects:
        card(path.stem, project["title"], project.get("card_label", project["category"]), project.get("hero", {}).get("image", project["img"]))
    print("Generated 1200 x 630 homepage and project share cards")


if __name__ == "__main__":
    main()
