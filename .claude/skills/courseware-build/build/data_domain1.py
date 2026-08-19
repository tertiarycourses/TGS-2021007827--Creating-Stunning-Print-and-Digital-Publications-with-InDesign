"""
Topic 1 — Get Started on InDesign.
Hands-on activities. Global contiguous lab numbering across all three domains.

Each activity is a realistic workplace case study: a named client, a real brief,
a deliverable and a verifiable outcome — the same shape as the Practical
Performance assessment so the class rehearses exactly what is assessed.
"""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Establish the Layout Requirement from a Client Brief",
        lo="LO1",
        objective="Establish drawing and layout requirements from a client brief and translate them into a written InDesign document specification (TSC A1, A2).",
        scenario=(
            "You are the junior layout designer at **Harmony Petals**, a Singapore florist with three "
            "retail outlets. The marketing manager, Priya, forwards an e-mail brief at 9.40 am: "
            "\"We need an A5 landscape promotional flyer for the Mid-Autumn range, full-colour, printed "
            "both sides on 200 gsm art card, 5,000 copies, litho at Sun Ray Printers. Photos bleed off "
            "all four edges. Please confirm the specification before you start.\" "
            "Priya has not stated the bleed, the margins or the colour mode. Sun Ray Printers' website "
            "states a 3 mm bleed and a 5 mm minimum safety margin. Getting this wrong costs the "
            "5,000-copy print run."
        ),
        desc=(
            "Interrogate a real client brief, identify what is specified and what is missing, and produce "
            "a completed Document Specification Sheet. You then set the InDesign application preferences "
            "(units in millimetres) that every subsequent lab depends on."
        ),
        build="A completed Document Specification Sheet (trim, bleed, slug, margins, columns, colour mode, resolution, output) signed off before any file is created, plus InDesign preferences set to millimetres.",
        services="Adobe InDesign · Document Specification Sheet · Preferences > Units & Increments",
        questions=[
            "Which four items in Priya's brief are production specifications, and which two are still missing?",
            "Why is 3 mm bleed required when the photographs are described as running 'off all four edges'?",
            "The job is litho-printed. What colour mode must the document use, and what would happen at the printer if RGB were used instead?",
            "The flyer is A5 landscape. State the trim size in millimetres, and the document size including bleed.",
            "Why must units be set to millimetres with no document open, rather than after creating the file?",
        ],
        steps=[
            ("Read the brief and list every stated requirement — size, orientation, colour, stock, quantity, print process, finishing.", ""),
            ("Identify the missing specifications. The brief omits bleed, margins, slug and colour mode; these must be confirmed with the printer, not assumed.", ""),
            ("Look up Sun Ray Printers' specification: 3 mm bleed on all four sides, 5 mm minimum safety margin from trim, PDF/X-1a supply.", ""),
            ("Compute the sizes. A5 landscape trim = 210 x 148 mm. Add 3 mm bleed on all sides for the artwork area = 216 x 154 mm.", "Trim 210 x 148 mm  |  Bleed 3 mm  |  Artwork 216 x 154 mm"),
            ("Decide the colour mode from the output: litho press = CMYK. Set image resolution at 300 ppi effective at final size.", ""),
            ("Complete the Document Specification Sheet and have it checked by the trainer, acting as Priya, before proceeding.", ""),
            ("Close all documents. Choose Edit (Windows) or InDesign (macOS) > Preferences > Units & Increments and set Horizontal and Vertical to Millimeters.", "Preferences > Units & Increments > Millimeters"),
            ("In Preferences > File Handling, enable Auto-activate Adobe Fonts so missing fonts are resolved automatically.", "Preferences > File Handling > Auto-activate Adobe Fonts"),
        ],
        test="Your Specification Sheet states trim 210 x 148 mm, bleed 3 mm, artwork 216 x 154 mm, CMYK, 300 ppi, PDF/X-1a — and the InDesign rulers now read in millimetres.",
        troubleshoot="If the rulers still show picas or inches, you changed preferences with a document open — that only changes the current document. Close all documents and set the preference again to make it the application default.",
    ),
    dict(
        num=2, topic=1,
        title="Create the Document and Explore the InDesign Workspace",
        lo="LO1",
        objective="Create an InDesign document to a stated specification and navigate the workspace, panels and selection tools with confidence (TSC A2, A3).",
        scenario=(
            "The Harmony Petals specification from Lab 1 is signed off. Priya now needs the empty, "
            "correctly specified file created and saved to the shared drive so the copywriter can start "
            "dropping text in. She also asks you to standardise your workspace, because last month a "
            "colleague spent twenty minutes hunting for the Links panel while a client waited on a call."
        ),
        desc=(
            "Create the flyer document from the signed-off specification, learn the Start workspace and "
            "the New Document dialog including presets and Adobe Stock templates, then build and save a "
            "custom workspace containing the panels a layout designer actually uses."
        ),
        build="Harmony_Flyer.indd — an A5 landscape, 2-page, CMYK document with 3 mm bleed and 5 mm margins, plus a saved custom workspace named 'Publication Layout'.",
        services="Adobe InDesign · Start workspace · New Document dialog · Panels & workspaces",
        questions=[
            "What is the difference between the Print, Web and Mobile intents in the New Document dialog, and what does each one change behind the scenes?",
            "You need to move a photograph's frame without changing the photograph inside it. Which selection tool do you use, and why?",
            "Where would you find the Links panel, and why does a production designer keep it visible at all times?",
            "What does 'Facing Pages' do, and why is it switched OFF for a single-sided flyer but ON for a magazine?",
            "How does saving a custom workspace protect against the twenty-minute panel hunt Priya described?",
        ],
        steps=[
            ("Launch InDesign and study the Start workspace — recent files, presets, and the Adobe Stock template gallery.", ""),
            ("Choose File > New > Document. Select the Print intent so the colour mode defaults to CMYK and units to millimetres.", "File > New > Document  ·  Intent: Print"),
            ("Set Width 210 mm, Height 148 mm, Orientation Landscape, Pages 2, and clear Facing Pages — this is a single-sided flyer printed both sides, not a spread.", "210 x 148 mm  ·  Landscape  ·  2 pages  ·  Facing Pages OFF"),
            ("Set all four Margins to 5 mm. Expand Bleed and Slug and set Bleed to 3 mm on all four sides.", "Margins 5 mm  ·  Bleed 3 mm"),
            ("Click Create, then File > Save As and name the file Harmony_Flyer.indd in your working folder.", "File > Save As  ·  Harmony_Flyer.indd"),
            ("Identify the red bleed line, the black trim edge and the magenta margin guide on screen. Confirm all three are visible.", ""),
            ("Explore the Tools panel. Select a frame with the black Selection tool (V), then with the white Direct Selection tool (A), and observe what each one selects.", "V = Selection (frame)  ·  A = Direct Selection (content / points)"),
            ("Open Window > Links, Window > Pages, Window > Colour > Swatches and Window > Output > Preflight, and dock them together on the right.", "Window > Links / Pages / Swatches / Preflight"),
            ("Choose Window > Workspace > New Workspace, name it 'Publication Layout', tick Panel Locations and Menu Customization, and click OK.", "Window > Workspace > New Workspace"),
            ("Press W to toggle Preview mode and see the flyer as it will trim; press W again to return to Normal.", "W = Preview / Normal toggle"),
        ],
        test="Harmony_Flyer.indd opens at 210 x 148 mm landscape with a visible 3 mm red bleed guide and 5 mm margins, and 'Publication Layout' appears in the Window > Workspace list.",
        troubleshoot="No red bleed line visible? Bleed was left at 0 — fix it in File > Document Setup without recreating the file. Guides missing entirely? Press W to leave Preview mode, or use View > Grids & Guides > Show Guides.",
    ),
    dict(
        num=3, topic=1,
        title="Build a Parent Page with Automatic Page Numbering",
        lo="LO1",
        objective="Manage pages using parent pages, automatic numbering markers and the Adjust Layout feature so a multi-page publication remains maintainable (TSC A2, A4).",
        scenario=(
            "Harmony Petals is also producing a 16-page **Seasonal Care Guide**. The previous designer "
            "typed the page numbers by hand. Marketing has now asked for two extra pages to be inserted "
            "at page 4, which means every folio after it is wrong, and the printer has separately advised "
            "that the outer margin must increase from 12 mm to 18 mm for the perfect binding. Re-doing "
            "this manually would take the rest of the day."
        ),
        desc=(
            "Open the supplied long document, build a proper parent page carrying a running footer and an "
            "automatic page-number marker, apply it across the publication, then insert pages and change "
            "the margins — proving that the automatic numbering and Adjust Layout do the re-work for you."
        ),
        build="HP_LongDoc.indd with an A-Parent carrying an automatic folio and running footer, applied to all pages, surviving a 2-page insertion and an 18 mm margin change.",
        services="Adobe InDesign · Pages panel · Parent pages · Current Page Number marker · Adjust Layout",
        questions=[
            "Why must a page number be inserted as a Current Page Number *marker* rather than typed digits?",
            "The letter 'A' appears in the text frame on the parent page. What will it display on document page 7?",
            "Objects from a parent page appear with a dotted border on document pages and cannot be selected normally. How do you override a single parent item on one page, and when is that justified?",
            "What exactly does File > Adjust Layout change, and what does it not change?",
            "Your document has front matter in roman numerals and a body in arabic numerals. Which feature makes that possible in one file?",
        ],
        steps=[
            ("Open HP_LongDoc.indd from the Topic 1 lab folder and open Window > Pages.", "Open HP_LongDoc.indd"),
            ("In the Pages panel, double-click A-Parent to edit it. Both parent pages appear in the document window.", ""),
            ("Select the Type tool (T) and draw a text frame in the bottom outer corner of the left parent page, wide enough for a three-digit number plus a label.", "T = Type tool"),
            ("With the cursor in the frame, choose Type > Insert Special Character > Markers > Current Page Number. The letter 'A' appears.", "Type > Insert Special Character > Markers > Current Page Number"),
            ("Type a space then 'Harmony Petals Seasonal Care Guide'. Set it to 8 pt, and align it to the outer edge.", ""),
            ("Copy the frame, paste it onto the right parent page, and set its alignment to the opposite outer edge so the folio always sits on the outside.", "Edit > Paste in Place, then reposition"),
            ("Return to page 1 by double-clicking it in the Pages panel. Confirm real page numbers now appear on every page.", ""),
            ("In the Pages panel menu choose Insert Pages, insert 2 pages after page 3, and confirm every subsequent folio renumbers itself automatically.", "Pages panel menu > Insert Pages > 2 pages after page 3"),
            ("Choose File > Document Setup, click Adjust Layout, change the outer margin to 18 mm, and click OK. Watch the existing page elements re-flow.", "File > Document Setup > Adjust Layout  ·  outer margin 18 mm"),
            ("Review three or four pages and correct any element the automatic adjustment has left visually unbalanced.", ""),
        ],
        test="Every page carries a correct, automatically generated folio; after inserting two pages the numbering is still correct end to end; the outer margin measures 18 mm and content has re-flowed to respect it.",
        troubleshoot="Folio shows 'A' on document pages too? You typed the letter A instead of inserting the marker — delete it and use the Markers menu. Cannot select the footer on a document page? That is correct: parent items are locked. Use Ctrl/Cmd+Shift+click to override just that instance.",
    ),
    dict(
        num=4, topic=1,
        title="Set Up Grids, Guides and a Modular Column Structure",
        lo="LO1",
        objective="Determine document dimensions and structure by building a baseline grid, a document grid and a modular guide system that aligns every element on the page (TSC A2, A4).",
        scenario=(
            "The Harmony Petals brochure has come back from the client with one comment: \"It looks "
            "untidy — the pictures and the headings don't line up.\" Priya wants the two product "
            "photographs aligned exactly and the whole page built on a repeatable structure so that the "
            "next six brochures in the series look like a family rather than six unrelated documents."
        ),
        desc=(
            "Diagnose why an unaligned page reads as untidy, then build the invisible skeleton that fixes "
            "it: a baseline grid for the type, a document grid for objects, ruler guides for specific "
            "positions, and a full modular grid created in one dialog with Layout > Create Guides."
        ),
        build="HP_Brochure_1.indd with a 12 pt baseline grid, a 3-column x 4-row modular grid with 4 mm gutters, and the two product images aligned exactly to the grid.",
        services="Adobe InDesign · Preferences > Grids · Layout > Create Guides · Ruler guides · Smart Guides",
        questions=[
            "What is the difference between a baseline grid and a document grid, and what does each one align?",
            "Why should the baseline grid increment match the leading of your body text?",
            "State the difference between a page guide and a spread guide, and how you create each one.",
            "Layout > Create Guides asks for Number and Gutter. If a 190 mm text area is divided into 3 columns with 4 mm gutters, how wide is each column?",
            "Grids and guides never print. Why, then, are they considered a production requirement rather than a personal preference?",
        ],
        steps=[
            ("Open HP_Brochure_1.indd from the Topic 1 lab folder and assess the current alignment of the two images.", "Open HP_Brochure_1.indd"),
            ("Choose Preferences > Grids. Set the baseline grid Start at 0 mm, Relative To Top Margin, and Increment Every 12 pt to match a 12 pt body leading.", "Preferences > Grids  ·  Increment Every 12 pt"),
            ("In the same dialog set the Document Grid to 5 mm gridline spacing with 5 subdivisions.", "Document Grid: 5 mm, 5 subdivisions"),
            ("Show the grids with View > Grids & Guides > Show Baseline Grid and Show Document Grid.", "View > Grids & Guides > Show Baseline Grid"),
            ("Choose Layout > Create Guides. Set Rows 4, Row Gutter 4 mm, Columns 3, Column Gutter 4 mm, Fit Guides to Margins, and tick Remove Existing Ruler Guides.", "Layout > Create Guides  ·  4 rows / 3 columns / 4 mm gutters"),
            ("Drag a horizontal ruler guide from the top ruler to sit exactly on the second row line; note the Y value in the Control panel as you drag.", ""),
            ("Drag from the ruler with the pointer over the pasteboard to create a spread guide, and compare its extent with the page guide you just made.", ""),
            ("Enable View > Grids & Guides > Snap to Guides, then drag the first product image so its top-left corner snaps to a grid intersection.", "View > Grids & Guides > Snap to Guides"),
            ("Drag the second image and use the green Smart Guides to align its top edge and its vertical centre with the first image.", ""),
            ("Select both images, open Window > Object & Layout > Align, and click Align Top Edges then Distribute Horizontal Centers to confirm the alignment numerically.", "Window > Object & Layout > Align"),
            ("Press W for Preview and confirm the page now reads as ordered, with no visible guides.", "W = Preview"),
        ],
        test="Both images sit exactly on grid intersections, the Align panel confirms their top edges match, and the page shows a consistent 3 x 4 modular structure with 4 mm gutters.",
        troubleshoot="Objects will not snap? Snap to Guides is off, or you are zoomed too far out for the snap zone to engage — zoom to at least 100%. Baseline grid not visible? It only displays above a threshold zoom set in Preferences > Grids > View Threshold.",
    ),
]
