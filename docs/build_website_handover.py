from pathlib import Path
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "Sankofa_Digital_ZA_Website_Handover.docx"

BLACK = "000000"
GOLD = "D69516"
DARK = "202124"
PALE = "F5F1E8"
PALE_ALT = "F2F2F2"
WHITE = "FFFFFF"
GRAY = "666666"
BORDER = "D9D9D9"


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=120, start=130, bottom=120, end=130):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = borders.find(qn(f"w:{edge}"))
        if tag is None:
            tag = OxmlElement(f"w:{edge}")
            borders.append(tag)
        tag.set(qn("w:val"), "single")
        tag.set(qn("w:sz"), "5")
        tag.set(qn("w:space"), "0")
        tag.set(qn("w:color"), BORDER)


def set_repeat_table_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_run_font(run, name="Aptos", size=10.5, bold=False, color=BLACK):
    run.font.name = name
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), name)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), name)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run("Page ")
    set_run_font(run, size=8.5, color=GRAY)
    fld_char_1 = OxmlElement("w:fldChar")
    fld_char_1.set(qn("w:fldCharType"), "begin")
    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = " PAGE "
    fld_char_2 = OxmlElement("w:fldChar")
    fld_char_2.set(qn("w:fldCharType"), "end")
    run._r.append(fld_char_1)
    run._r.append(instr_text)
    run._r.append(fld_char_2)


