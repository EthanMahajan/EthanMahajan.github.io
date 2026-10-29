"""Generate a portfolio PDF and link previews from the website's project data."""
from html import escape
from pathlib import Path
import re
from shutil import copyfile
import yaml
from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, Image, KeepTogether,
)
from reportlab.platypus.tableofcontents import TableOfContents
from build_browser_model import build_browser_model
from build_image_metadata import build_image_metadata

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


class PortfolioDocument(BaseDocTemplate):
    """Flow one compact editorial document, with real internal destinations."""

    def afterFlowable(self, flowable):
        key = getattr(flowable, "project_key", None)
        if key:
            # Target the heading, not just the containing page, when several
            # compact project summaries share one sheet.
            self.canv.bookmarkHorizontalAbsolute(key, self.frame._y + flowable.height + flowable.getSpaceAfter())
            self.canv.addOutlineEntry(flowable.getPlainText(), key, 0)
            self.notify("TOCEntry", (0, flowable.getPlainText(), self.page, key))


def build_pdf(config, socials, projects):
    destination = ROOT / "assets/pdf/Ethan_Mahajan_Portfolio.pdf"
    destination.parent.mkdir(parents=True, exist_ok=True)
    base = config["url"].rstrip("/") + (config.get("baseurl") or "")
    doc = PortfolioDocument(str(destination), pagesize=(WIDTH, HEIGHT),
                            leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=40, bottomMargin=46,
                            title="Ethan Mahajan: Engineering Portfolio",
                            author="Ethan Mahajan")
    def footer(pdf, document):
        pdf.setStrokeColor(colors.HexColor("#dbe3e1"))
        pdf.line(MARGIN, 35, WIDTH - MARGIN, 35)
        pdf.setFillColor(colors.HexColor(MUTED))
        pdf.setFont("Helvetica", 8)
        pdf.drawString(MARGIN, 22, "Ethan Mahajan | Engineering portfolio")
        pdf.linkURL(base + "/projects/", (MARGIN, 18, 290, 32), relative=0)
        pdf.drawRightString(WIDTH - MARGIN, 22, f"Page {document.page}")
        if document.page == 1:
            pdf.bookmarkPage("contents")
        else:
            pdf.drawCentredString(WIDTH / 2 + 75, 22, "Contents")
            pdf.linkRect("Back to contents", "contents", (345, 18, 410, 32), relative=0, thickness=0)

    frame = Frame(MARGIN, 46, CONTENT, HEIGHT - 86,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="portfolio", frames=frame, onPage=footer))
    def style(name, size=9, leading=11.5, color=INK, **kwargs):
        return ParagraphStyle(name, fontName="Helvetica", fontSize=size,
                              leading=leading, textColor=colors.HexColor(color),
                              spaceAfter=4, **kwargs)
    body = style("body")
    meta = style("meta", 8, 10, MUTED)
    caption = style("caption", 7.5, 9, MUTED)
    heading = ParagraphStyle(
        "project", fontName="Helvetica-Bold", fontSize=15, leading=18,
        textColor=colors.HexColor(ACCENT), spaceBefore=12, spaceAfter=4,
        keepWithNext=True)
    title = ParagraphStyle("title", parent=heading, fontSize=26, leading=29, spaceBefore=0)
    toc = TableOfContents()
    toc.levelStyles = [style("contents-entry", 9, 12, ACCENT, leftIndent=0, rightIndent=0, spaceBefore=1)]
    story = [Paragraph("Ethan Mahajan", title),
             Paragraph("ENGINEERING PORTFOLIO", style("eyebrow", 9, 12, ACCENT)),
             Paragraph(escape(config["description"].strip()), body),
             Paragraph(f'<link href="mailto:{socials["email"]}" color="{ACCENT}">{socials["email"]}</link>'
                       f' | <link href="{base}" color="{ACCENT}">{base.replace("https://", "")}</link>', meta),
             Paragraph("From working prototypes to current design work", ParagraphStyle(
                 "intro", parent=heading, fontSize=11, leading=14, spaceBefore=5)),
             Paragraph("These five projects connect CAD, fabrication, electronics, and engineering communication. "
                       "Each summary identifies my contribution, the evidence available, and the work still pending. "
                       "The linked case studies provide complete documentation and demonstrations.", body),
             Paragraph("Contents", ParagraphStyle("toc-title", parent=heading, fontSize=11, leading=13, spaceBefore=6)),
             toc, Spacer(1, 4)]
    for path, project in projects:
        summary = project["pdf_summary"]
        hero = project.get("hero", {})
        project_heading = Paragraph(escape(project["title"]), heading)
        project_heading.project_key = path.stem
        details = project["project_summary"]
        story.append(KeepTogether([project_heading, Paragraph(
            escape(details["status"]) + " | " + escape(details["role"]), meta)]))
        source = ROOT / hero.get("image", project["img"]).lstrip("/")
        with PILImage.open(source) as original:
            width, height = original.size
        scale = min(112 / width, 110 / height)
        photo = Image(str(source), width * scale, height * scale, hAlign="CENTER")
        media = [photo, Spacer(1, 4), Paragraph(escape(summary.get("caption", hero.get("caption", ""))), caption)]
        narrative = [Paragraph('<b>Design and contribution.</b> ' + escape(summary["design"]), body),
                     Paragraph('<b>Evidence and next steps.</b> ' + escape(summary["evidence"]), body),
                     Paragraph('<b>Tools:</b> ' + escape(details["tools"]), meta),
                     Paragraph(f'<link href="{base}/projects/{path.stem}.html" color="{ACCENT}">Full case study and supporting evidence</link>', meta)]
        section = Table([[media, narrative]], colWidths=[124, CONTENT - 124], hAlign="LEFT")
        section.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (0, 0), 12),
            ("RIGHTPADDING", (1, 0), (1, 0), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(section)
    doc.multiBuild(story)
    print(f"Generated {destination.relative_to(ROOT)} with all {len(projects)} projects and linked contents")


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
    build_browser_model()
    # Keep the original source asset while publishing it with a standard PNG extension.
    copyfile(ROOT / "assets/img/PurifierPCB", ROOT / "assets/img/PurifierPCB.png")
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    socials = yaml.safe_load((ROOT / "_data/socials.yml").read_text(encoding="utf-8"))
    projects = [(path, frontmatter(path)) for path in sorted((ROOT / "_projects").glob("*.md"))]
    ordered = sorted(projects, key=lambda item: (item[1]["category"] != "Engineering", item[1]["importance"], item[1]["title"]))
    if not ordered:
        raise ValueError("No portfolio projects found")
    build_pdf(config, socials, ordered)
    lead = ordered[0][1]
    card("portfolio", "Design, build, test, refine", "Mechanical engineering at Georgia Tech", lead.get("hero", {}).get("image", lead["img"]))
    for path, project in projects:
        card(path.stem, project["title"], project.get("card_label", project["category"]), project.get("hero", {}).get("image", project["img"]))
    print("Generated 1200 x 630 homepage and project share cards")
    build_image_metadata()


if __name__ == "__main__":
    main()
