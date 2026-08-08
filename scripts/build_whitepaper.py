#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from html import escape
import re
import reportlab

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, ListFlowable, ListItem, PageBreak, PageTemplate,
    Paragraph, Spacer, HRFlowable,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/whitepaper/compressible-content-architecture_whitepaper.md"
TEXT_OUT = ROOT / "docs/whitepaper/compressible-content-architecture_ai-readable.txt"
PDF_OUT = ROOT / "docs/whitepaper/compressible-content-architecture_whitepaper.pdf"

INK = HexColor("#172033")
MUTED = HexColor("#596273")
ACCENT = HexColor("#8056D6")
PALE = HexColor("#EEE9FA")
WHITE = HexColor("#FFFFFF")


def register_fonts() -> None:
    font_dir = Path(reportlab.__file__).resolve().parent / "fonts"
    pdfmetrics.registerFont(TTFont("V7Sans", str(font_dir / "Vera.ttf")))
    pdfmetrics.registerFont(TTFont("V7Sans-Bold", str(font_dir / "VeraBd.ttf")))
    pdfmetrics.registerFont(TTFont("V7Sans-Oblique", str(font_dir / "VeraIt.ttf")))
    pdfmetrics.registerFont(TTFont("V7Sans-BoldOblique", str(font_dir / "VeraBI.ttf")))
    pdfmetrics.registerFont(TTFont("V7Mono", str(font_dir / "Vera.ttf")))
    pdfmetrics.registerFontFamily(
        "V7Sans", normal="V7Sans", bold="V7Sans-Bold",
        italic="V7Sans-Oblique", boldItalic="V7Sans-BoldOblique",
    )


def inline(text: str) -> str:
    value = escape(text)
    value = re.sub(r"`([^`]+)`", r'<font name="V7Mono">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


def page_header_footer(canvas, doc) -> None:
    canvas.saveState()
    width, height = LETTER
    canvas.setStrokeColor(PALE)
    canvas.setLineWidth(0.8)
    canvas.line(0.72 * inch, height - 0.62 * inch, width - 0.72 * inch, height - 0.62 * inch)
    canvas.setFont("V7Sans", 7.7)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.72 * inch, height - 0.47 * inch, "THE COMPRESSIBLE CONTENT ARCHITECTURE · V0.4")
    canvas.drawRightString(width - 0.72 * inch, 0.45 * inch, str(doc.page))
    canvas.restoreState()


def cover(canvas, doc) -> None:
    canvas.saveState()
    width, height = LETTER
    canvas.setFillColor(INK)
    canvas.rect(0, 0, width, height, stroke=0, fill=1)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, height - 0.27 * inch, width, 0.27 * inch, stroke=0, fill=1)
    canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle("cover_kicker", parent=base["Normal"], fontName="V7Sans-Bold", fontSize=9, leading=12, textColor=HexColor("#CFC2F2"), spaceAfter=22, tracking=1.5),
        "cover_title": ParagraphStyle("cover_title", parent=base["Title"], fontName="V7Sans-Bold", fontSize=30, leading=35, textColor=WHITE, alignment=TA_LEFT, spaceAfter=22),
        "cover_subtitle": ParagraphStyle("cover_subtitle", parent=base["Normal"], fontName="V7Sans", fontSize=14, leading=21, textColor=HexColor("#E8E4F0"), spaceAfter=28),
        "cover_meta": ParagraphStyle("cover_meta", parent=base["Normal"], fontName="V7Sans", fontSize=9, leading=14, textColor=HexColor("#B9C0D0")),
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName="V7Sans-Bold", fontSize=22, leading=27, textColor=INK, spaceBefore=0, spaceAfter=16, keepWithNext=True),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="V7Sans-Bold", fontSize=19, leading=24, textColor=INK, spaceBefore=0, spaceAfter=15, keepWithNext=True),
        "h3": ParagraphStyle("h3", parent=base["Heading3"], fontName="V7Sans-Bold", fontSize=12.5, leading=17, textColor=ACCENT, spaceBefore=12, spaceAfter=7, keepWithNext=True),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName="V7Sans", fontSize=9.35, leading=14.4, textColor=INK, alignment=TA_LEFT, spaceAfter=9, allowWidows=0, allowOrphans=0),
        "list": ParagraphStyle("list", parent=base["BodyText"], fontName="V7Sans", fontSize=9.2, leading=14, textColor=INK, leftIndent=4, spaceAfter=4),
        "section_no": ParagraphStyle("section_no", parent=base["Normal"], fontName="V7Sans-Bold", fontSize=8, leading=10, textColor=ACCENT, spaceAfter=8),
    }