def add_label(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(text.upper())
    set_run_font(run, name="Aptos Display", size=9, bold=True, color=GOLD)
    run.font.all_caps = True
    return p


def add_heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(16 if level == 1 else 12)
    p.paragraph_format.space_after = Pt(7)
    return p


def add_body(doc, text, bold_lead=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.12
    if bold_lead:
        run = p.add_run(bold_lead)
        set_run_font(run, bold=True)
    run = p.add_run(text)
    set_run_font(run)
    return p


def add_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.25)
        for run in p.runs:
            set_run_font(run)
        if not p.runs:
            run = p.add_run(item)
            set_run_font(run)
        else:
            p.runs[0].text = item


def add_table(doc, headers, rows, widths=None, font_size=9):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    header = table.rows[0]
    set_repeat_table_header(header)
    for index, text in enumerate(headers):
        cell = header.cells[index]
        set_cell_shading(cell, DARK)
        set_cell_margins(cell)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        set_run_font(run, size=font_size, bold=True, color=WHITE)
        if widths:
            cell.width = Inches(widths[index])
    for row_index, values in enumerate(rows):
        cells = table.add_row().cells
        for index, value in enumerate(values):
            cell = cells[index]
            set_cell_shading(cell, WHITE if row_index % 2 == 0 else PALE_ALT)
            set_cell_margins(cell)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            run = p.add_run(str(value))
            set_run_font(run, size=font_size, color=BLACK)
            if widths:
                cell.width = Inches(widths[index])
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return table


doc = Document()
section = doc.sections[0]
section.page_width = Inches(8.5)
section.page_height = Inches(11)
section.top_margin = Inches(0.72)
section.bottom_margin = Inches(0.66)
section.left_margin = Inches(0.78)
section.right_margin = Inches(0.78)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Aptos"
normal._element.rPr.rFonts.set(qn("w:ascii"), "Aptos")
normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos")
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor.from_string(BLACK)

title_style = styles["Title"]
title_style.font.name = "Aptos Display"
title_style._element.rPr.rFonts.set(qn("w:ascii"), "Aptos Display")
title_style._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos Display")
title_style.font.size = Pt(34)
title_style.font.bold = True
title_style.font.color.rgb = RGBColor.from_string(BLACK)

for style_name, size in (("Heading 1", 20), ("Heading 2", 14), ("Heading 3", 11.5)):
    style = styles[style_name]
    style.font.name = "Aptos Display"
    style._element.rPr.rFonts.set(qn("w:ascii"), "Aptos Display")
    style._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos Display")
    style.font.size = Pt(size)
    style.font.bold = True
    style.font.color.rgb = RGBColor.from_string(BLACK)

footer = section.footer
fp = footer.paragraphs[0]
fp.clear()
left = fp.add_run("Sankofa Digital ZA Website Handover")
set_run_font(left, size=8.5, color=GRAY)
fp.add_run("\t")
add_page_number(fp)

# Cover
add_label(doc, "Sankofa Digital ZA")
title = doc.add_paragraph(style="Title")
title.paragraph_format.space_before = Pt(80)
title.paragraph_format.space_after = Pt(14)
run = title.add_run("Sankofa Digital ZA Website Handover")
set_run_font(run, name="Aptos Display", size=34, bold=True, color=BLACK)
subtitle = doc.add_paragraph()
subtitle.paragraph_format.space_after = Pt(30)
run = subtitle.add_run("Business Website Content Design and Release Record")
set_run_font(run, name="Aptos Display", size=17, bold=True, color=GOLD)
add_body(doc, "This document records the business purpose, public content, visual system, enquiry behaviour, verification evidence and maintenance requirements for the Sankofa Digital ZA website.")
meta = doc.add_table(rows=4, cols=2)
meta.alignment = WD_TABLE_ALIGNMENT.LEFT
meta.autofit = False
set_table_borders(meta)
for idx, (label, value) in enumerate([
    ("Prepared for", "Sankofa Digital ZA"),
    ("Prepared on", "1 November 2026"),
    ("Website type", "Responsive multi page static business website"),
    ("Initial release", "Private Sites deployment for review"),
]):
    c1, c2 = meta.rows[idx].cells
    for cell in (c1, c2):
        set_cell_margins(cell, 115, 130, 115, 130)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    set_cell_shading(c1, PALE)
    r1 = c1.paragraphs[0].add_run(label)
    set_run_font(r1, size=9, bold=True)
    r2 = c2.paragraphs[0].add_run(value)
    set_run_font(r2, size=9)
doc.add_page_break()

# Contents
add_label(doc, "Document navigation")
add_heading(doc, "Contents", 1)
contents = [
    "1 Website Summary",
    "2 Site Architecture",
    "3 Portfolio Presentation",
    "4 Design and Interaction System",
    "5 Contact and Privacy Behaviour",
    "6 Verification and Release Record",
    "7 Maintenance and Approval",
]
for item in contents:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(9)
    run = p.add_run(item)
    set_run_font(run, name="Aptos Display", size=12, bold=True)
add_body(doc, "The website source and this handover should be reviewed together before any public launch. Product status, contact details and legal wording require approval when they change.")
doc.add_page_break()

# 1 Summary
add_label(doc, "Section 1")
add_heading(doc, "Website Summary", 1)
add_body(doc, "The website positions Sankofa Digital ZA as a South African product engineering studio serving organisations with operational, education, commerce and social-impact challenges. It uses verified workspace products as evidence and avoids unsupported delivery counts, testimonials and maturity claims.")
add_heading(doc, "Primary outcome", 2)
add_body(doc, "A prospective client should understand what the studio builds, see credible examples, learn how delivery works and start a structured enquiry through email or WhatsApp.")
add_heading(doc, "Approved positioning", 2)
add_table(doc, ["Decision", "Approved direction"], [
    ("Public brand", "Sankofa Digital ZA"),
    ("Audience", "South African organisations with complex operational, education, commerce or social-impact needs"),
    ("Offer", "Product engineering services supported by proprietary product work"),
    ("Commercial approach", "No generic public pricing; begin with a structured discovery conversation"),
    ("Initial access", "Private review deployment before any public audience change"),
], widths=[1.65, 5.2])
doc.add_page_break()

# 2 Architecture
add_label(doc, "Section 2")
add_heading(doc, "Site Architecture", 1)
add_body(doc, "The static multi-page structure gives each business question a clear destination while keeping the implementation lightweight and maintainable.")
add_table(doc, ["Page", "Purpose", "Primary action"], [
    ("Home", "Position the studio and introduce services, work and process", "Review work or start a conversation"),
    ("Services", "Explain six delivery capabilities and common engagement shapes", "Describe the operating problem"),
    ("Work", "Present five public-safe product summaries with status labels", "Assess relevant experience"),
    ("About", "Explain the Sankofa principle and studio standards", "Understand the working philosophy"),
    ("Process", "Show discovery through launch and the evidence left at each stage", "Understand delivery expectations"),
    ("Contact", "Prepare an enquiry for email or WhatsApp without website storage", "Send an enquiry through the chosen provider"),
    ("Privacy", "Explain data handling for the current static implementation", "Contact the studio about information rights"),
    ("Terms", "Define the informational and pre-contract nature of the website", "Confirm material claims when required"),
], widths=[1.0, 3.85, 2.0], font_size=8.5)
doc.add_page_break()

# 3 Portfolio
add_label(doc, "Section 3")
add_heading(doc, "Portfolio Presentation", 1)
add_body(doc, "Portfolio language is evidence-based and status-aware. Sensitive products are described only at the level needed to show relevant capability.")
add_table(doc, ["Product", "Public status", "Public story"], [
    ("Sankofa Computer Master Class", "Controlled pilot", "Guided NATED, CAT and certification learning paths with lecturer release controls and rollout checks"),
    ("NSC Maths Sankofa Portal", "Portal", "Student and lecturer flows connecting diagnosis, guided practice, roadmap and feedback"),
    ("Senatla Ops", "Internal platform", "Role-controlled operations records spanning field activity, assets, approvals and audit evidence"),
    ("Phekong Commerce Platform", "MVP", "Commerce, booking, inventory, seller tracking and business intelligence for a South African wellness brand"),
    ("Umkhuseli The Protector", "Evaluation product", "Privacy-conscious, low-data safety and evidence workflow concepts for South African conditions"),
], widths=[1.75, 1.25, 3.85], font_size=8.5)
add_heading(doc, "Publication limits", 2)
add_bullets(doc, [
    "Do not publish client credentials, learner records, employee information or private operational evidence.",
    "Do not present pilot, internal, MVP or evaluation work as a mature public production service.",
    "Do not add customer counts, project counts, ratings, testimonials or compliance guarantees without evidence and approval.",
    "Keep Umkhuseli wording informational and state that it does not replace emergency, medical or legal services.",
])
doc.add_page_break()

# 4 Design
add_label(doc, "Section 4")
add_heading(doc, "Design and Interaction System", 1)
add_body(doc, "The visual direction preserves the established black-and-gold Afrofuturist identity while reducing decorative noise. Large type, restrained motion and real product imagery support the business narrative.")
add_table(doc, ["Element", "Implementation"], [
    ("Palette", "Near-black backgrounds, warm white text and gold accents with high-contrast interactive states"),
    ("Typography", "Condensed display typography for headings and a system sans-serif stack for body copy"),
    ("Imagery", "Heritage-led hero artwork plus public-safe product screenshots and diagrams"),
    ("Motion", "Scroll reveals with a reduced-motion fallback"),
    ("Navigation", "Fixed desktop navigation and an accessible mobile menu with expanded-state reporting"),
    ("Responsive behaviour", "Single-column mobile layouts, touch-sized controls and no horizontal overflow at tested widths"),
], widths=[1.55, 5.3])
add_heading(doc, "Accessibility baseline", 2)
add_bullets(doc, [
    "Language, page titles, viewport metadata and main landmarks are present on every public page.",
    "Images include alternative text or intentionally empty alternatives for decorative marks.",
    "The site includes a keyboard-accessible skip link, labelled form controls and visible focus states.",
    "Animations respect the visitor's reduced-motion preference.",
])
doc.add_page_break()

# 5 Contact and privacy
add_label(doc, "Section 5")
add_heading(doc, "Contact and Privacy Behaviour", 1)
add_body(doc, "The enquiry form does not send data to a website database. It prepares a message in the visitor's email application or WhatsApp, and the visitor chooses whether to send it.")
add_table(doc, ["Item", "Current behaviour"], [
    ("Email", "sankofa.digital.studios@gmail.com"),
    ("Telephone and WhatsApp", "+27 75 465 4865"),
    ("Required enquiry fields", "Name, email, project type, project stage and problem description"),
    ("Website storage", "No account, CRM, database or form-submission storage"),
    ("Tracking", "No analytics, advertising or tracking cookies"),
    ("External processing", "Email and WhatsApp process messages only after the visitor chooses the relevant action"),
], widths=[1.7, 5.15])
add_heading(doc, "Change control", 2)
add_body(doc, "If the site later adds analytics, a server-side form, a CRM, booking tools or advertising, the privacy notice and consent design must be updated before release.")
doc.add_page_break()

# 6 Verification
add_label(doc, "Section 6")
add_heading(doc, "Verification and Release Record", 1)
add_body(doc, "The implementation received three review passes: source and claim review, automated static validation, and browser-based responsive verification.")
add_table(doc, ["Check", "Result"], [
    ("Static page validation", "Nine HTML files passed internal-link, asset, title, landmark, alternative-text and duplicate-ID checks"),
    ("Unsupported claim scan", "No placeholder client counts, delivery counts or testimonials remained"),
    ("Portfolio images", "All five portfolio headings loaded; referenced images reported no load failures"),
    ("Mobile layout", "All public pages matched viewport width without horizontal overflow"),
    ("Desktop layout", "All public pages matched viewport width without horizontal overflow"),
    ("Navigation", "Desktop current-page states and mobile expanded-state behaviour were verified"),
    ("Browser console", "No warnings or errors were reported during the route checks"),
], widths=[1.85, 5.0], font_size=8.5)
add_heading(doc, "Initial publication", 2)
add_body(doc, "The website is prepared for a private Sites deployment. A public audience change should occur only after content, contact and legal approval.")
doc.add_page_break()

# 7 Maintenance
add_label(doc, "Section 7")
add_heading(doc, "Maintenance and Approval", 1)
add_body(doc, "The website is intentionally buildless. Editors can update HTML, CSS and JavaScript without a framework build, but every material change should repeat the claim, link and responsive checks.")
add_heading(doc, "Prelaunch approval checklist", 2)
add_bullets(doc, [
    "Approve the public name Sankofa Digital ZA and the South African product-engineering positioning.",
    "Confirm the email address and telephone or WhatsApp number.",
    "Approve each portfolio product name, status label, screenshot and public description.",
    "Review the privacy notice and website terms for the intended public audience.",
    "Confirm whether the private Sites deployment may be changed to public access.",
    "Add a custom domain only after DNS ownership and launch responsibility are clear.",
])
add_heading(doc, "Routine update rule", 2)
add_body(doc, "When services, products or contact behaviour change, update the source, repeat automated validation, review desktop and mobile layouts, save a new Sites version and record the deployed URL.")
add_heading(doc, "Source location", 2)
add_body(doc, "The website source is stored in the workspace under sites/sankofa-digital-za. The deployment identity is recorded in .openai/hosting.json and the publishable static files are in dist.")

doc.core_properties.title = "Sankofa Digital ZA Website Handover"
doc.core_properties.subject = "Business website content design and release record"
doc.core_properties.author = "Sankofa Digital ZA"
doc.core_properties.keywords = "Sankofa Digital ZA website handover product engineering"
doc.settings.element.set(qn("w:updateFields"), "true")

OUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUT)
print(OUT)
