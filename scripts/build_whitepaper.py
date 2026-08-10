#!/usr/bin/env python3
from __future__ import annotations

from html import escape
from pathlib import Path
import re

import reportlab.rl_config
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/whitepaper"
SOURCE = DOCS / "virtue7_whitepaper.md"
TEXT_OUT = DOCS / "virtue7_ai-readable.txt"
PDF_OUT = DOCS / "virtue7_whitepaper.pdf"

# Stable PDF metadata/object ordering for deterministic builds.
reportlab.rl_config.invariant = 1

TITLE = "Virtue7: A Lightweight Governed Runtime for AI Work"
AUTHOR = "Virtue7"
DATE = "August 2026"


def inline(text: str) -> str:
    value = escape(text)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


def footer(canvas: Canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Times-Roman", 9)
    canvas.drawCentredString(LETTER[0] / 2, 0.46 * inch, str(doc.page))
    canvas.restoreState()


class Diagram(Flowable):
    def __init__(self, kind: str, caption: str, width: float = 6.25 * inch):
        self.kind = kind
        self.caption = caption
        self.width = width
        heights = {
            "mode-router": 1.38 * inch,
            "loading": 1.45 * inch,
            "improvement": 1.25 * inch,
        }
        self.height = heights.get(kind, 1.4 * inch) + 0.24 * inch

    def _box(self, c, x, y, w, h, label, size=8.5):
        c.rect(x, y, w, h, stroke=1, fill=0)
        c.setFont("Helvetica", size)
        lines = label.split("\n")
        start = y + h / 2 + (len(lines)-1) * 5 - 3
        for i, line in enumerate(lines):
            c.drawCentredString(x + w / 2, start - i * 10, line)

    def _arrow(self, c, x1, y1, x2, y2):
        c.line(x1, y1, x2, y2)
        import math
        angle = math.atan2(y2-y1, x2-x1)
        a = 5
        for off in (0.48, -0.48):
            c.line(x2, y2, x2 - a*math.cos(angle+off), y2 - a*math.sin(angle+off))

    def draw(self):
        c = self.canv
        c.saveState()
        c.setLineWidth(0.65)
        c.setStrokeColorRGB(0, 0, 0)
        c.setFillColorRGB(0, 0, 0)
        W = self.width
        H = self.height - 0.28 * inch

        if self.kind == "mode-router":
            bw, bh = 1.02*inch, 0.38*inch
            cx = W/2 - bw/2
            top = H - 0.43*inch
            self._box(c, cx, top, bw, bh, "Intent")
            ys = 0.22*inch
            labels = ["Chat", "Content", "Automation"]
            gap = (W - 3*bw) / 2
            for i, label in enumerate(labels):
                x = i*(bw+gap)
                self._box(c, x, ys, bw, bh, label)
                self._arrow(c, W/2, top, x+bw/2, ys+bh)


        elif self.kind == "loading":
            bw, bh = 0.9*inch, 0.36*inch
            y = H-0.48*inch
            labels = ["Boot", "Mode?", "Route?", "Profile?", "State", "Tool?"]
            gap = (W - len(labels)*bw)/(len(labels)-1)
            for i,label in enumerate(labels):
                x = i*(bw+gap)
                self._box(c,x,y,bw,bh,label,7.8)
                if i < len(labels)-1:
                    self._arrow(c,x+bw,y+bh/2,x+bw+gap,y+bh/2)
            c.setFont("Helvetica",8)
            c.drawCentredString(W/2,0.37*inch,"? = load only when the current step requires it")
            c.setFont("Courier",8)
            c.drawCentredString(W/2,0.13*inch,"B + M? + R? + P? + Smin + Tmin")


        elif self.kind == "improvement":
            bw,bh=0.92*inch,0.36*inch
            labels=["Observe","Propose","Sandbox","Evaluate","Promote"]
            gap=(W-len(labels)*bw)/(len(labels)-1)
            y=H-0.52*inch
            for i,label in enumerate(labels):
                x=i*(bw+gap)
                self._box(c,x,y,bw,bh,label,7.8)
                if i<len(labels)-1:
                    self._arrow(c,x+bw,y+bh/2,x+bw+gap,y+bh/2)

        c.setFont("Times-Italic", 8.2)
        c.drawCentredString(W/2, -1, self.caption)
        c.restoreState()


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("title", parent=base["Title"], fontName="Times-Bold", fontSize=17.5, leading=20.5, alignment=TA_CENTER, spaceAfter=23),
        "author": ParagraphStyle("author", parent=base["Normal"], fontName="Times-Roman", fontSize=10.5, leading=13, alignment=TA_CENTER, spaceAfter=0),
        "abstract": ParagraphStyle("abstract", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.7, leading=11.8, alignment=TA_JUSTIFY, leftIndent=0.52*inch, rightIndent=0.52*inch, spaceAfter=19),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="Times-Bold", fontSize=12.1, leading=14.0, alignment=TA_LEFT, spaceBefore=8, spaceAfter=5.5, keepWithNext=True),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.9, leading=12.0, alignment=TA_JUSTIFY, spaceAfter=6.4, firstLineIndent=0.23*inch, allowWidows=0, allowOrphans=0),
        "body_noindent": ParagraphStyle("body_noindent", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.9, leading=12.0, alignment=TA_JUSTIFY, spaceAfter=6.4, firstLineIndent=0, allowWidows=0, allowOrphans=0),
        "equation": ParagraphStyle("equation", parent=base["BodyText"], fontName="Courier", fontSize=9.1, leading=11, alignment=TA_CENTER, spaceBefore=3, spaceAfter=8),
        "list": ParagraphStyle("list", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.8, leading=11.9, alignment=TA_JUSTIFY, leftIndent=0.18*inch, firstLineIndent=0, spaceAfter=2.5),
    }


