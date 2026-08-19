#!/usr/bin/env python3
"""Build the slide deck for
   Creating Stunning Print and Digital Publications with InDesign (TGS-2021007827).

House style: all-white Tertiary Infotech deck. Every teaching slide is a visual
component — tile grid, process map, comparison matrix, screenshot-with-explanation
or generated concept diagram. NO step-by-step procedures on the slides: the detailed
steps live in the Learner Guide, per the course brief. The deck shows WHAT and WHY;
the LG shows HOW.

Images come from two libraries, both placed on real slides:
  courseware/assets/screens/  — the 106 screenshots imported from the original deck
  courseware/assets/gen/      — the 10 generated concept diagrams (make_graphics.py)

Run:  python3 build_slides.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from engine import *                      # templates, palette, prs, REPO, helpers
import engine
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3

# Lab -> the source artwork shown on its case-study slide (imported from the old deck)
LAB_IMG = {
    1:"act_masterpage", 2:"start_workspace", 3:"act_masterpage", 4:"act_grids",
    5:"act_textframe", 6:"act_threading", 7:"act_path", 8:"pen_curves",
    9:"pathfinder_panel", 10:"act_colour", 11:"transparency_effects", 12:"act_layers",
    13:"act_typepath", 14:"act_dropcap", 15:"nested_styles", 16:"act_table",
    17:"act_hyperlink", 18:"act_animation", 19:"preflight_gate", 20:"act_epub",
}

# ============================================================ BUILD
cover()

# ---------------------------------------------------------------- ADMIN (front)
section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

tile_grid("Digital Attendance (Mandatory)", [
 ("Three times today", "Take the AM, PM and Assessment digital attendance — mandatory for every WSQ-funded course."),
 ("Trainer shows the QR", "The trainer or administrator displays the digital attendance QR code from the SSG portal."),
 ("Scan and submit", "Scan the QR code with your mobile phone camera and submit your attendance."),
 ("75% minimum", "A minimum of 75% attendance is required to be eligible for assessment and funding.")],
 kicker="TRAQOM · SSG DIGITAL ATTENDANCE", cols=2, size=15)

trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
 "General Trainer template —\nto be completed by the trainer",
 [("Name",""),("Title / Designation",""),("Qualifications",""),
  ("Areas of expertise",""),("Training & industry experience",""),("Contact","")],
 initials="?", accent=GREY)

trainer_slide("YOUR TRAINER", C.TRAINER,
 "Principal Trainer\nTertiary Infotech Academy Pte Ltd",
 [("Role","Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
  ("Expertise","Adobe Creative Cloud for print and digital publishing — InDesign, Photoshop and Illustrator."),
  ("Delivers","WSQ courses in digital design, page layout production and creative technologies."),
  ("Founder","Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
 initials="AA", accent=BLUE)

tile_grid("Let's Know Each Other", [
 ("Who you are", "Your name, your organisation and the role you play there."),
 ("Your experience", "How much you have used Adobe InDesign, Photoshop or Illustrator — if at all."),
 ("What you produce", "The publications you need to make at work: brochures, magazines, reports, e-books?"),
 ("Your goal for today", "One thing you would like to be able to do by the time you leave.")],
 kicker="ICE-BREAKER", cols=2, size=15, accent=TEAL)

tile_grid("Ground Rules", [
 "Set your mobile phone to silent mode.", "Participate actively — no question is too small.",
 "Mutual respect: agree to disagree.", "One conversation at a time.",
 "Be punctual; return from breaks on time.", "75% attendance is required."],
 kicker="HOUSEKEEPING", cols=2, size=15)

image_explain("Download Your Course Material", "lms_portal", [
 ("1 · Go to the LMS portal", "Open https://lms-tms.tertiaryinfotech.com in your browser."),
 ("2 · Log in", "Sign in with the account e-mail you used to register for this course."),
 ("3 · Open this course", "Select 'Creating Stunning Print and Digital Publications with InDesign'."),
 ("4 · Download", "Take the Trainer Slides, Learner Guide and Lesson Plan (PDF)."),
 ("5 · Get the lab files", "Download the InDesign lab files — you need them from Lab 1 onwards."),
 ("6 · Keep them open", "You may use these materials during the open-book assessment.")],
 kicker="LMS / TMS  ·  lms-tms.tertiaryinfotech.com", accent=BLUE)

tile_grid("Skills Framework Alignment", [
 ("TSC Title", C.TSC_TITLE),
 ("TSC Code", C.TSC_CODE)] +
 [(f"{k} · Ability", v) for k, v in C.TSC_ABILITIES],
 kicker="SKILLS FRAMEWORK  ·  TSC", cols=2, size=13, accent=VIOLET)

tile_grid("Underpinning Knowledge", [(f"{k}", v) for k, v in C.TSC_KNOWLEDGE],
 kicker=f"TSC KNOWLEDGE  ·  {C.TSC_CODE}", cols=1, size=14, accent=VIOLET)

tile_grid("Learning Outcomes", [(t, b) for t, b in C.LEARNING_OUTCOMES_LONG],
 kicker="WHAT YOU'LL ACHIEVE", cols=1, size=14)

tile_grid("Course Outline", [
 ("Topic 1 — Get Started on InDesign",
  "Establish drawing & layout requirements · the interface · create documents · parent pages · grids and guides."),
 ("Topic 2 — Basic InDesign Drawing Techniques",
  "Text and threading · frames and paths · graphics and links · colour, gradients and effects · transform, align, layers."),
 ("Topic 3 — Refine InDesign Drawings",
  "Typography and type on a path · paragraph, character and object styles · tables · interactivity · preflight, package and export.")],
 kicker="THREE TOPICS  ·  20 HANDS-ON ACTIVITIES", cols=1, size=15)

two_col("Lesson Plan — 1 Day, 8 Instructional Hours", [
 ("Morning — 9:30am to 1:00pm", 0),
 ("Digital Attendance (AM) · Introductions · Learning Outcomes", 1),
 ("Topic 1: Get Started on InDesign (Activities 1–4)", 1),
 ("Tea break — 11:00am", 1),
 ("Topic 2: Basic InDesign Drawing Techniques begins (Activities 5–8)", 1),
 ("Lunch Break — 1:00pm to 2:00pm", 1)],
 [("Afternoon — 2:00pm to 6:30pm", 0),
 ("Digital Attendance (PM)", 1),
 ("Topic 2 continues (Activities 9–12)", 1),
 ("Topic 3: Refine InDesign Drawings (Activities 13–20)", 1),
 ("Tea break — 3:45pm", 1),
 ("TRAQOM Survey · Digital Attendance (Assessment)", 1),
 ("Final Assessment: PP (75 min) + OQ (15 min)", 1)],
 kicker="SCHEDULE", lhead="Morning", rhead="Afternoon")

tile_grid("Briefing for Assessment", [
 ("Do · Clear your desk", "Place phones and other materials under the table or on the floor."),
 ("Don't · No recording", "No photos or recording of assessment scripts."),
 ("Don't · No discussion", "Work individually — no discussion during the assessment."),
 ("Do · Black or blue pen", "Use a black or blue pen for hard-copy assessments."),
 ("Don't · No correction fluid", "No liquid paper or correction tape may be used."),
 ("Do · Stop on time", "Scripts are collected when time is up.")],
 kicker="BEFORE YOU START", cols=2, size=14, accent=AMBER)

tile_grid("Assessment", [
 ("Practical Performance (PP)", "Hands-on InDesign layout tasks · 75 minutes · open book. Assesses abilities A1–A4."),
 ("Oral Questioning (OQ)", "Five questions, one-to-one with the assessor · 15 minutes · open book. Assesses knowledge K1–K3."),
 ("Open book", "You may use the course slides, the Learner Guide and approved materials only."),
 ("Eligibility", "A minimum of 75% attendance is required to be eligible for assessment and funding."),
 ("Result", "You are assessed as Competent (C) or Not Yet Competent (NYC) on every A and K. One NYC means NYC for the unit."),
 ("Appeals", "An appeal process is available if you wish to contest an assessment outcome.")],
 kicker="FINAL ASSESSMENT", cols=2, size=14)

compare_table("The Two Assessment Instruments",
 ["", "Practical Performance (PP)", "Oral Questioning (OQ)"],
 [["What it assesses", "Abilities A1–A4 — what you can DO", "Knowledge K1–K3 — what you UNDERSTAND"],
  ["Duration", "75 minutes", "15 minutes"],
  ["Format", "Hands-on InDesign layout tasks", "Five questions, one-to-one with the assessor"],
  ["You submit", "Your InDesign document plus screenshots of each task", "Your spoken answers, recorded by the assessor"],
  ["Conditions", "Individual · summative · open book", "Individual · summative · open book"]],
 kicker="HOW YOU ARE ASSESSED", accent=VIOLET,
 note="You must be assessed Competent on EVERY ability and EVERY knowledge statement. A single NYC makes the whole unit NYC, and the entire assessment must be re-taken.")

process_map("Assessment Flow", [
 ("TRAQOM survey", "Scan the LMS QR code"),
 ("Digital attendance", "Scan the SSG assessment QR"),
 ("Sit the PP", "75 minutes · open book"),
 ("Answer the OQ", "15 minutes · one-to-one"),
 ("Sign the record", "Sign the Summary Record")],
 kicker="ON ASSESSMENT DAY", color=BLUE,
 synthesis=("REMEMBER", "All five steps are mandatory for WSQ funding — missing the digital attendance or the TRAQOM survey can invalidate your claim."))

tile_grid("Criteria for Funding", [
 ("Attendance", "A minimum attendance rate of 75%, based on the SSG Digital Attendance record."),
 ("Assessment", "Complete both assessment components and be assessed as 'Competent'."),
 ("Digital attendance", "Scan the SSG QR code for AM, PM and Assessment on the training day."),
 ("TRAQOM survey", "Complete the mandatory TRAQOM course feedback survey on the LMS.")],
 kicker="WSQ FUNDING", cols=2, size=15, accent=AMBER)

tile_grid("Set Up Before We Start", [
 ("Adobe InDesign", "InDesign 2024 or later, launched and signed in to your Creative Cloud account."),
 ("Lab files", "Download the course lab files from the LMS and unzip them to your desktop."),
 ("Units", "We work in millimetres — Singapore print practice. We set this in Activity 1."),
 ("Adobe Fonts", "Sign in so missing fonts auto-activate; otherwise fonts show pink highlighting."),
 ("A mouse", "Precision work with the Pen tool is far easier with a mouse than a trackpad."),
 ("Save often", "Ctrl/Cmd+S. InDesign auto-recovers, but a saved file is a safe file.")],
 kicker="LAB ENVIRONMENT", cols=2, size=14, accent=TEAL)

# ---------------------------------------------------------------- WHY INDESIGN
section("CORE CONCEPTS", "Why InDesign, and What It Is For", "")

image_gallery("What You Can Make with InDesign",
 ["showcase_brochure_a", "showcase_brochure_b", "showcase_flyer_a",
  "showcase_flyer_b", "showcase_epub", "act_table"],
 ["Brochures", "Corporate collateral", "Flyers and promotions",
  "Posters and campaigns", "EPUB e-books", "Data-driven catalogues"],
 kicker="ONE TOOL  ·  PRINT AND DIGITAL", cols=3)

tile_grid("What Adobe InDesign Is", [
 ("Page layout, not image editing", "InDesign assembles type, photographs and vector artwork into a precisely specified, production-ready publication."),
 ("Print and digital from one file", "The same layout exports as a press-ready PDF/X, an interactive PDF, an EPUB e-book or a web page."),
 ("Built for multi-page work", "Parent pages, styles, sections, books and automatic numbering are what set it apart from Word, Canva or Illustrator."),
 ("Precise typographic control", "Kerning, tracking, optical margin alignment and a baseline grid — the details that make a page look professionally set."),
 ("Tightly integrated", "Round-trips with Photoshop, Illustrator and Acrobat; placed assets stay linked and update automatically."),
 ("The industry standard", "Publishers, agencies and print houses in Singapore and worldwide expect InDesign files.")],
 kicker="THE LAYOUT APPLICATION", cols=2, size=14)

image_full("Which Application Owns Which Job?", "app_roles",
 kicker="CREATIVE CLOUD WORKFLOW",
 caption="Pixels in Photoshop · vectors in Illustrator · the page in InDesign. Placed assets stay linked, so an edit upstream updates the layout.",
 accent=AMBER)

compare_table("InDesign vs the Alternatives",
 ["Capability", "InDesign", "Illustrator", "Word / Canva"],
 [["Multi-page publications", "Built for it — parent pages, sections, books", "One artboard at a time", "Basic, no production control"],
  ["Typographic control", "Full — kerning, baseline grid, optical margins", "Good, but per-object", "Limited"],
  ["Styles that cascade", "Paragraph, character, object, table, cell", "Character & paragraph only", "Basic paragraph styles"],
  ["Print production", "Preflight, package, PDF/X, spot colours, bleed", "Partial", "Not press-ready"],
  ["Digital output", "EPUB, interactive PDF, Publish Online", "SVG, web assets", "PDF only"]],
 kicker="CHOOSING THE RIGHT TOOL", accent=BLUE,
 note="A three-page flyer can be done anywhere. A 96-page catalogue with a price table, a house style and a printer's specification can only be done properly in InDesign.")

# ---------------------------------------------------------------- TOPICS
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}
CARD_COLORS = [BLUE, TEAL, VIOLET]

# Extra visual teaching slides injected per topic, keyed by topic number.
# These carry the imported screenshots and the generated concept diagrams.
def topic1_visuals():
    image_full("Anatomy of a Print Page", "page_anatomy",
     kicker="ESTABLISH THE REQUIREMENT",
     caption="Trim, bleed, margin and slug are the four numbers every printer asks for. Confirm them in writing before you create the file.",
     accent=TEAL)
    image_full("Colour Mode Follows the Output", "colour_modes",
     kicker="ESTABLISH THE REQUIREMENT",
     caption="CMYK for ink on paper, RGB for light on a screen. The Intent you pick in New Document sets this for the whole document.",
     accent=BLUE)
    image_full("Resolution Follows the Medium", "resolution_ladder",
     kicker="SELECT THE RIGHT MEDIUM",
     caption="Effective PPI — what the image measures after you scale it in InDesign — is what actually prints. Check it in the Links panel.",
     accent=VIOLET)
    tile_grid("Reading a Client Brief", [
     ("What is stated", "Size, orientation, quantity, stock, print process, finishing, delivery date."),
     ("What is assumed", "Bleed, margins, colour mode and resolution are usually left out — you must confirm them."),
     ("Who decides", "The printer's specification governs. Ask for it, in writing, before you begin."),
     ("What it costs", "A wrong trim size or a missing bleed is discovered at the press — after you have paid for plates."),
     ("Document it", "A one-page specification sheet, signed off by the client, protects you and the job."),
     ("Then build", "Only when the specification is agreed do you open the New Document dialog.")],
     kicker="A1 · ESTABLISH DRAWING REQUIREMENTS", cols=2, size=14, accent=TEAL)
    image_explain("The Start Workspace", "start_workspace", [
     ("Recent files", "Reopen the job you were working on yesterday without hunting through folders."),
     ("New / Open", "Start a document from a preset, a template, or open an existing one."),
     ("Adobe Stock templates", "Professionally built starting points for letterheads, cards, magazines and social assets."),
     ("Learn", "Built-in hands-on tutorials that open as real InDesign documents.")],
     kicker="TOPIC 01 · THE INTERFACE", accent=BLUE)
    image_explain("The New Document Dialog", "new_document_dialog", [
     ("Intent", "Print, Web or Mobile — this sets colour mode, units and the transparency blend space."),
     ("Size and orientation", "The trim size. Type the exact millimetres from your specification sheet."),
     ("Facing pages", "On for anything bound as a spread; off for a single-sided flyer or a poster."),
     ("Margins, columns, gutter", "The text area and its structure. Change it later with Layout > Margins and Columns."),
     ("Bleed and slug", "Expand this section — bleed defaults to 0 and a printer will reject that.")],
     kicker="TOPIC 01 · CREATE THE DOCUMENT", accent=BLUE,
     lead="Every field here comes straight off the specification sheet you agreed in Activity 1.")
    image_full("The InDesign Workspace", "workspace_map",
     kicker="TOPIC 01 · THE INTERFACE",
     caption="Save your own panel arrangement with Window > Workspace > New Workspace so every job starts in the same, fast environment.",
     accent=BLUE)
    image_full("Frame and Content Are Two Different Things", "frame_content",
     kicker="TOPIC 01 · THE TWO SELECTION TOOLS",
     caption="Black arrow (V) selects the frame. White arrow (A) selects what is inside it. Almost every beginner problem starts here.",
     accent=TEAL)
    image_explain("Parent Pages", "apply_master", [
     ("A reusable background", "Running heads, folios, footers and repeating logos live on the parent, not on each page."),
     ("Change once, update everywhere", "Edit the parent and every page based on it updates automatically."),
     ("Apply by dragging", "Drag the parent icon onto a page, or onto a spread corner, in the Pages panel."),
     ("Override deliberately", "Ctrl/Cmd+Shift+click releases a single parent item on one page when you genuinely need to.")],
     kicker="TOPIC 01 · MANAGE PAGES", accent=VIOLET)
    image_explain("Automatic Page Numbering", "page_number_marker", [
     ("Insert a marker, not digits", "Type > Insert Special Character > Markers > Current Page Number."),
     ("It shows as 'A'", "On the parent it displays the parent's prefix; on document pages it shows the real number."),
     ("It re-flows", "Insert, delete or reorder pages and every folio corrects itself."),
     ("Sections", "Layout > Numbering & Section Options gives roman front matter and arabic body matter in one file.")],
     kicker="TOPIC 01 · MANAGE PAGES", accent=VIOLET)
    image_explain("Grids, Guides and the Modular Grid", "create_guides_dialog", [
     ("Baseline grid", "Locks body text to a common rhythm so columns line up across the spread."),
     ("Document grid", "Graph-paper alignment for objects, set in Preferences > Grids."),
     ("Ruler guides", "Drag from a ruler. On the page = page guide; from the pasteboard = spread guide."),
     ("Layout > Create Guides", "Builds a full rows-and-columns modular grid, with gutters, in one dialog."),
     ("None of it prints", "Guides are the invisible skeleton — they structure the page but never appear on it.")],
     kicker="TOPIC 01 · STRUCTURE THE PAGE", accent=TEAL)
    image_explain("Adjust Layout — the Productivity Feature", "adjust_layout_dialog", [
     ("The problem", "The client changes the page size or the printer changes the margin — and every element is now wrong."),
     ("The old way", "Re-position every object on every page by hand. Hours or days of work."),
     ("File > Adjust Layout", "InDesign re-flows the existing elements to the new page size, margins or bleed automatically."),
     ("Then review", "It is a very good first pass, not a final answer — check each spread and correct the balance.")],
     kicker="TOPIC 01 · A1 / A4  ·  REFINE TO REQUIREMENT", accent=AMBER)

def topic2_visuals():
    image_full("Threading: One Story, Many Frames", "threading",
     kicker="TOPIC 02 · TEXT",
     caption="A red + in the out port means overset text — copy that exists in the story but has nowhere to sit. It never prints.",
     accent=BLUE)
    image_explain("Four Ways to Flow Text", "flow_text_methods", [
     ("Click", "Manual — one frame at a time. Full control, slow for long copy."),
     ("Shift-click · Autoflow", "Adds frames AND pages until the whole story is placed. A 40-page import in one click."),
     ("Alt/Opt-click · Semi-autoflow", "Places one frame and keeps the cursor loaded for the next."),
     ("Shift+Alt/Opt · Fixed-page", "Fills the existing pages only; never adds new ones."),
     ("Smart Text Reflow", "Preferences > Type — adds and removes pages automatically as the story grows or shrinks.")],
     kicker="TOPIC 02 · TEXT", accent=BLUE)
    image_explain("Placing Graphics and the Links Panel", "act_path", [
     ("Placed, not embedded", "File > Place creates a LINK to the original file — the layout stays light and the asset stays editable."),
     ("The Links panel is production control", "Status, effective PPI, colour space, scale and page for every asset in the job."),
     ("Missing = red · Modified = yellow", "A missing link at output means a blank or low-res box on the printed page."),
     ("Frame fitting", "Fill Frame Proportionally, Fit Content Proportionally, Content-Aware Fit — set it before you place."),
     ("The Content Grabber", "The doughnut in the middle of a frame grabs the image inside without moving the frame.")],
     kicker="TOPIC 02 · GRAPHICS", accent=TEAL)
    image_pair("Paths: Anchor Points and Direction Handles",
     ["paths_anchor", "direction_handles"],
     ["A path is points joined by segments", "Direction handles shape the curve"],
     kicker="TOPIC 02 · FRAMES AND PATHS", accent=VIOLET,
     note="The angle and length of the direction lines determine the shape and size of the adjoining curve segments. This is the single most transferable vector skill in design.")
    image_pair("Drawing with the Pen Tool",
     ["pen_straight", "pen_curves"],
     ["Click = corner point, straight segment", "Click-drag = smooth point, curve"],
     kicker="TOPIC 02 · FRAMES AND PATHS", accent=VIOLET,
     note="Click for corners, drag for curves. Alt/Option-drag a handle to break the symmetry and go from a curve straight into a corner.")
    image_explain("Compound Paths and the Pathfinder", "pathfinder_panel", [
     ("Compound path", "Object > Paths > Make Compound Path punches a transparent hole through a shape."),
     ("Add", "Merges the selected shapes into one outline."),
     ("Subtract", "Removes the front shapes from the backmost one."),
     ("Intersect", "Keeps only the overlapping area."),
     ("Exclude Overlap", "Keeps everything except the overlap — the classic doughnut."),
     ("Minus Back", "Removes the back shapes from the frontmost one.")],
     kicker="TOPIC 02 · FRAMES AND PATHS", accent=VIOLET)
    image_explain("Clipping Paths and Text Wrap", "clipping_detect_edges", [
     ("Silhouette an image", "Object > Clipping Path > Detect Edges removes a plain background with no alpha channel."),
     ("Better: use the alpha", "A PSD saved with transparency or a path gives a far cleaner edge than Detect Edges."),
     ("Then wrap the text", "The Text Wrap panel pushes body copy around the silhouette, not the rectangular frame."),
     ("Wrap around object shape", "This is the setting that makes a magazine page look professionally composed.")],
     kicker="TOPIC 02 · FRAMES AND PATHS", accent=TEAL)
    image_explain("Colour: Swatches, Spot and Process", "colour_picker", [
     ("Stroke and fill", "Colour applies to the border (stroke) or the interior (fill) of any object, and to text."),
     ("Name your swatches", "A named swatch is global — edit it once and every object using it updates."),
     ("Process (CMYK)", "Built from four inks. The default for full-colour print."),
     ("Spot (Pantone)", "A pre-mixed ink for brand-critical colour. Each spot colour is an extra plate and an extra cost."),
     ("Unnamed colours", "Mixing straight in the Colour panel is why files reach the printer with forty near-identical blues.")],
     kicker="TOPIC 02 · COLOUR", accent=AMBER)
    image_pair("Colour Themes and Gradients",
     ["colour_theme_tool", "gradients"],
     ["Colour Theme tool — extract a palette from any image", "Gradients — linear and radial blends"],
     kicker="TOPIC 02 · COLOUR", accent=AMBER,
     note="The Colour Theme tool is the fastest professional route from a client's photograph to a coherent, harmonious palette added straight into Swatches.")
    image_explain("Transparency, Blending Modes and Effects", "effects_panel", [
     ("Applied per level", "Object, stroke, fill or text — each can carry its own opacity and effect."),
     ("Blending modes", "Multiply, Screen, Overlay and the rest control how a colour interacts with what is beneath it."),
     ("Nine effects", "Drop shadow, inner shadow, outer and inner glow, bevel & emboss, satin, and three feathers."),
     ("Use with restraint", "One considered shadow reads as design; five competing effects read as a beginner's page."),
     ("Print warning", "Transparency must be flattened for PDF/X-1a. Check with Window > Output > Flattener Preview.")],
     kicker="TOPIC 02 · COLOUR AND EFFECTS", accent=AMBER)
    image_explain("Transform: Move, Scale, Rotate, Shear, Reflect", "scale_objects", [
     ("Never by eye", "Type exact X/Y and W/H values in the Control panel, against a chosen reference point."),
     ("The reference point matters", "The little 9-point proxy decides which corner stays fixed as you transform."),
     ("Scale frame + content", "Hold Ctrl/Cmd with the Selection tool; add Shift to keep it proportional."),
     ("Shear and reflect", "Object > Transform, or the Shear tool, for numeric precision rather than dragging."),
     ("Smart Guides", "Live green feedback showing alignment, equal spacing and matching dimensions as you drag.")],
     kicker="TOPIC 02 · MANAGE OBJECTS", accent=BLUE)
    image_explain("Align, Distribute and Layers", "align_panel", [
     ("Align to what?", "Selection, margins, page or spread — the dropdown changes the whole result."),
     ("Distribute spacing", "Equal gaps between objects, which is not the same as equal centres."),
     ("Layers are sheets", "Stacking, visibility, locking and printing controlled as a group."),
     ("Name your layers", "Background, images, text, notes. It is how another designer can open your file and work in it."),
     ("Non-printing layers", "Put client notes and guides on a layer set not to print.")],
     kicker="TOPIC 02 · MANAGE OBJECTS", accent=TEAL)

def topic3_visuals():
    image_pair("Type on a Path",
     ["type_on_path_a", "path_type_effects"],
     ["Text flows along any open or closed path", "Rainbow · Skew · 3D Ribbon · Stair Step · Gravity"],
     kicker="TOPIC 03 · TYPOGRAPHY", accent=BLUE,
     note="On a tight curve, characters fan apart. Type > Type on a Path > Options > Spacing tightens them back up — the detail that separates a professional result from an amateur one.")
    tile_grid("The Typographer's Vocabulary", [
     ("Typeface vs font", "A typeface is the design (Minion); a font is one instance of it (Minion Bold 10 pt)."),
     ("Point size and leading", "Size sets the letters; leading sets the line spacing. Start body text at leading ≈ 120% of size."),
     ("Kerning", "Space between two specific characters. Optical for display type, Metrics for well-made text faces."),
     ("Tracking", "Space applied evenly across a range. A headline and small-caps tool — it destroys body copy."),
     ("x-height and cap height", "Why two faces at the same point size can look completely different in scale."),
     ("Measure", "Line length. Roughly 45–75 characters is the readable range for body text.")],
     kicker="TOPIC 03 · TYPOGRAPHY", cols=2, size=14, accent=BLUE)
    image_explain("Paragraph Craft", "drop_cap", [
     ("Drop caps", "Set the number of lines and characters in the Paragraph panel; style it with a character style."),
     ("Space before / after", "Never use empty paragraph returns — they break as soon as text reflows."),
     ("Indents", "First-line and hanging indents, set numerically, not with tabs or spaces."),
     ("Hyphenation and justification", "Control the rag and the word spacing. Turn hyphenation off for headlines."),
     ("Paragraph rules", "A rule above or below that moves with the paragraph — for run-in headings and pull quotes.")],
     kicker="TOPIC 03 · TYPOGRAPHY", accent=BLUE)
    image_full("The Styles Cascade", "styles_cascade",
     kicker="TOPIC 03 · STYLES",
     caption="Redefine one paragraph style and 200 pages reflow in a second. A '+' beside a style name is the warning sign of a local override.",
     accent=VIOLET)
    image_explain("Nested Styles and Bulleted Lists", "nested_styles", [
     ("Nested styles", "Apply a character style automatically up to a chosen character — a colon, a tab, the end of a word."),
     ("Perfect for run-in headings", "'Delivery: ' in bold, the rest in regular, with no manual formatting anywhere."),
     ("Bullets and numbering", "Type > Bulleted & Numbered Lists — never typed hyphens, which break on reflow."),
     ("Glyphs", "Type > Glyphs reaches every character in the font: ligatures, alternates, fractions, true small caps."),
     ("Text variables", "Running headers, chapter titles and last page number that update themselves.")],
     kicker="TOPIC 03 · STYLES", accent=VIOLET)
    image_explain("Tables", "table_cell_styles", [
     ("Two ways in", "Table > Insert Table from scratch, or Table > Convert Text to Table from tab-delimited data."),
     ("A cell is a mini text frame", "It holds text, an inline graphic, or another table."),
     ("Header rows repeat", "Mark a row as a header and it repeats automatically when the table breaks across pages."),
     ("Table and cell options", "Borders, row and column strokes, alternating fills, insets and vertical justification."),
     ("Table and cell styles", "The same discipline as paragraph styles — consistency across a data-heavy publication.")],
     kicker="TOPIC 03 · TABLES", accent=TEAL)
    image_explain("Interactivity: Hyperlinks, Buttons and QR Codes", "new_hyperlink", [
     ("Hyperlinks", "To a URL, a file, an e-mail address, a page, or a text anchor inside the document."),
     ("Buttons", "Any frame becomes a button with an event and an action — go to page, open a URL, play a video."),
     ("QR codes", "Object > Generate QR Code makes a live, vector, colour-editable code — the print-to-digital bridge."),
     ("Media", "Place H.264/MP4 video and MP3 audio; control them from the Media panel."),
     ("Where they work", "Interactive PDF and EPUB. A print PDF ignores them entirely.")],
     kicker="TOPIC 03 · INTERACTIVITY", accent=AMBER)
    image_explain("Animation and Page Transitions", "animation_panel", [
     ("Motion presets", "Ready-made animations applied from the Animation panel in one click."),
     ("Motion paths", "Edit the path with the Pen and Direct Selection tools, exactly like any other path."),
     ("The Timing panel", "Controls the order animations play, and what plays together."),
     ("Page transitions", "Applied per spread; they appear in exported interactive PDF and fixed-layout EPUB."),
     ("Not for print", "Animation exists only in digital output — it has no meaning in a press-ready PDF.")],
     kicker="TOPIC 03 · INTERACTIVITY", accent=AMBER)
    image_full("The Preflight Gate", "preflight_gate",
     kicker="TOPIC 03 · OUTPUT",
     caption="A green light in the status bar before you export. Then File > Package collects the document, links and fonts for the printer.",
     accent=TEAL)
    image_full("Choose the Export by the Destination", "export_matrix",
     kicker="TOPIC 03 · OUTPUT",
     caption="One layout, many outputs. Each destination has its own non-negotiable settings — and getting them wrong is what gets a file rejected.",
     accent=BLUE)
    decision_map("Reflowable or Fixed-Layout EPUB?",
     "Must the design stay exactly as laid out?",
     ("Fixed Layout EPUB",
      "Every position preserved; animation survives; larger files. Children's books, magazines, photo books, anything design-led."),
     ("Reflowable EPUB",
      "Text reflows to the device; the reader sets the type size; styles map to CSS. Novels, reports, guides — anything text-led."),
     kicker="TOPIC 03 · DIGITAL OUTPUT", color=VIOLET,
     note="If in doubt, ask who reads it and on what. A commuter on a phone needs reflowable; a recipe book on a tablet needs fixed layout.")
    image_explain("Share for Review", "share_review", [
     ("The old loop", "E-mail a PDF, get a marked-up printout back, retype every comment. Slow and error-prone."),
     ("File > Share for Review", "Publishes the layout for stakeholder comment, with controlled access."),
     ("Comments come back in", "Reviewers' comments land in the Comments panel inside InDesign, anchored to the artwork."),
     ("Tracked and auditable", "You can see who asked for what, and mark each comment resolved."),
     ("Version control", "Create a new review for each round so the approval trail is clear.")],
     kicker="TOPIC 03 · COLLABORATION", accent=TEAL)

TOPIC_VISUALS = {1: topic1_visuals, 2: topic2_visuals, 3: topic3_visuals}

for t in C.TOPICS:
    section(f"TOPIC {t['code']}", t["title"], t["code"], t["subtitle"])

    # key concepts, chunked into readable tile grids
    cons = t["concepts"]
    per = 6
    chunks = [cons[i:i + per] for i in range(0, len(cons), per)]
    for ci, chunk in enumerate(chunks):
        suffix = "" if ci == 0 else f" ({ci + 1})"
        tile_grid(f"Key Concepts — {t['title']}{suffix}", chunk,
                  kicker=f"TOPIC WEIGHTING {t['weighting']}", cols=2, size=12)

    # the visual teaching block for this topic (screenshots + concept diagrams)
    TOPIC_VISUALS[t["num"]]()

    acts = TOPIC_ACTS[t["num"]]
    third = (len(acts) + 2) // 3
    groups = [acts[i:i + third] for i in range(0, len(acts), third)][:3]
    while len(groups) < 3: groups.append([])
    cards = []
    for gi, g in enumerate(groups):
        lbl = ("—" if not g else (f"Activity {g[0]['num']}" if g[0]['num'] == g[-1]['num']
                                  else f"Activities {g[0]['num']}–{g[-1]['num']}"))
        cards.append((CARD_COLORS[gi], lbl, [a["title"] for a in g] if g else ["—"]))
    cards3(f"Hands-On Activities — {t['title']}", cards, kicker="WHAT YOU'LL DO")

    for a in acts:
        # 1. the case-study briefing, with the real source artwork
        activity_visual(f"ACTIVITY {a['num']}", a["title"], LAB_IMG.get(a["num"], "act_masterpage"),
                        a["scenario"].replace("**", ""), kicker=f"TOPIC {t['code']} · CASE STUDY",
                        deliverable=a["build"])
        # 2. what it is for — objective, deliverable, toolchain, done-when
        activity_overview(f"ACTIVITY {a['num']}", a["title"], a["desc"], a["build"], a["services"],
                          kicker=f"TOPIC {t['code']} · HANDS-ON",
                          objective=a.get("objective"), test=a.get("test"))
        # 3. the discussion questions the trainer works through with the class
        tile_grid(f"Discuss — Activity {a['num']}", [(f"Q{i + 1}", q) for i, q in enumerate(a["questions"])],
                  kicker=f"ACTIVITY {a['num']} · ORAL QUESTIONING PRACTICE", cols=1, size=12,
                  accent=VIOLET)
        # 4. verification + troubleshooting (NO step-by-step — that is the LG's job)
        test_slide(a["title"], a["test"], kicker=f"ACTIVITY {a['num']} · VERIFY",
                   troubleshoot=[("If it doesn't work", a["troubleshoot"]),
                                 ("Where are the steps?", "The full step-by-step procedure for this activity is in your Learner Guide."),
                                 ("Still stuck?", "Raise your hand — the trainer will work through it with you at your machine.")])

    content(f"Recap — {t['title']}",
            ["You can now: " + a["objective"].split("(TSC")[0].strip().rstrip(".") + "." for a in acts][:6],
            kicker="TOPIC RECAP", size=15)

# ---------------------------------------------------------------- CLOSE
section("WRAP-UP", "Course Summary & Next Steps", "")

tile_grid("What You Achieved", [(t, b) for t, b in C.LEARNING_OUTCOMES_LONG],
 kicker="LEARNING OUTCOMES", cols=1, size=14)

tile_grid("Continue Your Learning", [
 ("Adobe InDesign Learn & Support", "https://helpx.adobe.com/indesign/desktop.html — the official reference for every feature."),
 ("Get started with InDesign", "https://www.adobe.com/learn/indesign/web/get-started-indesign — Adobe's structured beginner path."),
 ("InDesignSkills", "https://indesignskills.com — practical tutorials, free templates and layout inspiration."),
 ("Rebuild today's activities", "Redo each activity from a blank document until the workflow is automatic."),
 ("Build a portfolio piece", "Take one real publication end to end: brief, spec, layout, preflight, package, export."),
 ("Adobe InDesign Developer", "https://developer.adobe.com/indesign/ — scripting and UXP plugins when you are ready to automate.")],
 kicker="NEXT STEPS", cols=2, size=13)

tile_grid("Recommended Courses", [(rc, "") for rc in C.RECOMMENDED_COURSES],
 kicker="CONTINUE WITH TERTIARY INFOTECH", cols=1, size=15)

tile_grid("Support", [
 ("Email", "enquiry@tertiaryinfotech.com"),
 ("Telephone", "+65 6100 0613"),
 ("Website", "www.tertiarycourses.com.sg"),
 ("LMS / TMS", "https://lms-tms.tertiaryinfotech.com")],
 kicker="WE'RE HERE TO HELP  ·  DURING AND AFTER THE CLASS", cols=2, size=16)

tile_grid("Assessment", [
 ("Practical Performance (PP)", "75 minutes · open book · hands-on InDesign layout tasks (A1–A4)."),
 ("Oral Questioning (OQ)", "15 minutes · one-to-one with the assessor · five knowledge questions (K1–K3)."),
 ("Digital attendance", "Remember to take the Assessment digital attendance (TRAQOM) before you start."),
 ("Submit your work", "Submit your InDesign document and screenshots as directed by the assessor.")],
 kicker="WRAP-UP", cols=2, size=15)

process_map("Assessment Flow", [
 ("TRAQOM survey", "Scan the LMS QR code"),
 ("Digital attendance", "Scan the SSG assessment QR"),
 ("Sit the PP", "75 minutes · open book"),
 ("Answer the OQ", "15 minutes · one-to-one"),
 ("Sign the record", "Sign the Summary Record")],
 kicker="ON ASSESSMENT DAY", color=BLUE,
 synthesis=("REMEMBER", "All five steps are mandatory for WSQ funding — missing the digital attendance or the TRAQOM survey can invalidate your claim."))

tile_grid("Digital Attendance (Mandatory)", [
 ("Three times today", "Take the AM, PM and Assessment digital attendance — mandatory for every WSQ-funded course."),
 ("Trainer shows the QR", "The trainer or administrator displays the digital attendance QR code from the SSG portal."),
 ("Scan and submit", "Scan the QR code with your mobile phone camera and submit your attendance."),
 ("75% minimum", "A minimum of 75% attendance is required to be eligible for assessment and funding.")],
 kicker="TRAQOM · SSG DIGITAL ATTENDANCE", cols=2, size=15)

big_statement("Thank You!",
 "You can now establish a layout requirement, build the document, use the InDesign toolset and refine it into a print- and screen-ready publication.",
 "HAPPY DESIGNING", color=TEAL)

# ---------------------------------------------------------------- motion pass
DIVIDERS = ("COURSE ADMINISTRATION", "CORE CONCEPTS", "WRAP-UP")
for s in prs.slides:
    joined = " ".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame)
    is_div = any(k in joined for k in DIVIDERS) or \
             any(t["title"] in joined and f"TOPIC {t['code']}" in joined for t in C.TOPICS)
    engine._transition(s, "push" if is_div else "fade", speed="med" if is_div else "fast")

OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
NSLIDES = len(prs.slides._sldIdLst)
print(f"Saved {OUT}  ({NSLIDES} slides)")

# ---------------------------------------------------------------- slide index
# The Lesson Plan cites slide numbers. Emit them FROM THE DECK WE JUST BUILT so the
# LP can never drift out of step with the PPT — build_lesson_plan.py reads this file
# and refuses to run without it.
import json, re as _re
_rows = []
for _i, _s in enumerate(prs.slides, 1):
    _t = " ".join(sh.text_frame.text.replace("\n", " ") for sh in _s.shapes if sh.has_text_frame)
    _rows.append((_i, " ".join(_t.split())))

def _first(pred, start=1):
    for _i, _t in _rows:
        if _i >= start and pred(_t):
            return _i
    return None

_idx = {"admin_start": 2, "total": NSLIDES}
_idx["core_concepts"] = _first(lambda t: "CORE CONCEPTS" in t and "Why InDesign" in t)
_idx["core_end"] = _first(lambda t: "TOPIC 01" in t and C.TOPICS[0]["title"] in t) - 1
for _tp in C.TOPICS:
    _n, _c, _ti = _tp["num"], _tp["code"], _tp["title"]
    _sec = _first(lambda t, c=_c, ti=_ti: f"TOPIC {c}" in t and ti in t and "Key Concepts" not in t)
    _cards = _first(lambda t, ti=_ti: "WHAT YOU'LL DO" in t and ti in t, _sec)
    _recap = _first(lambda t, ti=_ti: "TOPIC RECAP" in t and ti in t, _sec)
    _idx[f"t{_n}_section"] = _sec
    _idx[f"t{_n}_concepts_start"] = _sec + 1
    _idx[f"t{_n}_concepts_end"] = _cards - 1
    _idx[f"t{_n}_labs_start"] = _cards
    _idx[f"t{_n}_recap"] = _recap
_acts = {}
for _i, _t in _rows:
    if "CASE STUDY" in _t:
        _m = _re.search(r"ACTIVITY (\d+)", _t)
        if _m:
            _acts.setdefault(_m.group(1), _i)
_idx["activity_slide"] = _acts
_idx["wrapup"] = _first(lambda t: "WRAP-UP" in t and "Course Summary" in t)
json.dump(_idx, open(os.path.join(HERE, "slide_index.json"), "w"), indent=1)
print("  slide_index.json written —", len(_acts), "activities mapped")
