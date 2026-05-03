"""Generate CW2_SUBMISSION.pdf with updated GitHub URL and commit history."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib import colors

# Output path
output_path = "CW2_SUBMISSION.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    topMargin=20*mm,
    bottomMargin=15*mm,
    leftMargin=18*mm,
    rightMargin=18*mm,
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    'DocTitle', parent=styles['Title'], fontSize=18, spaceAfter=4*mm,
    textColor=HexColor('#1a1a2e')
))
styles.add(ParagraphStyle(
    'SectionHead', parent=styles['Heading2'], fontSize=13, spaceBefore=8*mm,
    spaceAfter=3*mm, textColor=HexColor('#16213e'), bold=True
))
styles.add(ParagraphStyle(
    'SubHead', parent=styles['Heading3'], fontSize=11, spaceBefore=4*mm,
    spaceAfter=2*mm, textColor=HexColor('#0f3460'), bold=True
))
styles.add(ParagraphStyle(
    'InfoField', parent=styles['Normal'], fontSize=10, spaceAfter=1*mm,
    leading=14
))
styles.add(ParagraphStyle(
    'CommitMono', parent=styles['Normal'], fontSize=8.5, fontName='Courier',
    leading=12, spaceAfter=0.5*mm
))

story = []

# ── Header ──
story.append(Paragraph("XJCO3011 — Coursework 2: Search Engine Tool", styles['DocTitle']))
story.append(Paragraph("Submission Document", styles['Heading2']))
story.append(Spacer(1, 3*mm))

# ── Student Info ──
info_data = [
    ["Student Name:", "Minhao Gao"],
    ["Student ID:", "201691058"],
    ["Module:", "XJCO3011 — Web Services and Web Data"],
    ["Submission Date:", "May 2026"],
]
info_table = Table(info_data, colWidths=[50*mm, 100*mm])
info_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
]))
story.append(info_table)
story.append(Spacer(1, 5*mm))

# ── (A) Video Link ──
story.append(Paragraph("(A) Video Demonstration Link", styles['SectionHead']))
story.append(Paragraph("Platform: Google Drive / YouTube / OneDrive (public link required)", styles['InfoField']))
video_link_style = ParagraphStyle('VideoLink', parent=styles['InfoField'],
                                   textColor=HexColor('#cc0000'), fontName='Helvetica-Bold')
story.append(Paragraph("Video Link: <b>[TO BE FILLED AFTER RECORDING]</b>", video_link_style))
story.append(Paragraph("The video must be accessible via a public URL. Test the link in incognito mode before submitting.", styles['InfoField']))
story.append(Spacer(1, 2*mm))

bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leftIndent=10*mm, leading=14)
story.append(Paragraph("<b>Video Requirements:</b>", styles['InfoField']))
for b in [
    "Duration: Maximum 5 minutes (strict)",
    "Format: MP4 or MOV",
    "Content: Live demo + design explanation + testing + Git history + GenAI reflection",
    "Must cover all 5 components per coursework brief",
]:
    story.append(Paragraph(f"<bullet>&bull;</bullet>{b}", bullet_style))

# ── (B) GitHub Repository ──
story.append(Paragraph("(B) GitHub Repository URL", styles['SectionHead']))
story.append(Paragraph("Repository: <b>https://github.com/Bartley007/xjco3011-cw2</b>",
                        ParagraphStyle('RepoLink', parent=styles['InfoField'],
                                       textColor=colors.blue, fontName='Courier')))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("<b>Repository Contents:</b>", styles['InfoField']))

# Files table
file_header_style = ParagraphStyle('TH', parent=styles['Normal'], fontSize=9, fontName='Helvetica-Bold')
file_cell_style = ParagraphStyle('TD', parent=styles['Normal'], fontSize=9, leading=13)

files_data = [
    [Paragraph("File / Directory", file_header_style),
     Paragraph("Description", file_header_style)],
    [Paragraph(".gitignore", file_cell_style),
     Paragraph("Git ignore rules", file_cell_style)],
    [Paragraph("requirements.txt", file_cell_style),
     Paragraph("Python dependencies (requests, beautifulsoup4)", file_cell_style)],
    [Paragraph("README.md", file_cell_style),
     Paragraph("Project documentation with setup/usage instructions", file_cell_style)],
    [Paragraph("src/", file_cell_style),
     Paragraph("Core source code modules", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;crawler.py", file_cell_style),
     Paragraph("Web crawler for quotes.toscrape.com (BeautifulSoup)", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;indexer.py", file_cell_style),
     Paragraph("Inverted index builder (term frequency + positions)", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;search.py", file_cell_style),
     Paragraph("Intersection-based multi-word search engine", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;main.py", file_cell_style),
     Paragraph("Interactive CLI (build/load/find/print/exit)", file_cell_style)],
    [Paragraph("tests/", file_cell_style),
     Paragraph("Unit test suite", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;test_crawler.py", file_cell_style),
     Paragraph("Crawler tests with mocked HTTP responses", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;test_indexer.py", file_cell_style),
     Paragraph("Indexer tests (tokenization, build, save/load)", file_cell_style)],
    [Paragraph("&nbsp;&nbsp;&nbsp;test_search.py", file_cell_style),
     Paragraph("Search tests (single/multi-word, edge cases)", file_cell_style)],
    [Paragraph("data/", file_cell_style),
     Paragraph("Generated index files (index.json + docs.json)", file_cell_style)],
]

files_table = Table(files_data, colWidths=[55*mm, 100*mm])
files_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#e8e8e8')),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(files_table)
story.append(Spacer(1, 4*mm))

# Commit history
story.append(Paragraph("Git Commit History (11 commits):", styles['SubHead']))
commits = [
    "57fb037 | May 03 | fix: convert JSON string keys to int on load",
    "c5d1bc9 | May 02 | docs: finalize for submission",
    "d4b4661 | May 01 | docs: GenAI declaration",
    "1b83cc3 | Apr 30 | feat: integrate all modules",
    "70b4873 | Apr 29 | chore: update requirements",
    "d134d18 | Apr 28 | docs: add README",
    "c5e3054 | Apr 27 | test: add unit tests",
    "e6eaf52 | Apr 23 | feat: implement CLI main loop",
    "a643e75 | Apr 22 | feat: implement search engine",
    "b7aadf2 | Apr 21 | feat: implement inverted indexer",
    "9c213ae | Apr 20 | feat: implement web crawler",
]
for c in commits:
    story.append(Paragraph(c, styles['CommitMono']))

# ── (C) Index File ──
story.append(Paragraph("(C) Index File (Inverted Index)", styles['SectionHead']))
story.append(Paragraph("File Name: <b>data/index.json</b> + <b>data/docs.json</b>", styles['InfoField']))
story.append(Paragraph("Description: Serialized inverted index generated by running the build command.", styles['InfoField']))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("<b>Index Structure:</b>", styles['InfoField']))

index_header_style = ParagraphStyle('IH', parent=styles['Normal'], fontSize=9, fontName='Helvetica-Bold')
index_cell_style = ParagraphStyle('IC', parent=styles['Normal'], fontSize=9, leading=13)

index_data = [
    [Paragraph("Component", index_header_style),
     Paragraph("Format", index_header_style),
     Paragraph("Details", index_header_style)],
    [Paragraph("index.json", index_cell_style),
     Paragraph("Dict[word &rarr; Dict[doc_id &rarr; List[pos]]]", index_cell_style),
     Paragraph("Positional inverted index (100 quotes indexed)", index_cell_style)],
    [Paragraph("docs.json", index_cell_style),
     Paragraph("List[{text, author, tags, url}]", index_cell_style),
     Paragraph("Full document storage from quotes.toscrape.com", index_cell_style)],
]

index_table = Table(index_data, colWidths=[35*mm, 60*mm, 60*mm])
index_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#e8e8e8')),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(index_table)
story.append(Spacer(1, 3*mm))
story.append(Paragraph(
    "Note: The index file will be attached separately on Minerva or included as a download link if too large.",
    styles['InfoField']
))

# ── Footer ──
story.append(Spacer(1, 8*mm))
story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#cccccc')))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(
    "<i>Submitted by Minhao Gao (201691058) &mdash; XJCO3011 Coursework 2: Search Engine Tool</i>",
    ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.grey, alignment=1)
))

# Build
doc.build(story)
print("PDF generated:", output_path)
