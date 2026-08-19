"""
SINGLE SOURCE OF TRUTH — Creating Stunning Print and Digital Publications with InDesign
Course Code: TGS-2021007827

Every artifact (PPT, LP, LG, LG.md, labs index, activities folders, assessment) is
generated from this file + data_domain1..3.py so they stay 100% aligned.

Guiding principle: the course material is 100% aligned to the assessed learning
outcomes so learners who take the course can pass the assessment.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Creating Stunning Print and Digital Publications with InDesign"
SHORT_TITLE  = "Creating Stunning Print and Digital Publications with InDesign"
COURSE_CODE  = "TGS-2021007827"
VERSION      = "v12.0"
VERSION_DATE = "19 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 1
HOURS_PER_DAY = 8

COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-creating-stunning-print-and-digital-publications-with-indesign.html"

# ------------------------------------------------------------------ Skills Framework
TSC_TITLE = "Manual and Digital Drawings Production"
TSC_CODE  = "RET-DNI-4004-1.1"
TSC_REF   = "SF-RET_TSC_Ref_DNI_Manual and Digital Drawings Production_SDD_20170710_V01"

TSC_ABILITIES = [
    ("A1", "Establish drawing requirements"),
    ("A2", "Determine document dimensions, angles, shapes and finished sizes of project requirements"),
    ("A3", "Identify and select appropriate mediums for drawings"),
    ("A4", "Refine drawings to meet project requirements within scope of authority"),
]
TSC_KNOWLEDGE = [
    ("K1", "Types, techniques and processes of manual production drawings"),
    ("K2", "Types of computer-aided drawing equipment, software, techniques and processes"),
    ("K3", "Conventional signs and markings for drawings"),
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Establish the drawing layout requirement and create the InDesign document.",
    "LO2: Utilize InDesign tools for drawings.",
    "LO3: Refine drawings using InDesign.",
]

LEARNING_OUTCOMES_LONG = [
    ("LO1 · Establish & create",
     "Establish the drawing layout requirement from a client brief — trim, bleed, margins, "
     "columns, colour mode and binding — and create the correctly specified InDesign document "
     "with parent pages, grids and guides."),
    ("LO2 · Utilize InDesign tools",
     "Utilize the InDesign drawing toolset — text frames and threading, the Pen and shape tools, "
     "paths and Pathfinder, colour, gradients, transparency and effects, transform, align and "
     "layers — to build the page."),
    ("LO3 · Refine the drawings",
     "Refine the layout with professional typography, paragraph/character/object styles, tables, "
     "interactivity and a preflighted, correctly packaged export for both print and digital delivery."),
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Get Started on InDesign",
         subtitle="Establish drawing & layout requirements · Explore the interface · Create documents · Manage pages",
         weighting="30%",
         concepts=[
            "Adobe InDesign is the industry-standard page-layout application for print and digital publishing — it assembles type, images and vector artwork into a precisely specified, production-ready document, and it is the only Creative Cloud application built around the multi-page, multi-master, style-driven workflow that publications demand.",
            "InDesign is a layout tool, not an image editor or an illustration tool: pixels are retouched in Photoshop, vector artwork is drawn in Illustrator, and both are *placed* into InDesign as linked assets. Knowing which application owns which job is the single biggest efficiency gain for a junior designer.",
            "Every job begins with a written specification: the trim size (final cut size), the bleed (artwork extending past trim, 3 mm in Singapore/ISO practice), the slug (production marks area), the safety/margin (no live matter inside), the binding method and the intended output. Get the spec wrong and the whole file is re-done.",
            "Colour mode is decided by the output, not by preference: CMYK for offset and digital print, RGB for screen, EPUB and interactive PDF. Setting the wrong Intent in the New Document dialog silently sets the wrong colour space, transparency blend space and default swatch library.",
            "Resolution follows the medium: 300 ppi at final size for print, 72–150 ppi for screen, and vector wherever possible for logos and type. Effective PPI (not native PPI) is what actually prints — scaling a placed image up in InDesign lowers its effective resolution.",
            "The InDesign interface is workspace-driven — the Tools panel, the Control panel (context-sensitive to the current selection), the Properties panel, the panel dock and the document window. Saving a custom workspace (Window > Workspace > New Workspace) is how professionals keep a consistent, fast layout environment.",
            "Two selection tools do very different jobs: the black Selection tool moves and resizes the *frame*, and the white Direct Selection tool edits the *content* inside the frame or the individual anchor points of a path. Most beginner frustration in InDesign is a wrong-selection-tool problem.",
            "A parent page (formerly 'master page') is a reusable background applied to many document pages — running heads, folios, footers, column structure and repeating logos live there. Change the parent once and every page based on it updates automatically.",
            "Automatic page numbering is inserted as a *marker* (Type > Insert Special Character > Markers > Current Page Number) on the parent page, not as typed digits, so numbering re-flows correctly when pages are added, removed or re-ordered.",
            "Sections and section markers let one document carry front matter in roman numerals and body matter in arabic numerals, with chapter prefixes — essential for books, reports and catalogues.",
            "Grids and guides are the invisible skeleton of professional layout: a baseline grid locks body text to a common rhythm across columns and pages, a document grid aligns objects, and ruler guides (page guides vs spread guides) position elements precisely. Layout > Create Guides builds a full modular grid in one dialog.",
            "The Adjust Layout feature (File > Adjust Layout) re-flows an existing layout automatically when the page size, margins or bleed change — turning a formerly day-long re-work into a single dialog, and a genuine productivity skill to demonstrate to an employer.",
            "A book file (File > New > Book) is a collection of InDesign documents that share styles, swatches and parent pages, with continuous pagination across the whole set — the standard way to produce a long publication as manageable chapter files.",
            "Preferences that matter from day one: units and increments (millimetres for Singapore print), Auto-activate Adobe Fonts, Smart Text Reflow and the Interface scaling. Set them with no document open and they become the application default for every new job.",
         ]),
    dict(num=2, code="02",
         title="Basic InDesign Drawing Techniques",
         subtitle="Text & threading · Frames & paths · Graphics & colour · Manage objects",
         weighting="40%",
         concepts=[
            "Everything on an InDesign page lives inside a frame. A text frame holds a story, a graphics frame holds a placed image, and an unassigned frame is a coloured shape. A frame and its content are two separate things that can be selected, moved and scaled independently — this is the mental model the whole application is built on.",
            "Text enters a layout by typing, by File > Place (the professional route — it keeps the source file's structure and can be linked), by pasting, or by Type > Fill With Placeholder Text when the copy has not arrived yet and the design still has to be shown to a client.",
            "Threading connects frames so a single story flows between them: click the out port of a frame, then click or drag on the next frame. A red plus sign in the out port means overset text — copy that exists in the story but has nowhere to sit. Overset text is invisible on the printed page and is the most common production error in a junior designer's file.",
            "Four ways to flow text after loading the cursor: click for a single frame, Shift-click for autoflow (adds pages), Alt/Option-click for semi-autoflow (keeps the cursor loaded), and Shift+Alt/Option-click for fixed-page autoflow. Knowing autoflow turns a 40-page text import from an afternoon into a few seconds.",
            "Smart Text Reflow (Preferences > Type) adds and deletes pages automatically as the story grows or shrinks — indispensable for text-led publications such as reports and books.",
            "Graphics are *placed*, never embedded by default: File > Place creates a link to the original file, and the Links panel is the production control panel for every placed asset — showing modified links, missing links, effective PPI, colour space and scale. A file that goes to print with a missing or low-resolution link is a rejected job.",
            "Frame fitting controls the relationship between an image and its frame: Fill Frame Proportionally, Fit Content Proportionally, Fit Frame to Content and Content-Aware Fit. Setting Object > Object Layer Options > Frame Fitting Options on a frame *before* placing is the professional habit.",
            "Paths are made of anchor points joined by segments; direction handles on a smooth point control the shape and size of the adjoining curves. The Pen tool creates corner points by clicking and smooth points by click-dragging — the single most transferable vector skill across InDesign, Illustrator and every other design tool.",
            "The Pencil tool draws freehand paths and reshapes existing ones; the Smooth and Erase tools refine them. For layout work these are used for organic decorative shapes rather than precision artwork.",
            "Compound paths (Object > Paths > Make Compound Path) punch transparent holes through a shape — how a doughnut, a stencilled letterform or a knocked-out window in a colour block is made. The Pathfinder panel (Add, Subtract, Intersect, Exclude Overlap, Minus Back) combines shapes into new compound shapes.",
            "Clipping paths and text wrap control how images sit within text: Object > Clipping Path > Detect Edges silhouettes an image without an alpha channel, and the Text Wrap panel pushes body copy around the silhouette rather than the rectangular frame — the difference between an amateur and a professional-looking magazine page.",
            "Colour in InDesign is applied to the *stroke* (the border) or the *fill* (the interior) of an object, and to text. Swatches are named, reusable and — critically — global: edit the swatch and every object using it updates. Unnamed colours mixed straight in the Colour panel are the reason files go to print with 40 nearly-identical blues.",
            "Spot colours (Pantone) are pre-mixed inks specified for brand-critical colour and special finishes; process colours are built from CMYK. Every spot colour on a page is an extra printing plate and an extra cost, so the swatch type is a commercial decision, not just a visual one.",
            "The Colour Theme tool extracts a harmonious five-colour theme from any image or artwork on the page and adds it to the Swatches panel — the fastest professional route from a client's photograph to a coherent palette.",
            "Gradients (linear and radial) create graduated blends and can be applied directly to live text. Transparency, blending modes and the nine InDesign effects — drop shadow, inner shadow, outer and inner glow, bevel & emboss, satin, and three feathers — are applied per level (object, stroke, fill or text) from the Effects panel.",
            "Objects are positioned precisely, never by eye: the X/Y and W/H fields in the Control panel with a chosen reference point, Smart Guides for live alignment feedback, the Align panel (align to selection, margins, page or spread, plus Distribute Spacing), and Object > Transform for numeric rotate, scale, shear and reflect.",
            "Layers are transparent sheets that control stacking, visibility, locking and printing. A professional file separates background, images, text and non-printing notes onto named layers — which also makes multi-language versions and client-specific variants trivial to produce.",
            "Grouping, Object > Arrange (Bring to Front / Send to Back), locking and anchored objects (objects that flow inline with text) complete the object-management toolkit that keeps a complex page maintainable by someone other than its author.",
         ]),
    dict(num=3, code="03",
         title="Refine InDesign Drawings",
         subtitle="Typography & type on a path · Styles · Tables · Interactivity · Export & package",
         weighting="30%",
         concepts=[
            "Refinement is where a competent layout becomes a professional publication: typographic detail, systematic styles, structured tables, and an export that a printer or a digital platform will actually accept without a query.",
            "Typography vocabulary is the professional's toolkit: typeface vs font vs type style, x-height, cap height, ascender and descender, weight and width. Point size sets the letters; leading sets the line spacing; the classic starting ratio for body text is leading ≈ 120% of point size.",
            "Kerning adjusts the space between two specific characters (use Optical for display type, Metrics for well-made text faces); tracking adjusts space evenly across a range. Excessive tracking on body copy destroys readability — it is a headline and small-caps tool.",
            "Type on a path (Type > Type on a Path) flows text along any open or closed path, with Rainbow, Skew, 3D Ribbon, Stair Step and Gravity effects plus a Spacing control that fixes the fanning that occurs on tight curves.",
            "Paragraph-level craft: alignment and justification settings, hyphenation control, indents (including hanging indents), space before/after (never empty paragraph returns), drop caps, nested styles for run-in headings, and paragraph rules above and below.",
            "Bulleted and numbered lists are created through Type > Bulleted & Numbered Lists — never by typing hyphens — so that the marker, indent and font are controlled by the style and remain consistent throughout the publication.",
            "Glyphs (Type > Glyphs) give access to every character in a font — ligatures, alternates, ornaments, fractions and true small caps — and text variables (running headers, last page number, chapter title, modification date) insert content that updates itself.",
            "Styles are the single largest productivity multiplier in InDesign. A paragraph style holds every attribute of a paragraph; a character style overrides selected characters within it; object styles carry frame, stroke, fill, effects and text-frame options; table and cell styles do the same for tables. Redefine one style and the entire 200-page document reflows in a second.",
            "Style discipline: build styles Based On a parent style so global changes cascade; set Next Style so a heading automatically leads into body copy; use Find/Change and Load Styles to import a house style set from another document. A '+' beside a style name means a local override — a warning sign in a production file.",
            "Tables are created from scratch (Table > Insert Table) or converted from tab-delimited text (Table > Convert Text to Table). A cell behaves like a miniature text frame and can hold text, an inline graphic or another table. Header rows repeat automatically when a table breaks across frames or pages.",
            "Table formatting is controlled through Table Options (borders, row/column strokes, alternating fills, header and footer rows) and Cell Options (insets, vertical justification, diagonal lines), and locked in with table and cell styles for consistency across a data-heavy publication.",
            "Interactivity turns a layout into a digital publication: hyperlinks to URLs, files, e-mail addresses and text anchors; buttons with events and actions; animation with motion presets, the Timing panel and editable motion paths; page transitions; and placed video (H.264/MP4) and audio (MP3).",
            "A QR code generated inside InDesign (Object > Generate QR Code) is live, vector, colour-editable and infinitely scalable — the standard bridge from a printed page to a digital destination.",
            "Preflight (Window > Output > Preflight) checks the live document continuously against a profile — missing links, low effective resolution, overset text, RGB images in a CMYK job, missing fonts. The green light in the status bar before you export is the professional's final gate.",
            "Package (File > Package) collects the INDD, every linked asset, every used font and a printing-instructions report into one folder — the correct way to hand a job to a printer or another designer.",
            "Export is output-specific: PDF/X-1a or PDF/X-4 with marks and 3 mm bleed for print; Adobe PDF (Interactive) for on-screen documents with hyperlinks and buttons; EPUB Reflowable for text-led e-books that adapt to the reader's device; EPUB Fixed Layout where the design must be preserved exactly; JPEG/PNG for previews; and Publish Online for a shareable web version.",
            "Sharing for review (File > Share for Review) posts the layout for stakeholder comment with controlled access, and comments return into the Comments panel inside InDesign — replacing the e-mailed-PDF-and-marked-up-printout loop with a tracked, auditable process.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "From Client Brief to Print- and Screen-Ready Publication",
}

# ------------------------------------------------------------------ assessment
# Instruments per Assessment Plan v5 (17 Oct 2025): Practical Performance + Oral
# Questioning. There is NO written short-answer paper on this course.
ASSESSMENT = dict(
    written="Oral Questioning (OQ) — 5 questions, 15 minutes, 1:1 with the assessor, open book. Covers the underpinning knowledge K1–K3.",
    practical="Practical Performance (PP) — hands-on InDesign layout tasks, 75 minutes, open book. Covers the abilities A1–A4.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
ASSESSMENT_SHORT = "Practical Performance (75 min) + Oral Questioning (15 min)"

# ------------------------------------------------------------------ recommended
RECOMMENDED_COURSES = [
    "WSQ - Professional Digital Image Editing with Photoshop",
    "WSQ - Creating Professional Graphics with Adobe Illustrator",
    "WSQ - Compositing and Visual Effects with After Effects",
    "WSQ - Video Editing with Premiere Pro",
    "WSQ - Interactive UI Design with Adobe XD: From Wireframes to Prototypes",
]

# ------------------------------------------------------------------ prerequisites
PREREQUISITES = [
    ("Knowledge & skills", "Able to operate a computer confidently. Minimum 3 GCE 'O' Levels including English, or WPL Level 5."),
    ("Experience", "Minimum 1 year of working experience."),
    ("Attitude", "Positive learning mindset and willingness to participate in hands-on practice."),
    ("Software", "Adobe InDesign (2024 or later) installed on a Windows or macOS laptop."),
    ("Hardware", "Laptop with a mouse; a minimum 1280 x 800 display is recommended."),
    ("Files", "The course lab files, downloaded from the LMS before the class starts."),
]

TARGET_AUDIENCE = [
    "Graphic and layout designers moving into publication work",
    "Marketing and communications executives who produce collateral in-house",
    "Editorial and publishing professionals",
    "Branding and content creators preparing print and digital assets",
    "Career-changers building an Adobe Creative Cloud skill set",
]
