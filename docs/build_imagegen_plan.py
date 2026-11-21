from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "Sankofa_Digital_ZA_ImageGen_Website_Visual_Reset_Plan.docx"
INK = "171916"; GOLD = "C48A27"; PAPER = "F5F1E8"; LINE = "D9D4C8"; MUTED = "5D625A"

def font(run, name="Aptos", size=10.5, bold=False, color=INK):
    run.font.name = name; run.font.size = Pt(size); run.font.bold = bold; run.font.color.rgb = RGBColor.from_string(color)
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), name); run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), name)

def shade(cell, color):
    pr = cell._tc.get_or_add_tcPr(); node = OxmlElement("w:shd"); node.set(qn("w:fill"), color); pr.append(node)

def margins(cell, value=120):
    pr = cell._tc.get_or_add_tcPr(); mar = OxmlElement("w:tcMar")
    for side in ("top", "start", "bottom", "end"):
        node = OxmlElement(f"w:{side}"); node.set(qn("w:w"), str(value)); node.set(qn("w:type"), "dxa"); mar.append(node)
    pr.append(mar)

def borders(table):
    pr = table._tbl.tblPr; b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        n = OxmlElement(f"w:{edge}"); n.set(qn("w:val"), "single"); n.set(qn("w:sz"), "5"); n.set(qn("w:color"), LINE); b.append(n)
    pr.append(b)

def heading(doc, text, level=1):
    p = doc.add_heading(text, level=level); p.paragraph_format.keep_with_next = True; return p

def body(doc, text, color=INK):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(7); p.paragraph_format.line_spacing = 1.12
    r = p.add_run(text); font(r, color=color); return p

def label(doc, text):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(5); r = p.add_run(text.upper()); font(r, name="Aptos Display", size=8.5, bold=True, color=GOLD); return p

def remove_paragraph_borders(paragraph):
    ppr = paragraph._p.get_or_add_pPr()
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is not None:
        ppr.remove(pbdr)

def bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet"); p.paragraph_format.space_after = Pt(3); r = p.add_run(item); font(r)

def table(doc, headers, rows, widths):
    t = doc.add_table(rows=1, cols=len(headers)); t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.autofit = False; borders(t)
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; shade(c, INK); margins(c); c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER; c.width = Inches(widths[i]); r = c.paragraphs[0].add_run(h); font(r, size=9, bold=True, color="FFFFFF")
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, value in enumerate(row):
            c = cells[i]; shade(c, "FFFFFF" if ri % 2 == 0 else "F1F0EB"); margins(c); c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER; c.width = Inches(widths[i]); r = c.paragraphs[0].add_run(value); font(r, size=9)
    doc.add_paragraph().paragraph_format.space_after = Pt(0); return t

doc = Document(); sec = doc.sections[0]; sec.top_margin = Inches(.7); sec.bottom_margin = Inches(.65); sec.left_margin = Inches(.78); sec.right_margin = Inches(.78)
styles = doc.styles; styles["Normal"].font.name = "Aptos"; styles["Normal"].font.size = Pt(10.5); styles["Normal"].font.color.rgb = RGBColor.from_string(INK)
for s, size in (("Title", 30), ("Heading 1", 19), ("Heading 2", 13)):
    styles[s].font.name = "Aptos Display"; styles[s].font.size = Pt(size); styles[s].font.bold = True; styles[s].font.color.rgb = RGBColor.from_string(INK)
title_ppr = styles["Title"]._element.get_or_add_pPr(); title_pbdr = title_ppr.find(qn("w:pBdr"))
if title_pbdr is not None:
    title_ppr.remove(title_pbdr)

label(doc, "Sankofa Digital ZA")
p = doc.add_paragraph(style="Title"); remove_paragraph_borders(p); p.paragraph_format.space_before = Pt(56); p.paragraph_format.space_after = Pt(12); r = p.add_run("Website Visual Reset Plan"); font(r, name="Aptos Display", size=30, bold=True)
p = doc.add_paragraph(); r = p.add_run("A concise redesign direction for bespoke studio positioning and ImageGen-supported visual storytelling"); font(r, name="Aptos Display", size=15, bold=True, color=GOLD)
body(doc, "The current site has a strong identity but asks visitors to process too much explanation before they can understand the offer. This plan reduces the homepage to a proof-led studio story and defines where generated imagery will help without replacing real product evidence.", color=MUTED)
doc.add_paragraph(); table(doc, ["Decision", "Direction"], [("Primary shift", "From manifesto-heavy dark interface to editorial product engineering studio"), ("Homepage job", "Explain the offer, show credible work, invite a conversation"), ("ImageGen role", "Create atmosphere and context around workflows; never fabricate proof")], [1.5, 5.25])
doc.add_page_break()

label(doc, "Contents"); heading(doc, "Contents", 1)
for item in ["1 The problem", "2 New homepage journey", "3 Visual direction", "4 ImageGen asset briefs", "5 Copy and implementation rules", "6 Three-pass acceptance test"]:
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(6); r = p.add_run(item); font(r, name="Aptos Display", size=12, bold=True)
doc.add_page_break()

