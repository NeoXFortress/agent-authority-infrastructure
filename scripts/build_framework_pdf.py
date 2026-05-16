from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers" / "agent-authority-infrastructure-framework-v1.pdf"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def md_to_story(markdown: str, styles):
    story = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            story.append(Spacer(1, 0.08 * inch))
            continue
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["Title"]))
            story.append(Spacer(1, 0.16 * inch))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["Heading2"]))
            story.append(Spacer(1, 0.08 * inch))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.startswith("- "):
            story.append(Paragraph("• " + line[2:], styles["AAIBullet"]))
        elif line.startswith("|"):
            continue
        elif line.startswith(">"):
            story.append(Paragraph(line.lstrip("> "), styles["Quote"]))
        else:
            safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            story.append(Paragraph(safe, styles["Body"]))
    return story


def main():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#1f2937"),
        spaceAfter=5,
    ))
    styles.add(ParagraphStyle(
        name="AAIBullet",
        parent=styles["Body"],
        leftIndent=16,
        firstLineIndent=-10,
    ))
    styles.add(ParagraphStyle(
        name="Quote",
        parent=styles["Body"],
        borderColor=colors.HexColor("#10b981"),
        borderWidth=1,
        borderPadding=8,
        backColor=colors.HexColor("#ecfdf5"),
    ))
    styles["Title"].fontName = "Helvetica-Bold"
    styles["Title"].fontSize = 22
    styles["Title"].leading = 26
    styles["Title"].textColor = colors.HexColor("#0f172a")
    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontSize = 15
    styles["Heading2"].leading = 18
    styles["Heading2"].textColor = colors.HexColor("#0f766e")
    styles["Heading3"].fontName = "Helvetica-Bold"
    styles["Heading3"].fontSize = 12
    styles["Heading3"].textColor = colors.HexColor("#0f172a")

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title="Agent Authority Infrastructure Framework v1.0",
        author="Julio Berroa, NeoXFortress LLC",
    )

    files = [
        "papers/the-case-for-agent-authority-infrastructure.md",
        "docs/01-definition.md",
        "docs/02-framework.md",
        "docs/03-reference-architecture.md",
        "docs/05-what-aai-is-not.md",
        "docs/06-policy-context.md",
        "docs/08-faq.md",
    ]
    story = []
    for index, path in enumerate(files):
        if index:
            story.append(PageBreak())
        story.extend(md_to_story(read(path), styles))

    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    main()