def parse(source: str, st: dict) -> list:
    lines = source.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip() == "## Abstract")
    lines = lines[start:]
    story = []
    paragraph = []
    numbered = []
    in_abstract = False
    first_after_heading = True

    def flush_para():
        nonlocal first_after_heading
        if paragraph:
            text = " ".join(x.strip() for x in paragraph)
            style = st["body_noindent"] if first_after_heading else st["body"]
            story.append(Paragraph(inline(text), style))
            paragraph.clear()
            first_after_heading = False

    def flush_numbered():
        if numbered:
            items=[ListItem(Paragraph(inline(item),st["list"])) for item in numbered]
            story.append(ListFlowable(items, bulletType="1", start="1", leftIndent=0.28*inch, bulletFontName="Times-Roman", bulletFontSize=9.5))
            story.append(Spacer(1,4))
            numbered.clear()

    i=0
    while i < len(lines):
        raw=lines[i].rstrip()
        line=raw.strip()
        if line == "## Abstract":
            flush_para(); flush_numbered(); in_abstract=True
            i += 1
            # gather abstract paragraph(s) until next H2
            parts=[]
            while i < len(lines) and not lines[i].startswith("## "):
                if lines[i].strip(): parts.append(lines[i].strip())
                i += 1
            story.append(Paragraph("<b>Abstract.</b> " + inline(" ".join(parts)), st["abstract"]))
            in_abstract=False
            continue
        if not line:
            flush_para(); flush_numbered(); i+=1; continue
        if line.startswith("## "):
            flush_para(); flush_numbered();
            story.append(Paragraph(inline(line[3:]), st["h2"]))
            first_after_heading=True
        elif re.match(r"^\[\[diagram:[a-z-]+\]\]\s+.+$", line):
            flush_para(); flush_numbered()
            m=re.match(r"^\[\[diagram:([a-z-]+)\]\]\s+(.+)$", line)
            story.append(Spacer(1,4))
            story.append(Diagram(m.group(1), m.group(2)))
            story.append(Spacer(1,8))
            first_after_heading=False
        elif re.match(r"^\d+\.\s+", line):
            flush_para(); numbered.append(re.sub(r"^\d+\.\s+", "", line))
        elif line.startswith("`") and line.endswith("`") and line.count("`")==2:
            flush_para(); flush_numbered(); story.append(Paragraph(inline(line[1:-1]), st["equation"])); first_after_heading=False
        else:
            flush_numbered(); paragraph.append(line)
        i += 1
    flush_para(); flush_numbered()
    return story


def build() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    TEXT_OUT.write_text(source.rstrip() + "\n", encoding="utf-8")
    st = styles()

    doc = BaseDocTemplate(
        str(PDF_OUT),
        pagesize=LETTER,
        leftMargin=0.91*inch,
        rightMargin=0.91*inch,
        topMargin=0.68*inch,
        bottomMargin=0.66*inch,
        title=TITLE,
        author=AUTHOR,
        subject="Chat, content, automation, and minimum-sufficient loading",
    )
    frame=Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="paper", showBoundary=0)
    doc.addPageTemplates([PageTemplate(id="Paper", frames=[frame], onPage=footer)])

    story=[
        Spacer(1,0.33*inch),
        Paragraph(TITLE,st["title"]),
        Paragraph(AUTHOR,st["author"]),
        Paragraph(DATE,st["author"]),
        Spacer(1,0.34*inch),
    ]
    story.extend(parse(source,st))
    doc.build(story)
    print(PDF_OUT)
    print(TEXT_OUT)


if __name__ == "__main__":
    build()