def parse_body(source: str, s: dict) -> list:
    lines = source.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip() == "## Abstract")
    lines = lines[start:]
    story: list = []
    paragraph: list[str] = []
    list_items: list[str] = []
    section_count = 0

    def flush_paragraph() -> None:
        if paragraph:
            story.append(Paragraph(inline(" ".join(part.strip() for part in paragraph)), s["body"]))
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            flow = [ListItem(Paragraph(inline(item), s["list"])) for item in list_items]
            story.append(ListFlowable(flow, bulletType="bullet", start="circle", leftIndent=18, bulletFontName="V7Sans"))
            story.append(Spacer(1, 5))
            list_items.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_paragraph()
            flush_list()
            continue
        if line.startswith("## "):
            flush_paragraph()
            flush_list()
            if story:
                story.append(PageBreak())
            section_count += 1
            label = "FOUNDATION" if section_count == 1 else f"SECTION {section_count - 1:02d}"
            story.append(Paragraph(label, s["section_no"]))
            story.append(Paragraph(inline(line[3:]), s["h2"]))
            story.append(HRFlowable(width="100%", thickness=1.2, color=PALE, spaceAfter=16))
        elif line.startswith("### "):
            flush_paragraph()
            flush_list()
            if line.startswith("### 2.5 "):
                story.append(PageBreak())
            story.append(Paragraph(inline(line[4:]), s["h3"]))
        elif re.match(r"^[-*] ", line):
            flush_paragraph()
            list_items.append(re.sub(r"^[-*] ", "", line))
        else:
            flush_list()
            paragraph.append(line)
    flush_paragraph()
    flush_list()
    return story


def build() -> None:
    register_fonts()
    s = styles()
    source = SOURCE.read_text(encoding="utf-8")
    TEXT_OUT.write_text(source.rstrip() + "\n", encoding="utf-8")

    doc = BaseDocTemplate(
        str(PDF_OUT), pagesize=LETTER, leftMargin=0.78 * inch, rightMargin=0.78 * inch,
        topMargin=0.82 * inch, bottomMargin=0.72 * inch,
        title="The Compressible Content Architecture, v0.4",
        author="Virtue7 Writing Kit",
        subject="A Personal, Governed Runtime for Writing, Research, and Multi-Format Production",
    )
    width, height = LETTER
    cover_frame = Frame(0.82 * inch, 0.8 * inch, width - 1.64 * inch, height - 1.6 * inch, id="cover", showBoundary=0)
    body_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body", showBoundary=0)
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cover_frame], onPage=cover, autoNextPageTemplate="Body"),
        PageTemplate(id="Body", frames=[body_frame], onPage=page_header_footer),
    ])

    story = [
        Spacer(1, 0.62 * inch),
        Paragraph("VIRTUE7 WRITING KIT · OPEN WORKING PAPER", s["cover_kicker"]),
        Paragraph("The Compressible<br/>Content Architecture,<br/>v0.4", s["cover_title"]),
        Paragraph("A Personal, Governed Runtime for Writing, Research, and Multi-Format Production", s["cover_subtitle"]),
        HRFlowable(width="28%", thickness=3, color=ACCENT, hAlign="LEFT", spaceAfter=28),
        Spacer(1, 2.15 * inch),
        Paragraph("Reference implementation<br/>August 2026<br/>Open source · model neutral · white-label output", s["cover_meta"]),
        PageBreak(),
    ]
    story.extend(parse_body(source, s))
    doc.build(story)
    print(PDF_OUT)
    print(TEXT_OUT)


if __name__ == "__main__":
    build()
