"""
Topic 3 — Refine InDesign Drawings.
Hands-on activities. Global contiguous lab numbering across all three domains.

Each activity is a realistic workplace case study: a named client, a real brief,
a deliverable and a verifiable outcome — the same shape as the Practical
Performance assessment so the class rehearses exactly what is assessed.
"""

DOMAIN3 = [
    dict(
        num=13, topic=3,
        title="Set Type on a Path for a Curved Masthead",
        lo="LO3",
        objective="Refine a layout by placing and controlling type on a path so display typography follows the artwork geometry accurately (TSC A4).",
        scenario=(
            "**Harmony Petals** is running a full-page advertorial in a Singapore lifestyle magazine for "
            "the Orchard outlet's first anniversary. The agency has supplied a circular wreath photograph "
            "and Priya wants the strapline \"Fresh from our Orchard Road studio since 2024\" to curve around "
            "the top of the wreath, exactly as it appears on the shop window decal. The junior designer "
            "tried to fake the curve by rotating each word into place; at 100% the letters visibly stagger "
            "and the magazine's art director has rejected the page. The reprint deadline is 5 pm and the "
            "magazine charges a S$450 late-artwork fee."
        ),
        desc=(
            "Draw a path with the Pen and Ellipse tools, attach live editable type to it with the Type on "
            "a Path tool, then control the result properly — flipping the type inside the curve, changing "
            "the path type effect, and correcting the letter spacing that curves always distort."
        ),
        build="HP_Magazine_5.indd with a live curved strapline set on an elliptical path, correctly flipped, spaced and aligned — editable text, not outlines.",
        services="Adobe InDesign · Type on a Path tool · Ellipse & Pen tools · Type > Type on a Path > Options · Character panel (tracking) · Stroke panel",
        questions=[
            "Type on a path stays live and editable while converted outlines do not. What production risk does converting to outlines create when the client changes one word?",
            "Why does the Rainbow effect distort letter spacing more on a tight curve than on a shallow one, and what two controls correct it?",
            "You need the strapline to read the right way up on the *inside* of the circle. Describe two different ways to achieve that.",
            "The path itself is currently showing a 1 pt black stroke in the printed proof. Why does that happen, and how do you remove it without deleting the type?",
            "Start, Center, End and the flip indicator are all handles on a path type object. Explain what each one moves and why they are easy to confuse.",
        ],
        steps=[
            ("Open HP_Magazine_5.indd from the Topic 3 lab folder and delete the rotated word frames the previous designer left on the page.", "Open HP_Magazine_5.indd"),
            ("Select the Ellipse tool (L) and, holding Shift, draw a circle concentric with the wreath image, slightly larger than the wreath's outer edge.", "L = Ellipse tool  ·  Shift-drag for a circle"),
            ("Set the ellipse Fill to None and Stroke to None — the path is a guide for the type, not a drawn ring.", "Fill None  ·  Stroke None"),
            ("Choose the Type on a Path tool (nested under the Type tool) and click on the top of the circle's edge when the cursor shows a small plus sign.", "Type on a Path tool (Shift+T)"),
            ("Type the strapline 'Fresh from our Orchard Road studio since 2024' and set it to 18 pt in the house display font.", ""),
            ("Switch to the Selection tool and drag the Center bracket to slide the whole strapline around the circle until it is centred at 12 o'clock.", "V = Selection tool  ·  drag the Center bracket"),
            ("Drag the Start and End brackets inwards to define the arc the text may occupy, so the words do not wrap round the bottom of the circle.", ""),
            ("Choose Type > Type on a Path > Options. Try each Effect — Rainbow, Skew, 3D Ribbon, Stair Step and Gravity — and settle on Rainbow for a masthead.", "Type > Type on a Path > Options"),
            ("In the same dialog set Align to Center and To Path Ascender, and tick Flip if the type needs to sit inside the curve.", "Options: Align Center · To Path Ascender · Flip"),
            ("Open the Character panel and increase Tracking to about 40 to counteract the crowding that the curve introduces at the baseline.", "Window > Type & Tables > Character  ·  Tracking 40"),
            ("Press W for Preview, zoom to 200% and confirm every letter sits evenly on the arc with no visible stagger before saving.", "W = Preview"),
        ],
        test="The strapline curves smoothly around the wreath as a single live text object — you can click into it with the Type tool and edit a word — and no stroke or fill from the guide path prints in Preview.",
        troubleshoot="Clicking on the path creates a new text frame instead of path type? You used the ordinary Type tool — switch to the Type on a Path tool and wait for the cursor's plus sign. If the text reads upside down along the bottom half, drag the flip indicator (the small marker at the centre bracket) across the path, or tick Flip in Type on a Path Options.",
    ),
    dict(
        num=14, topic=3,
        title="Refine Character and Paragraph Formatting for Readability",
        lo="LO3",
        objective="Refine drawings to meet project requirements by applying professional character and paragraph typography — kerning, tracking, leading, drop caps and nested styles (TSC A3, A4).",
        scenario=(
            "The **Harmony Petals** Seasonal Care Guide has come back from a readability review commissioned "
            "by Priya after two customers phoned to say the care instructions were \"hard to read on the bus\". "
            "The reviewer's report is blunt: the lines are too tightly leaded, the display headings have "
            "ugly gaps after the capital W, the opening paragraph has no visual entry point, and the "
            "ingredient runs-in are all set in the same weight so nothing stands out. Priya needs the type "
            "fixed before the guide goes back to **Sun Ray Printers** on Thursday."
        ),
        desc=(
            "Work through the typographic controls that separate amateur from professional pages: optical "
            "versus metrics kerning, tracking for display type, leading set as a paragraph value, a hanging "
            "drop cap, and a nested style that automatically formats the run-in lead of every paragraph."
        ),
        build="HP_Magazine_6.indd with optically kerned headings, a three-line drop cap on the opening paragraph, corrected leading throughout, and a nested style auto-formatting each run-in lead.",
        services="Adobe InDesign · Character panel · Paragraph panel · Kerning & Tracking · Drop Caps and Nested Styles · Glyphs panel",
        questions=[
            "Explain the difference between kerning and tracking, and state which one you would never apply to a full paragraph of body text and why.",
            "Metrics kerning uses pairs built into the font; Optical kerning is calculated by InDesign. When is Optical the better choice?",
            "Body text is 10 pt with 12 pt leading. What is the leading expressed as a ratio, and what happens to readability if the leading is reduced to 10 pt?",
            "A nested style formats the first n characters or up to a delimiter. Why is a nested style more maintainable than manually bolding each run-in lead?",
            "Your drop cap overlaps the text below it. Which two settings govern a drop cap, and which one do you change to fix the overlap?",
        ],
        steps=[
            ("Open HP_Magazine_6.indd and use Type > Show Hidden Characters to see the paragraph and space marks you will be working around.", "Type > Show Hidden Characters (Ctrl/Cmd+Alt+I)"),
            ("Click into the main heading with the Type tool, select all of it, and in the Character panel set Kerning to Optical to even out the gap after the capital W.", "Character panel > Kerning: Optical"),
            ("Place the cursor between two specific letters that still look loose and apply manual kerning of -20 with Alt/Option+Left Arrow.", "Alt/Option + Left Arrow = kern -20"),
            ("Select the display heading and reduce Tracking to about -15 so the large type sits tighter, as display type should.", "Character panel > Tracking -15"),
            ("Select the body text and set the type size to 10 pt with leading 13 pt, entered in the Character panel's leading field rather than left on Auto.", "Character panel > 10 pt / 13 pt"),
            ("Click in the opening paragraph and, in the Paragraph panel, set Drop Cap Number of Lines to 3 and Drop Cap One or More Characters to 1.", "Paragraph panel > Drop Cap 3 lines / 1 character"),
            ("Open Paragraph panel menu > Drop Caps and Nested Styles, tick Align Left Edge and Scale for Descenders to tuck the drop cap correctly against the text.", "Paragraph panel menu > Drop Caps and Nested Styles"),
            ("Create a character style named 'Run-in Lead' — bold, small caps, in the Harmony Petals green — with Window > Styles > Character Styles > New Character Style.", "Window > Styles > Character Styles > New Character Style"),
            ("Reopen Drop Caps and Nested Styles, click New Nested Style, and set 'Run-in Lead' through 1 Em Dash so every lead-in formats automatically.", "New Nested Style: Run-in Lead · through · 1 · Em Dash"),
            ("Use Type > Glyphs to replace the three typed hyphens in the care instructions with a proper en dash and confirm the nested style still triggers.", "Type > Glyphs"),
            ("Turn on View > Extras > Show Text Threads, scan for any newly created overset, and save the file.", "View > Extras > Show Text Threads"),
        ],
        test="Headings show even letter spacing at 300% zoom, body copy sits at 10/13, the opening paragraph carries a clean three-line drop cap, and every run-in lead formats itself the moment you type the em dash.",
        troubleshoot="Nested style not applying? The delimiter you chose does not exist in the text — check with Show Hidden Characters that an em dash, not a hyphen, ends each lead-in. If the drop cap collides with the following line, raise the Drop Cap Number of Lines or enable Scale for Descenders; do not fix it by adding manual returns.",
    ),
    dict(
        num=15, topic=3,
        title="Build and Apply a House Style Set",
        lo="LO3",
        objective="Refine drawings to project requirements by constructing a reusable paragraph, character and object style set that enforces a consistent house look across a publication (TSC A1, A4).",
        scenario=(
            "**Harmony Petals** has grown to three outlets and Priya now commissions two freelance designers "
            "alongside you. The three of you have produced the same brochure template three different ways: "
            "one used 11 pt Helvetica headings, one 12 pt Arial, one 11.5 pt with a different green. A "
            "franchise partner spotted the inconsistency and asked whether the brand guidelines were real. "
            "Priya wants a single locked style set built into the brochure template so that any designer "
            "who opens it produces identical typography, and a global colour change takes seconds not hours."
        ),
        desc=(
            "Convert manually formatted text into a structured style system: build paragraph styles with "
            "Based On inheritance, character styles for local emphasis, object styles for picture frames "
            "and callout boxes, then chain the styles with Next Style so a whole article formats in one "
            "command. Finally, prove the value of the system by changing one parent style."
        ),
        build="HP_Brochure_7.indd carrying a complete house style set — Body / Body First / Heading 1 / Heading 2 / Caption paragraph styles with Based On and Next Style, two character styles, and an object style for image frames.",
        services="Adobe InDesign · Paragraph Styles panel · Character Styles panel · Object Styles panel · Based On · Next Style · Quick Apply",
        questions=[
            "What does the Based On field actually inherit, and what happens to every child style when you change the parent's typeface?",
            "A style name in the Paragraph Styles panel shows a plus sign next to it. What does that mean and how do you clear it?",
            "Explain when you would use a character style rather than a second paragraph style.",
            "Next Style lets you format an entire article in one command. What must be true about the text's paragraph order for that to work?",
            "An object style can control fill, stroke, effects, text wrap and frame fitting. Why is that more valuable on a 40-page catalogue than on a one-page flyer?",
        ],
        steps=[
            ("Open HP_Brochure_7.indd and inspect the manually formatted text — note the three different heading treatments across the spread.", "Open HP_Brochure_7.indd"),
            ("Click into a well-formatted body paragraph, then open Window > Styles > Paragraph Styles and choose New Paragraph Style from the panel menu; the sampled formatting is pre-loaded.", "Window > Styles > Paragraph Styles > New Paragraph Style"),
            ("Name it 'Body', confirm 10 pt / 13 pt in Basic Character Formats, set a 3 mm Space After in Indents and Spacing, and click OK.", "Style Name: Body  ·  Space After 3 mm"),
            ("Create 'Body First' with Based On set to Body, and override only one thing — First Line Indent 0 mm — to prove inheritance.", "New Paragraph Style > Based On: Body"),
            ("Create 'Heading 1' at 20 pt bold in the Harmony Petals green, with Space Before 6 mm and Keep With Next 2 lines in the Keep Options pane.", "Keep Options > Keep with Next 2 lines"),
            ("Create 'Heading 2' Based On Heading 1 at 14 pt, then create 'Caption' at 8 pt italic.", ""),
            ("Edit Heading 1 and set Next Style to Body First; edit Body First and set Next Style to Body, so the chain runs automatically.", "Style Options > General > Next Style"),
            ("Select the whole article, right-click Heading 1 in the panel and choose 'Apply Heading 1 then Next Style' to format the article in one action.", "Right-click style > Apply [style] then Next Style"),
            ("Clear any remaining local overrides by Alt/Option-clicking the style name, and confirm the plus sign disappears from the panel.", "Alt/Option + click the style name"),
            ("Select a formatted image frame with a 0.5 pt green stroke and a 2 mm text wrap, then choose New Object Style from the Object Styles panel menu and name it 'Product Image'.", "Window > Styles > Object Styles > New Object Style"),
            ("Apply 'Product Image' to the other three picture frames, then edit the 'Body' style's typeface once and watch every dependent style update across the document.", ""),
        ],
        test="Every paragraph in the brochure shows a style name with no plus sign, all four image frames report the 'Product Image' object style, and changing the Body typeface propagates to Body First automatically.",
        troubleshoot="A style applies but the text does not change? Local overrides are winning — Alt/Option-click the style name to apply and clear overrides, or use Clear Overrides in the panel footer. If editing the parent does not change a child, the child's own definition overrides that attribute; delete the attribute from the child rather than editing it again.",
    ),
    dict(
        num=16, topic=3,
        title="Import Data and Build a Formatted Price Table",
        lo="LO3",
        objective="Refine a publication by importing tabular data, converting it to an InDesign table and formatting it with table and cell styles for repeatable, accurate presentation (TSC A3, A4).",
        scenario=(
            "**Harmony Petals** is publishing its 2026 corporate price list for hotel and events clients. "
            "Finance has supplied the 42-line rate card as a tab-delimited text file, TableData.txt, exported "
            "from their accounting system. The previous edition was retyped by hand into text frames; two "
            "prices were transcribed wrongly and Harmony Petals had to honour a S$2,800 quotation at the "
            "misprinted rate. Priya's instruction is explicit: no retyping, and the table must repeat its "
            "header row when it flows onto the second page."
        ),
        desc=(
            "Place a tab-delimited data file, convert the text to a table, then control it properly — "
            "setting header rows that repeat across frames, adjusting row and column dimensions, applying "
            "alternating fills, and locking the presentation into a table style plus cell styles so the "
            "next quarterly update is a five-minute job."
        ),
        build="Tables_A.indd containing the imported 2026 rate card as a live InDesign table with a repeating header row, alternating fills, and a saved 'Rate Card' table style plus 'Price Cell' and 'Header Cell' cell styles.",
        services="Adobe InDesign · File > Place · Table > Convert Text to Table · Table panel · Table Styles & Cell Styles panels · Table > Table Options",
        questions=[
            "The data arrives tab-delimited. Which two delimiters does Convert Text to Table ask for, and what does each map to?",
            "A header row is different from simply formatting the first row. What behaviour do you gain, and when does it matter?",
            "Explain the difference between a table style and a cell style, and the order in which InDesign applies them.",
            "Your table is too tall for the frame and shows a red overset symbol. List two legitimate fixes and one that would falsify the data.",
            "Finance will re-issue TableData.txt every quarter. What is the fastest correct way to refresh the table without rebuilding the formatting?",
        ],
        steps=[
            ("Open Tables_A.indd and draw a text frame inside the margins on page 1 with the Type tool.", "Open Tables_A.indd  ·  T = Type tool"),
            ("With the cursor in the frame choose File > Place, select TableData.txt, tick Show Import Options and confirm the delimiter is Tab.", "File > Place  ·  TableData.txt  ·  Show Import Options"),
            ("Select all the placed text and choose Table > Convert Text to Table with Column Separator: Tab and Row Separator: Paragraph.", "Table > Convert Text to Table"),
            ("Click into the first row, then choose Table > Convert Rows > To Header so the row repeats on every frame the table flows into.", "Table > Convert Rows > To Header"),
            ("Drag the frame's out port and flow the overset portion of the table to page 2; confirm the header row reappears at the top.", ""),
            ("Select all cells and choose Table > Cell Options > Text to set 1.5 mm inset on all four sides and vertical justification to Centre.", "Table > Cell Options > Text"),
            ("Select the price column and use the Control panel to right-align it, then set a fixed column width so figures align on the decimal.", "Control panel > Align Right"),
            ("Choose Table > Table Options > Alternating Fills, set Alternating Pattern to Every Other Row, and apply a 10% tint of the house green.", "Table > Table Options > Alternating Fills"),
            ("In Table > Table Options > Table Setup, set the Table Border to 0.5 pt and the row strokes to 0.25 pt so the rules do not overpower the data.", "Table > Table Options > Table Setup"),
            ("Create cell styles 'Header Cell' and 'Price Cell' from the formatted cells via Window > Styles > Cell Styles > New Cell Style.", "Window > Styles > Cell Styles > New Cell Style"),
            ("Create a table style named 'Rate Card' via Window > Styles > Table Styles, assigning the two cell styles to the Header and Body rows, then apply it to the whole table.", "Window > Styles > Table Styles > New Table Style"),
        ],
        test="All 42 rate lines appear as a live table with no retyped figures, the header row repeats at the top of page 2, and applying the 'Rate Card' table style to a fresh table reproduces the formatting exactly.",
        troubleshoot="Convert Text to Table produces one giant column? The file uses commas or multiple spaces rather than tabs — reopen Show Import Options and set the correct delimiter, or use Edit > Find/Change to normalise the separators first. A red overset marker in the bottom-right cell means the text does not fit that cell: increase the row height or reduce the cell inset — never delete characters from the price data.",
    ),
    dict(
        num=17, topic=3,
        title="Add Hyperlinks, Buttons and QR Codes for an Interactive Document",
        lo="LO3",
        objective="Refine a publication for a digital medium by adding hyperlinks, interactive buttons and generated QR codes that function reliably in the exported file (TSC A3, A4).",
        scenario=(
            "**Harmony Petals** is emailing a digital gift catalogue to its 4,200-strong corporate mailing "
            "list ahead of Chinese New Year. The first draft went out last year as a flat PDF; the "
            "e-commerce report showed only 11 clicks because none of the product names were linked and "
            "customers had to retype the URL. Priya wants every product to link to its online store page, "
            "a prominent 'Order Now' button on the cover, and a QR code on the back page so recipients "
            "reading a printed copy at the office can scan straight to the WhatsApp ordering line."
        ),
        desc=(
            "Turn a static catalogue into a working interactive document: create and manage URL and "
            "cross-reference hyperlinks with shared destinations, convert an object into a button with a "
            "rollover appearance and a Go To URL action, and generate a live vector QR code directly in "
            "InDesign. You then test everything before export."
        ),
        build="HP_InteractiveDoc_A.indd with every product name hyperlinked to its store URL, a working 'Order Now' button with a rollover state, and a scannable vector QR code on the back page.",
        services="Adobe InDesign · Hyperlinks panel · Buttons and Forms panel · Object > Generate QR Code · EPUB Interactivity Preview · Window > Interactive",
        questions=[
            "What is the difference between a hyperlink and a button in InDesign, and which export formats support each?",
            "Shared hyperlink destinations let one URL serve many links. Why does that matter when the store changes its domain?",
            "A button needs a Normal and a Rollover appearance. Why does a Rollover state improve conversion, and where does it have no effect at all?",
            "InDesign generates QR codes as live vector objects rather than placed images. What two practical advantages does that give the print production team?",
            "Your hyperlinks work in the InDesign preview but not in the exported PDF. Name the two most likely causes in the export settings.",
        ],
        steps=[
            ("Open HP_InteractiveDoc_A.indd and switch to the Interactive workspace so the relevant panels are visible.", "Window > Workspace > Interactive for PDF"),
            ("Select the first product name with the Type tool, open Window > Interactive > Hyperlinks and choose New Hyperlink from the panel menu.", "Window > Interactive > Hyperlinks > New Hyperlink"),
            ("Set Link To: URL, enter the store URL, tick Shared Hyperlink Destination, and assign the character style 'Hyperlink' so links look clickable.", "New Hyperlink > Link To: URL  ·  Shared Hyperlink Destination"),
            ("Repeat for the remaining products, reusing the shared destination from the URL dropdown where two products point at the same category page.", ""),
            ("Create an internal cross-reference from the contents page to the 'Delivery Terms' heading using New Cross-Reference in the Hyperlinks panel menu.", "Hyperlinks panel menu > New Cross-Reference"),
            ("Draw the 'Order Now' shape on the cover, select it, and choose Object > Interactive > Convert to Button.", "Object > Interactive > Convert to Button"),
            ("In Window > Interactive > Buttons and Forms, name the button 'OrderNow', set Event to On Release or Tap and add the action Go To URL with the store address.", "Buttons and Forms > Event: On Release or Tap  ·  Action: Go To URL"),
            ("Click [Rollover] in the Appearance list and change the fill to the darker house green so the button responds to the cursor.", "Buttons and Forms > Appearance > [Rollover]"),
            ("Go to the back page, choose Object > Generate QR Code, select Type: Web Hyperlink and enter the WhatsApp ordering link, then set the colour swatch.", "Object > Generate QR Code"),
            ("Click OK and place the loaded QR cursor in a frame at least 25 x 25 mm so it remains scannable in print.", ""),
            ("Test everything with Window > Interactive > EPUB Interactivity Preview, click Play, and verify each link, the button rollover and the cross-reference.", "Window > Interactive > EPUB Interactivity Preview"),
        ],
        test="Every product name opens its store page and the 'Order Now' button changes colour on rollover in the EPUB Interactivity Preview, and a phone camera scanning the QR code opens the WhatsApp ordering line.",
        troubleshoot="Links dead in the exported PDF? You exported Adobe PDF (Print) with Hyperlinks unticked — re-export using File > Export > Adobe PDF (Interactive), or tick Include Hyperlinks in the Print PDF's General pane. A QR code that will not scan is almost always too small or too low-contrast: enlarge it past 25 mm and keep it a dark colour on a plain light background with clear space around it.",
    ),
    dict(
        num=18, topic=3,
        title="Animate Objects with Motion Presets and Page Transitions",
        lo="LO3",
        objective="Refine a digital publication by applying animation, motion paths, timing controls and page transitions appropriate to the delivery medium (TSC A3, A4).",
        scenario=(
            "**Harmony Petals** sponsors a children's reading corner at a Bukit Timah community library and "
            "has commissioned an animated version of *The Little Red Hen* to play on the touchscreen kiosk. "
            "The library's IT officer reports that the current version \"plays everything at once and then "
            "stops\" — every object animates on page load with no sequencing, so children cannot follow the "
            "story. Priya also wants a Harmony Petals branded slide-in on the final page. The kiosk goes "
            "live at the school-holiday launch in nine days."
        ),
        desc=(
            "Study a finished animated file to see how sequencing is constructed, then build your own: "
            "apply motion presets, convert a drawn path into a motion path, control the event, duration "
            "and play order in the Timing panel, and finish with a page transition — always weighing "
            "whether the animation serves the reader or merely decorates."
        ),
        build="An animated Harmony Petals page in HP_Magazine_7.indd with at least three sequenced animations, one custom motion path and a page transition, benchmarked against Little_Red_Hen-anim-after.indd.",
        services="Adobe InDesign · Animation panel · Timing panel · Object > Interactive > Convert to Motion Path · Page Transitions panel · EPUB Interactivity Preview",
        questions=[
            "Animation in InDesign exports to some formats and is silently discarded by others. Which formats retain it, and what does that mean for a client who also wants a print version?",
            "The Animation panel offers Event choices such as On Page Load, On Click and On Roll Over. Which is appropriate for an unattended kiosk, and why?",
            "Explain the difference between the Duration and the Delay of an animation, and how the Timing panel uses each to sequence a scene.",
            "You drew a curved path and converted it to a motion path. What happens to the animation if you later reshape that path with the Direct Selection tool?",
            "Page transitions can be applied to one page or all pages. Give a design reason for restricting a transition to a single page rather than the whole document.",
        ],
        steps=[
            ("Open Little_Red_Hen-anim-after.indd and preview it with Window > Interactive > EPUB Interactivity Preview to see a properly sequenced animation.", "Open Little_Red_Hen-anim-after.indd  ·  EPUB Interactivity Preview"),
            ("Open the Timing panel and study how the delays stagger the objects; note which animations are grouped to play together.", "Window > Interactive > Timing"),
            ("Open HP_Magazine_7.indd, select the hero product image and open Window > Interactive > Animation.", "Window > Interactive > Animation"),
            ("Apply the preset 'Fly in from Left', set Event to On Page Load, Duration 1 second, and Speed to Ease Out.", "Animation panel > Preset: Fly in from Left"),
            ("Select the headline text frame, apply 'Fade In', and set its Duration to 0.75 seconds.", "Animation panel > Preset: Fade In"),
            ("Draw a gentle curve across the page with the Pen tool, then select both the curve and a petal graphic and choose Object > Interactive > Convert to Motion Path.", "Object > Interactive > Convert to Motion Path"),
            ("In the Animation panel adjust the motion path animation's Duration to 2 seconds and tick Animate: From Current Appearance.", "Animation panel > Animate: From Current Appearance"),
            ("Open the Timing panel, drag the three animations into the order hero image, headline, petal, and set a 0.5 second Delay on the headline and 1 second on the petal.", "Window > Interactive > Timing  ·  set Delay values"),
            ("Select two animations in the Timing panel and click Play Together at the panel footer to see the difference between sequential and simultaneous play.", "Timing panel > Play Together"),
            ("Open Window > Interactive > Page Transitions, apply the Push transition to the final page only, and set Direction and Speed.", "Window > Interactive > Page Transitions"),
            ("Preview the whole document again in EPUB Interactivity Preview and cut any animation that does not help the reader follow the page.", "EPUB Interactivity Preview > Play"),
        ],
        test="In EPUB Interactivity Preview the three objects animate in the intended order with visible delays between them, the petal follows the drawn curve, and the page transition fires only on the final page.",
        troubleshoot="Nothing animates in preview? The preview is set to Preview Spread rather than Preview Document, or the objects were animated on a parent page — animation on parent pages does not play. Animation missing from your exported file means you exported a Print PDF or a reflowable EPUB; use File > Export > Adobe PDF (Interactive), Publish Online or a fixed-layout EPUB instead.",
    ),
    dict(
        num=19, topic=3,
        title="Preflight, Package and Export a Print-Ready PDF/X",
        lo="LO3",
        objective="Refine and validate a document against print production requirements, then package the job and export a press-ready PDF/X file with correct bleed and marks (TSC A1, A3, A4).",
        scenario=(
            "**Sun Ray Printers** has rejected the Harmony Petals magazine file two hours before the press "
            "booking. Their prepress report lists four faults: one image is linked to a designer's desktop "
            "and is missing, a second image has an effective resolution of 96 ppi, there is overset text in "
            "a caption frame, and two fonts are not embedded. The press slot costs S$1,150 and rolls over to "
            "next Tuesday if missed. Priya needs a clean preflight, a proper package for the printer, and a "
            "PDF/X-1a file supplied within the hour."
        ),
        desc=(
            "Use InDesign's live Preflight to define and run a production profile, resolve every error in "
            "the Links panel, clear overset text, then package the job with fonts and links and export a "
            "PDF/X-1a file carrying 3 mm bleed and crop marks — the exact deliverable a commercial litho "
            "printer expects."
        ),
        build="A Harmony Petals package folder containing the .indd, Links, Document Fonts and an instructions file, plus HP_Magazine_7_PRINT.pdf exported as PDF/X-1a:2001 with 3 mm bleed and crop marks.",
        services="Adobe InDesign · Preflight panel & profiles · Links panel · File > Package · File > Export > Adobe PDF (Print) · PDF/X-1a:2001",
        questions=[
            "The default [Basic] preflight profile passes a file that the printer rejects. Why, and what should you do about it?",
            "Explain effective resolution versus actual resolution, and why scaling a 300 ppi image to 200% is a production error.",
            "File > Package creates a Document Fonts folder. What licensing condition governs your use of those fonts, and who may open them?",
            "What is the difference between PDF/X-1a and PDF/X-4, and which would you supply for a job with live transparency?",
            "You set 3 mm bleed in Document Setup but the exported PDF has none. Which specific export setting was missed?",
        ],
        steps=[
            ("Open HP_Magazine_7.indd and open Window > Output > Preflight; note the red error count in the status bar.", "Window > Output > Preflight"),
            ("From the Preflight panel menu choose Define Profiles, create a profile named 'Sun Ray Litho', and enable Missing Links, Image Resolution minimum 300 ppi, Overset Text and Non-Proportional Scaling.", "Preflight panel menu > Define Profiles"),
            ("Set the Profile dropdown to 'Sun Ray Litho' and expand the error list to see each offending page.", ""),
            ("Open Window > Links, select the missing link, click Relink and navigate to the correct file in the Links folder.", "Window > Links > Relink"),
            ("Select the low-resolution image in the Links panel and read Effective PPI in the Link Info section; replace it with the 300 ppi version supplied by the photographer.", "Links panel > Link Info > Effective PPI"),
            ("Double-click the Overset Text error in Preflight to jump to the caption frame, then fix it by enlarging the frame or editing the copy — not by deleting the frame.", "Preflight > double-click error to navigate"),
            ("Use Type > Find Font to confirm every font is available and, if necessary, replace the two unembedded fonts with licensed equivalents.", "Type > Find Font"),
            ("Re-run preflight and confirm the status bar reads 'No errors' before going any further.", ""),
            ("Choose File > Package, review the Summary, then click Package and tick Copy Fonts, Copy Linked Graphics, Update Graphic Links in Package and Include Fonts and Links From Hidden Content.", "File > Package"),
            ("Choose File > Export, set Format to Adobe PDF (Print), name the file HP_Magazine_7_PRINT.pdf and click Save.", "File > Export > Adobe PDF (Print)"),
            ("In the Export dialog select the [PDF/X-1a:2001] preset, tick Crop Marks and Use Document Bleed Settings in Marks and Bleeds, then open the PDF and check the artwork extends 3 mm past the crop marks.", "Marks and Bleeds > Crop Marks · Use Document Bleed Settings"),
        ],
        test="The Preflight panel reports 'No errors' against the Sun Ray Litho profile, the package folder contains the document, Links and Document Fonts, and the exported PDF/X-1a shows crop marks with artwork bleeding 3 mm beyond the trim.",
        troubleshoot="Preflight still reports errors after relinking? The panel caches until you re-run it — toggle the profile or click the panel refresh. If the exported PDF has crop marks but no bleed, you ticked Crop Marks without ticking Use Document Bleed Settings, so the marks sit on a document that was set to 0 mm bleed; fix the bleed in File > Document Setup and export again.",
    ),
    dict(
        num=20, topic=3,
        title="Export for Digital Delivery — Interactive PDF, EPUB and Publish Online",
        lo="LO3",
        objective="Identify and select the appropriate digital medium for a publication and export to it correctly, choosing between interactive PDF, reflowable EPUB, fixed-layout EPUB and Publish Online (TSC A1, A3, A4).",
        scenario=(
            "The animated *Little Red Hen* is finished and **Harmony Petals** now has three audiences for the "
            "same file. The community library kiosk needs the animation intact. The National Library Board "
            "wants a copy for its e-lending catalogue that must reflow on a 6-inch e-reader with adjustable "
            "type size. Priya wants a link she can WhatsApp to the board of directors this afternoon without "
            "sending a 40 MB attachment, and she wants their comments back in one place. Exporting the wrong "
            "format to the wrong audience last year produced an EPUB with the illustrations stacked "
            "randomly and an embarrassing complaint from the library."
        ),
        desc=(
            "Match each audience to the correct export path and produce all of them from one source file: "
            "an interactive PDF for the kiosk, a reflowable EPUB with a correct Articles-panel reading order "
            "and object export metadata for the e-reader, a fixed-layout EPUB to preserve the animation, "
            "a Publish Online link for the board, and a Share for Review link to collect comments."
        ),
        build="Four exports from Little_Red_Hen-anim-after.indd — an interactive PDF, a reflowable EPUB, a fixed-layout EPUB and a Publish Online URL — plus a Share for Review link with at least one comment received.",
        services="Adobe InDesign · File > Export > Adobe PDF (Interactive) · EPUB (Reflowable) & EPUB (Fixed Layout) · Articles panel · Object Export Options · Publish Online · Share for Review",
        questions=[
            "State the single most important difference between a reflowable and a fixed-layout EPUB, and give one publication type that suits each.",
            "The Articles panel controls EPUB reading order. What determines the order if you never open that panel, and why is that risky on a designed spread?",
            "Alt text is set in Object Export Options. Beyond accessibility compliance, what practical benefit does it deliver?",
            "Publish Online places the document on Adobe's servers with a public URL. What are the confidentiality implications for a client's unreleased pricing, and how would you manage them?",
            "A client wants comments on a draft. Compare Share for Review with emailing a PDF, in terms of version control and consolidating feedback.",
        ],
        steps=[
            ("Open Little_Red_Hen-anim-after.indd and list the three audiences and the format each one needs before exporting anything.", "Open Little_Red_Hen-anim-after.indd"),
            ("Choose File > Export, set Format to Adobe PDF (Interactive), and in the dialog tick Include All in Hyperlinks, set Page Transitions to From Document, and enable Interactive Elements: Include All.", "File > Export > Adobe PDF (Interactive)"),
            ("Open the exported PDF in Acrobat and confirm the buttons and page transitions still function.", ""),
            ("Open Window > Articles and drag the story frames into the panel in true reading order, ticking Include When Exporting.", "Window > Articles"),
            ("Select each illustration and choose Object > Object Export Options; on the Alt Text tab set the source to Custom and write a meaningful description.", "Object > Object Export Options > Alt Text"),
            ("On the EPUB and HTML tab of the same dialog set Custom Rasterization to 150 ppi PNG so the images travel well on an e-reader.", "Object Export Options > EPUB and HTML"),
            ("Choose File > Export > EPUB (Reflowable). In General set Order to Same as Articles Panel, and in Text set Bullets and Numbers to Map to Unordered Lists.", "File > Export > EPUB (Reflowable)"),
            ("Open the reflowable EPUB in an EPUB reader, change the reader's text size, and confirm the text reflows and the alt text is present.", ""),
            ("Export again with File > Export > EPUB (Fixed Layout), ticking Include Interactive Elements, and confirm the animation survives.", "File > Export > EPUB (Fixed Layout)"),
            ("Choose File > Publish Online, give the document a title and description, choose the pages to include, publish, and copy the generated URL.", "File > Publish Online"),
            ("Choose File > Share for Review, create the review link, send it to a classmate acting as Priya, then open Window > Comments to read their returned comment and mark it resolved.", "File > Share for Review  ·  Window > Comments"),
        ],
        test="The interactive PDF plays its transitions, the reflowable EPUB reflows and reads in the Articles-panel order with alt text intact, the fixed-layout EPUB retains the animation, and the Publish Online and Share for Review links both open with a comment visible in the Comments panel.",
        troubleshoot="EPUB content appearing in a jumbled order is the classic symptom of an unset reading order — populate the Articles panel and set Order to Same as Articles Panel on export. If your animation is missing, you exported the reflowable EPUB, which discards interactivity: use fixed layout, an Interactive PDF or Publish Online instead. Publish Online greyed out means it is disabled in Preferences or by your organisation's Creative Cloud administrator.",
    ),
]