label(doc, "Section 1"); heading(doc, "The problem", 1)
body(doc, "The homepage currently combines manifesto copy, a compiler demo, a comparison matrix, six service cards, philosophy, process, roots, and case studies. The result is distinctive but cognitively expensive. It can make a custom studio look like a technical encyclopedia instead of a team that can understand and solve a client workflow.")
heading(doc, "What changes", 2)
bullets(doc, ["Keep the Sankofa identity, but let the work carry more of the argument.", "Move long philosophy, the compiler demo, and detailed capability explanations to About or Process.", "Show three selected projects with status labels and one-sentence evidence.", "Use fewer sections, fewer borders, fewer gradients, and more visual breathing room."])

label(doc, "Section 2"); heading(doc, "New homepage journey", 1)
table(doc, ["Step", "Content job", "Limit"], [("Hero", "One clear promise, one CTA, one strong visual", "12-word headline; 24-word support"), ("Proof bar", "Custom platforms, mobile-first delivery, clear ownership", "Three signals"), ("Work", "Three case studies with status and evidence", "One sentence per card"), ("Offer", "Discover the system, build the product, support handover", "Three capability groups"), ("Process", "Four steps with tangible outputs", "Short labels plus outputs"), ("Close", "Invite the visitor to bring a real workflow", "One direct CTA")], [1.0, 4.6, 1.15])

doc.add_page_break(); heading(doc, "Visual direction", 1)
body(doc, "Shift from “Wikipedia in dark mode” to an editorial product engineering studio. Keep black and warm gold as accents, while introducing warm paper, clay, muted olive, and daylight neutrals. Use large type, generous whitespace, restrained motion, and imagery that shows operating context rather than abstract technology theatre.")
table(doc, ["Keep", "Reduce"], [("Sankofa mark, black and gold accents, real product screenshots, African context", "Neon gradients, terminal theatre, repeated sovereignty language, long paragraphs"), ("Evidence-led case-study labels and clear ownership language", "Guarantees, unsupported metrics, anonymous testimonials, invented client proof")], [3.25, 3.5])

label(doc, "Section 4"); heading(doc, "ImageGen asset briefs", 1)
body(doc, "Use the built-in ImageGen tool one asset at a time. These briefs are generation-ready directions, not a request to generate assets in this planning pass. Keep logos, icons, UI screenshots, and factual diagrams code-native.")
heading(doc, "Hero visual", 2); body(doc, "Use case: photorealistic-natural. Asset type: 16:9 website hero. Editorial documentary image of a South African product team working around a table with printed workflow maps, a rugged laptop, a phone, and handwritten notes; warm daylight, tactile materials, quiet confidence, generous negative space on the left for headline copy, no logos, no readable screen text, no watermark.")
heading(doc, "Workflow transition", 2); body(doc, "Use case: stylized-concept. Asset type: 4:3 section illustration. Art-directed still life showing a messy operational workflow becoming a clean digital system: layered paper cards, route lines, abstract phone shapes, and a small gold Sankofa-inspired curve; warm paper, charcoal ink, muted olive and gold, no readable text, no logo, no watermark.")
heading(doc, "Case-study family", 2); body(doc, "Create consistent variants for education, operations, and commerce. Keep faces secondary; make the workflow and product context the subject. Do not invent client logos, testimonials, metrics, or private records.")

doc.add_page_break(); label(doc, "Section 5"); heading(doc, "Copy and implementation rules", 1)
bullets(doc, ["Hero headline: maximum 12 words. Supporting copy: maximum 24 words.", "Section introductions: maximum 35 words. Cards: one sentence plus a status label.", "Prefer “purpose-built for your workflow” over abstract engineering language when clarity is the goal.", "Generate the hero visual first and test it at mobile width before generating the rest.", "Check 375px, 768px, and 1440px widths; provide descriptive alt text and mobile-appropriate file sizes."])
heading(doc, "Guardrails", 2)
bullets(doc, ["Never use generated images as client evidence or as a substitute for actual product screenshots.", "Do not fabricate people, logos, records, customer counts, testimonials, or performance claims.", "Do not present pilot, internal, MVP, or evaluation work as a mature public production service.", "If an image does not clarify the offer, remove it."])

label(doc, "Section 6"); heading(doc, "Three-pass acceptance test", 1)
table(doc, ["Pass", "Question"], [("Comprehension", "Can a visitor explain what Sankofa builds and who it helps after the first screen?"), ("Credibility", "Does every visual reinforce a real capability or published project boundary?"), ("Conversion", "Can a mobile visitor reach a case study or start an enquiry in under one minute?")], [1.35, 5.4])
body(doc, "Success means the website feels like a bespoke studio showing its work, not a manifesto asking the visitor to study it.", color=MUTED)
doc.core_properties.title = "Sankofa Digital ZA Website Visual Reset Plan"; doc.core_properties.author = "Sankofa Digital ZA"; doc.core_properties.subject = "Website redesign and ImageGen asset direction"
OUT.parent.mkdir(parents=True, exist_ok=True); doc.save(OUT); print(OUT)
