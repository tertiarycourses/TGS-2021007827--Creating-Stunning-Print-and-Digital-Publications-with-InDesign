"""
Topic 2 — Basic InDesign Drawing Techniques.
Text & threading · Frames & paths · Graphics & colour · Manage objects.
Hands-on activities. Global contiguous lab numbering across all three domains.

Each activity is a realistic workplace case study: a named client, a real brief,
a deliverable and a verifiable outcome — the same shape as the Practical
Performance assessment so the class rehearses exactly what is assessed.
"""

DOMAIN2 = [
    dict(
        num=5, topic=2,
        title="Create Text Frames and Import Client Copy from Word",
        lo="LO2",
        objective="Determine the text areas of a layout and select the appropriate import method to bring supplied client copy into InDesign without corrupting the document's typography (TSC A2, A3).",
        scenario=(
            "**Harmony Petals** is preparing a three-fold brochure for its new Tiong Bahru outlet. "
            "Priya has just e-mailed **HP_Brochure_Mission.docx** — the company mission statement written "
            "in Word by the founder, complete with Calibri 11 pt, blue headings and tracked changes. "
            "The last time a colleague pasted Word copy straight into a layout, the Calibri styling "
            "overrode the brochure's typeface and Sun Ray Printers flagged a missing font at output, "
            "delaying the job by two days. "
            "Priya needs the mission text placed today, in the brochure's own typography, and she wants "
            "the remaining panels filled with dummy text so she can judge the visual balance before the "
            "final copy arrives on Friday."
        ),
        desc=(
            "Draw and resize text frames to the brochure's column structure, then import the supplied Word "
            "file twice — once retaining its Word formatting and once discarding it — so you can see and "
            "explain the difference. You then fill the unwritten panels with placeholder text and inspect "
            "the frame's own options: inset, vertical justification and columns."
        ),
        build="HP_Brochure_1.indd with the client mission statement placed into a correctly sized text frame using Remove Styles and Formatting, plus the remaining panels filled with placeholder text and a 3 mm text inset applied.",
        services="Adobe InDesign · Type tool · File > Place · Import Options · Type > Fill with Placeholder Text · Text Frame Options",
        questions=[
            "Priya's Word file carries its own fonts and colours. What are the practical consequences of choosing 'Preserve Styles and Formatting' over 'Remove Styles and Formatting' for a job going to litho print?",
            "You drag a text frame with the Selection tool and the type inside gets squashed. What did you do wrong, and which tool or modifier avoids it?",
            "What is the difference between drawing a text frame with the Type tool and converting an existing graphic frame into a text frame?",
            "Placeholder text is not real copy. Why does a professional designer still use it, and at what point in the workflow must it be removed?",
            "A text frame's Inset Spacing is set to 0 mm and the type touches the frame edge, which becomes visible when a fill colour is applied. Explain why inset — not simply moving the frame — is the correct fix.",
        ],
        steps=[
            ("Open HP_Brochure_1.indd from the Topic 2 lab folder and identify the three panel columns established by the guides.", "Open HP_Brochure_1.indd"),
            ("Select the Type tool (T) and drag a text frame inside the left panel, snapping to the column guides top and bottom.", "T = Type tool"),
            ("With the insertion point in the frame, choose File > Place, tick Show Import Options, and select HP_Brochure_Mission.docx.", "File > Place  ·  Show Import Options ON"),
            ("In the Microsoft Word Import Options dialog choose Remove Styles and Formatting from Text and Tables, and set Manual Page Breaks to No Breaks. Click OK.", "Import Options > Remove Styles and Formatting from Text and Tables"),
            ("Undo the place (Ctrl/Cmd+Z), repeat the import choosing Preserve Styles and Formatting instead, and compare the two results on screen before undoing again and re-placing with Remove Styles.", "Ctrl/Cmd+Z"),
            ("Click into the middle panel with the Type tool, draw a second frame, and choose Type > Fill with Placeholder Text to flow dummy copy for layout assessment.", "Type > Fill with Placeholder Text"),
            ("Switch to the Selection tool (V) and resize a frame by dragging a corner handle; then hold Ctrl/Cmd while dragging the same handle and observe that the type now scales — undo that scaling.", "V = Selection  ·  Ctrl/Cmd+drag scales content"),
            ("With the mission frame selected, choose Object > Text Frame Options and set Inset Spacing to 3 mm on all four sides.", "Object > Text Frame Options  ·  Inset 3 mm"),
            ("In the same dialog set Vertical Justification Align to Top, then experiment with Center and Justify to see how each redistributes the copy in the frame.", "Text Frame Options > General > Vertical Justification"),
            ("Still in Text Frame Options, set Columns Number to 1 for the panel, then click Preview to confirm the result before clicking OK.", "Text Frame Options > Columns"),
            ("Save the file and note in the Links panel that a placed Word file appears as a link only if 'Create Links When Placing Text and Spreadsheet Files' was enabled in Preferences.", "File > Save  ·  Window > Links"),
        ],
        test="The mission statement sits in the left panel in the brochure's own typeface with no Calibri present in Type > Find/Replace Font, the frame shows a 3 mm inset, and the middle panel is filled with placeholder text.",
        troubleshoot="If blue Word headings and Calibri survive the import, you left 'Preserve Styles and Formatting' selected — undo, re-place with Show Import Options ticked and choose Remove Styles and Formatting. If the type appears stretched, you Ctrl/Cmd-dragged a corner handle and scaled the content: undo, or reset with Object > Transform > Clear Transformations.",
    ),
    dict(
        num=6, topic=2,
        title="Thread Text Across Frames and Resolve Overset Copy",
        lo="LO2",
        objective="Refine a text layout by threading a story across multiple frames and pages, and diagnose and resolve overset text so no client copy is lost at output (TSC A2, A4).",
        scenario=(
            "The Bellow Flower feature article, **HP_Brochure_BellowFlower.docx**, runs to about 900 words "
            "and must flow across four panels of the **Harmony Petals** brochure. "
            "Yesterday the file went to **Sun Ray Printers** with a red overset marker nobody noticed; the "
            "proof came back with the last paragraph of the founder's story simply missing, and the client "
            "refused to approve it. Priya has asked you to re-do the flow properly and to demonstrate, in "
            "front of her, that no copy is hidden. "
            "She also wants the article to autoflow so that if the copywriter adds two more paragraphs on "
            "Friday, the brochure extends itself rather than silently truncating."
        ),
        desc=(
            "Import a long story and thread it manually between frames using the in and out ports, then "
            "repeat the flow using semi-autoflow and autoflow with modifier keys. You learn to spot the red "
            "plus sign of overset text, use Story Editor and Preflight to prove nothing is lost, and unthread "
            "a frame without deleting its content."
        ),
        build="HP_Brochure_2.indd with the Bellow Flower story threaded across four frames, zero overset text, visible thread indicators, and a Preflight panel reporting no errors.",
        services="Adobe InDesign · In/out ports · Autoflow (Shift-click) · Semi-autoflow (Alt/Opt-click) · View > Extras > Show Text Threads · Edit > Edit in Story Editor · Preflight panel",
        questions=[
            "A red plus sign appears in the out port of a text frame. Explain precisely what it means and name three different ways to resolve it.",
            "Compare manual flow, semi-autoflow and autoflow. Which modifier key triggers each, and in what production situation would you deliberately choose the slowest of the three?",
            "You delete a threaded frame in the middle of a story. What happens to the text it contained, and why?",
            "Why is Story Editor a more reliable way to find overset copy than scrolling the layout looking for red markers?",
            "Priya's overset paragraph was invisible on screen but caused a rejected proof. What preflight or handover check should be standard before any file leaves the studio?",
        ],
        steps=[
            ("Open HP_Brochure_2.indd and turn on View > Extras > Show Text Threads so the links between frames are visible when frames are selected.", "View > Extras > Show Text Threads"),
            ("With nothing selected, choose File > Place and select HP_Brochure_BellowFlower.docx; the cursor becomes a loaded text icon.", "File > Place  ·  HP_Brochure_BellowFlower.docx"),
            ("Click once inside the first panel guide area to place the story into a single frame; note the red plus sign in the out port at the lower right.", ""),
            ("Switch to the Selection tool (V), click the red out port once — the cursor reloads — then click or drag in the second panel to thread the continuation.", "V, then click the out port"),
            ("Repeat for the third panel to confirm you can control the flow frame by frame.", ""),
            ("Undo back to the loaded cursor, then hold Alt (Windows) or Option (macOS) and click to use semi-autoflow, which keeps the cursor loaded after each placement.", "Alt/Opt-click = semi-autoflow"),
            ("Undo again and hold Shift while clicking to autoflow the whole story, letting InDesign add frames and pages until the copy is exhausted.", "Shift-click = autoflow"),
            ("Select a middle frame and choose Edit > Edit in Story Editor; scroll to the end and confirm no text sits below the overset depth line.", "Edit > Edit in Story Editor  ·  Ctrl/Cmd+Y"),
            ("Open Window > Output > Preflight, enable it, and confirm the [Basic] profile reports 0 errors with no overset text entry.", "Window > Output > Preflight"),
            ("Select the final frame and click its in port, then click the out port of the preceding frame to break the thread; observe that the text re-flows back rather than being deleted.", "Click in port to unthread"),
            ("Re-thread the final frame, then use Layout > Pages and the Pages panel to verify no unintended pages were added by autoflow. Save the file.", "File > Save"),
        ],
        test="Preflight reports 0 errors, Story Editor shows no copy below the overset line, and selecting any frame displays continuous thread arrows through all four panels.",
        troubleshoot="If clicking the out port creates a brand-new empty frame instead of continuing the story, you clicked with the Type tool rather than the Selection tool — press V first. If autoflow silently added six unwanted pages, you Shift-clicked with Smart Text Reflow enabled; undo, reduce the type size or enlarge the frames, then re-flow.",
    ),
    dict(
        num=7, topic=2,
        title="Place Graphics, Manage Links and Control Effective Resolution",
        lo="LO2",
        objective="Identify and select appropriate image mediums and formats for print, place them into frames with correct fitting, and verify effective PPI meets the printer's requirement (TSC A3, A4).",
        scenario=(
            "**Harmony Petals** is producing its first 16-page magazine, *Petals Quarterly*, for distribution "
            "at all three outlets. The photographer has supplied images at 300 ppi, but a junior designer "
            "enlarged one bouquet photograph to fill a full page and the printed proof came back visibly "
            "pixelated — **Sun Ray Printers** confirmed the effective resolution had dropped to 96 ppi. "
            "That single page cost a S$480 reprint. "
            "Priya now requires every image in the magazine to be checked for effective PPI and every link "
            "to be present and up to date before the file is handed over."
        ),
        desc=(
            "Place images into existing and new frames, learn the distinction between the frame and its "
            "content, apply the five fitting options, and use the Links panel to audit every placed graphic "
            "for status, actual PPI and effective PPI. You then deliberately break a link and repair it."
        ),
        build="HP_Magazine_1.indd with all images placed, fitted with Fill Frame Proportionally, every link showing OK status, and a documented effective-PPI check confirming 300 ppi or better on every print image.",
        services="Adobe InDesign · File > Place · Links panel · Object > Fitting · Frame Fitting Options · Content Grabber · Info panel",
        questions=[
            "Distinguish actual PPI from effective PPI. Which one determines print quality, and why?",
            "An image is placed at 300 ppi and then scaled to 200%. What is its effective PPI, and is it acceptable for litho printing?",
            "InDesign links to images rather than embedding them. State two advantages of linking and one risk it introduces at handover.",
            "Compare Fit Content Proportionally with Fill Frame Proportionally. Which one can leave white space, which one can crop, and how do you decide?",
            "Why would a designer choose a PSD or TIFF for a print magazine cover but a PNG or JPEG for a web banner?",
        ],
        steps=[
            ("Open HP_Magazine_1.indd and open Window > Links so the panel is visible for the whole exercise.", "Open HP_Magazine_1.indd  ·  Window > Links"),
            ("Select an empty graphic frame, then choose File > Place and select a supplied bouquet image so it lands inside that frame.", "File > Place"),
            ("With nothing selected, place a second image and drag with the loaded cursor to draw a new frame at the exact size you want.", "File > Place, then drag"),
            ("Use the Selection tool (V) on the frame, then click the doughnut-shaped Content Grabber at the centre to select the image inside; move the image within the frame without moving the frame.", "V  ·  Content Grabber"),
            ("Apply Object > Fitting > Fill Frame Proportionally to the first image, then try Fit Content Proportionally and Fit Frame to Content to compare the outcomes.", "Object > Fitting > Fill Frame Proportionally"),
            ("Select a frame and choose Object > Fitting > Frame Fitting Options; set Fitting to Fill Frame Proportionally and Align From the centre so future placements auto-fit.", "Object > Fitting > Frame Fitting Options"),
            ("In the Links panel, expand the link information panel at the bottom and read Actual PPI and Effective PPI for each placed image.", "Links panel > link info"),
            ("Scale one image to 200% with the Selection tool and re-read Effective PPI; confirm it has halved and undo the scaling.", "Ctrl/Cmd+Z"),
            ("Outside InDesign, rename one source image file, return to InDesign and observe the red missing-link icon in the Links panel.", ""),
            ("Select the missing link, click Relink, navigate to the renamed file and restore it; confirm the status changes to OK.", "Links panel > Relink"),
            ("Sort the Links panel by Effective PPI, confirm no print image falls below 300 ppi, and save the file.", "Links panel menu > Sort by Effective PPI"),
        ],
        test="The Links panel shows every image with an OK status, no missing or modified icons, and an effective PPI of 300 or higher for every image destined for litho print.",
        troubleshoot="If clicking a fitted image only moves the frame and leaves the picture behind, you are dragging the frame with the Selection tool — click the Content Grabber, or use the Direct Selection tool (A), to move the content instead. A yellow warning triangle in the Links panel means the source file was edited since placing: select it and click Update Link before output.",
    ),
    dict(
        num=8, topic=2,
        title="Draw Custom Paths with the Pen and Pencil Tools",
        lo="LO2",
        objective="Establish drawing requirements and construct precise vector paths using anchor points, straight segments and Bezier curves to produce artwork to specification (TSC A1, A4).",
        scenario=(
            "*Petals Quarterly* needs a custom petal-shaped motif to sit behind the contents page, and a "
            "hand-drawn 'Harmony' signature flourish for the editor's letter. "
            "The freelance illustrator quoted S$350 and a four-day turnaround; Priya has neither the budget "
            "nor the time, because the magazine goes to **Sun Ray Printers** on Thursday. "
            "She has asked whether the motif can be drawn natively in InDesign so it stays fully editable "
            "and prints as sharp vector artwork at any size, rather than as a raster file that would soften "
            "when scaled up for the outlet window posters."
        ),
        desc=(
            "Build vector artwork directly in InDesign: straight-edge paths, smooth curves, corner-to-smooth "
            "conversions, open versus closed paths and freehand shapes. You use the Pen tool for precision "
            "and the Pencil and Smooth tools for organic forms, then refine the result with the Direct "
            "Selection tool."
        ),
        build="A closed, editable petal motif and an open signature flourish drawn as native InDesign vector paths in HP_Magazine_1.indd, with clean anchor points and no stray open segments.",
        services="Adobe InDesign · Pen tool (P) · Add/Delete/Convert Anchor Point · Pencil tool (N) · Smooth tool · Direct Selection tool (A) · Stroke panel",
        questions=[
            "What is the difference between a corner point and a smooth point, and how do you convert one to the other while drawing?",
            "You want a curve to end and a straight line to begin from the same anchor. Describe the exact sequence of clicks and modifier keys.",
            "Explain the relationship between a direction handle's length and the shape of the curve it controls.",
            "When would you choose the Pencil tool over the Pen tool, and what is the production cost of that choice in terms of anchor points?",
            "The motif must also be used on a 2-metre outlet window poster. Why does drawing it as a vector path in InDesign solve a problem that a 300 ppi raster file cannot?",
        ],
        steps=[
            ("Open HP_Magazine_1.indd, navigate to the contents page and create a new layer named 'Motif' in Window > Layers so the drawing stays separate from the layout.", "Window > Layers > New Layer"),
            ("Select the Pen tool (P) and click four times without dragging to draw a closed straight-edged shape, clicking back on the first anchor to close it.", "P = Pen tool"),
            ("Draw a second path, this time click-and-dragging at each anchor to pull out direction handles and create smooth curves for the petal outline.", ""),
            ("While drawing, hold Alt/Option and drag a direction handle to break it, converting a smooth point into a corner so a curve meets a straight segment.", "Alt/Opt-drag = convert direction handle"),
            ("Close the petal path by returning to the first anchor point until a small circle appears beside the cursor, then click.", ""),
            ("Switch to the Direct Selection tool (A), click an individual anchor point and drag its direction handles to refine the petal shape.", "A = Direct Selection tool"),
            ("Use the Pen tool over an existing segment to add an anchor point, and over an existing point to delete one; then use Object > Paths > Open Path on a copy to see the effect.", "Pen tool over segment = Add Anchor Point"),
            ("Select the Pencil tool (N), nested under the Pen tool, and draw the 'Harmony' flourish freehand in a single stroke.", "N = Pencil tool"),
            ("Choose the Smooth tool from the same flyout and drag along the flourish to reduce excess anchor points and even out the line.", "Smooth tool"),
            ("Open Window > Stroke, set the flourish to 1.5 pt with round caps and round joins, and apply a stroke colour from Swatches.", "Window > Stroke  ·  1.5 pt, round cap/join"),
            ("Select both drawings, zoom to 400% and inspect for stray or doubled anchor points; delete any with the Pen tool, then save the file.", "Ctrl/Cmd+4 = 400% zoom"),
        ],
        test="The petal motif is a single closed path that accepts a fill colour, the flourish is an open stroked path, and the Direct Selection tool shows clean, evenly spaced anchor points with no duplicates.",
        troubleshoot="If a fill colour will not apply to the petal, the path never closed — select it and choose Object > Paths > Close Path. If the Pencil line has dozens of anchor points and looks lumpy, double-click the Pencil tool and raise the Smoothness value before redrawing, or run the Smooth tool along the existing path.",
    ),
    dict(
        num=9, topic=2,
        title="Combine Shapes with Pathfinder and Wrap Text Around a Clipping Path",
        lo="LO2",
        objective="Refine drawings to meet project requirements by combining shapes into compound paths, applying Pathfinder operations and wrapping body copy around an irregular image silhouette (TSC A2, A4).",
        scenario=(
            "The *Petals Quarterly* feature spread on orchids needs the body copy to hug the outline of a "
            "cut-out orchid photograph rather than sit in a plain rectangle. "
            "The supplied JPEG has a white background, and Priya's first attempt produced a rectangular "
            "text wrap that left an ugly white box in the middle of the column — a client reviewer described "
            "it as \"looking like a mistake\". "
            "She also needs a two-colour Harmony Petals logo mark built from overlapping circles, where the "
            "overlap must knock through to reveal the background rather than print as a solid. "
            "The spread is due at **Sun Ray Printers** on Thursday afternoon."
        ),
        desc=(
            "Combine and subtract shapes using compound paths and the Pathfinder panel, then apply text wrap "
            "in all its variants — including wrapping around an object shape derived from a Photoshop path or "
            "detected edges — and control the wrap offset so the type never touches the image."
        ),
        build="HP_Magazine_2.indd with a knock-through compound-path logo mark, a Pathfinder-combined decorative shape, and body copy wrapping cleanly around the orchid silhouette with a 3 mm offset.",
        services="Adobe InDesign · Object > Paths > Make Compound Path · Window > Object & Layout > Pathfinder · Window > Text Wrap · Object > Clipping Path > Options · Detect Edges",
        questions=[
            "What visually distinguishes a compound path from two shapes simply grouped together, and why does the distinction matter for a printed logo?",
            "Compare Pathfinder Subtract with Exclude Overlap. What is the difference in the resulting path, and when is each correct?",
            "Text wrap is applied to an image but the type in one frame ignores it completely. Name two settings that would cause this.",
            "Explain the difference between a clipping path created in Photoshop and one generated in InDesign by Detect Edges, and which you would trust for a client logo.",
            "Why should Text Wrap offset be set in the Text Wrap panel rather than by nudging the text frame away from the image?",
        ],
        steps=[
            ("Open HP_Magazine_2.indd and go to the orchid feature spread.", "Open HP_Magazine_2.indd"),
            ("Draw two overlapping circles with the Ellipse tool (L), select both, and choose Object > Paths > Make Compound Path — the overlap knocks through to reveal the page behind.", "Object > Paths > Make Compound Path  ·  Ctrl/Cmd+8"),
            ("Apply a fill colour to confirm the knock-out, then choose Object > Paths > Release Compound Path to see the two separate shapes again, and re-make the compound path.", "Object > Paths > Release Compound Path"),
            ("Draw a rectangle overlapping a circle, select both and open Window > Object & Layout > Pathfinder; click Add, then undo and click Subtract, Intersect, Exclude Overlap and Minus Back in turn to compare each result.", "Window > Object & Layout > Pathfinder"),
            ("Keep the shape produced by Subtract as the decorative element and position it on the spread.", ""),
            ("Select the orchid image frame and open Window > Text Wrap.", "Window > Text Wrap"),
            ("Click Wrap Around Bounding Box and observe the rectangular wrap; then click Wrap Around Object Shape.", "Text Wrap > Wrap Around Object Shape"),
            ("In the Text Wrap panel set Contour Options Type to Detect Edges so InDesign traces the orchid silhouette instead of the frame, and set Include Inside Edges if gaps in the flower should also receive text.", "Text Wrap > Contour Options > Detect Edges"),
            ("Set the Top Offset to 3 mm and click the chain icon so all four offsets match, keeping the type clear of the petals.", "Text Wrap offset 3 mm"),
            ("Fine-tune the generated wrap boundary with the Direct Selection tool (A), dragging individual anchor points where the type crowds the image.", "A = Direct Selection tool"),
            ("Select any text frame that is ignoring the wrap, confirm 'Ignore Text Wrap' is unticked in Object > Text Frame Options, then press W to preview the spread and save.", "Object > Text Frame Options > Ignore Text Wrap  ·  W = Preview"),
        ],
        test="The logo overlap shows the page through it, the Pathfinder shape is a single path in the Layers panel, and body copy follows the orchid outline with an even 3 mm gap on all sides.",
        troubleshoot="If the overlap prints solid instead of knocking through, you grouped the circles rather than making a compound path — ungroup and use Object > Paths > Make Compound Path. If Detect Edges traces a rectangle, the image has no transparency or clipping path: use Object > Clipping Path > Options > Detect Edges on the image first, or ask for a PSD with a proper alpha channel.",
    ),
    dict(
        num=10, topic=2,
        title="Build a Colour System with Swatches, Spot Colours and Gradients",
        lo="LO2",
        objective="Identify and select appropriate colour mediums for the print process, and build a reusable, correctly specified swatch system including spot and process colours and gradients (TSC A1, A3).",
        scenario=(
            "**Harmony Petals** has just registered its brand pink as **Pantone 212 C** because it must "
            "match exactly across shop signage, packaging ribbon and *Petals Quarterly*. "
            "**Sun Ray Printers** has quoted the magazine as 4-colour process plus one spot, and warned "
            "that the last file they received contained 31 unnamed colours, three RGB swatches and two "
            "duplicate pinks — which would have produced an unusable set of separations. "
            "Priya wants a locked-down swatch palette in the file before any more pages are designed, and "
            "she wants a soft pink-to-white gradient for the section dividers."
        ),
        desc=(
            "Build a disciplined colour system: create and name process swatches, add a Pantone spot colour "
            "from a colour book, extract a harmonious palette from a photograph with the Colour Theme tool, "
            "create linear and radial gradients, and audit the document so no unnamed or RGB colours survive."
        ),
        build="HP_Magazine_3.indd carrying a named swatch palette with Pantone 212 C as a spot colour, a Colour Theme palette extracted from the cover photograph, a pink-to-white linear gradient swatch, and zero RGB or unnamed colours.",
        services="Adobe InDesign · Swatches panel · New Colour Swatch · Colour Books (Pantone+ Solid Coated) · Colour Theme tool · Gradient panel & Gradient Swatch tool · Window > Output > Separations Preview",
        questions=[
            "Explain the difference between a process colour and a spot colour in terms of what happens on the printing press and what it costs.",
            "Why is a named swatch preferable to a colour mixed in the Colour panel, especially when a client changes the brand pink three weeks into a job?",
            "The client supplied their brand pink as an RGB value. What must you do before that colour is used in a litho job, and what will change visually?",
            "A tint swatch and a lighter mixed colour can look identical on screen. What is the production advantage of the tint?",
            "How does Separations Preview let you prove to Sun Ray Printers that the file will output on exactly five plates?",
        ],
        steps=[
            ("Open HP_Magazine_3.indd and open Window > Colour > Swatches.", "Window > Colour > Swatches"),
            ("From the Swatches panel menu choose New Colour Swatch, set Colour Type to Process, Colour Mode to CMYK, mix the brand secondary green, name it 'HP Leaf Green' and click OK.", "Swatches panel menu > New Colour Swatch"),
            ("Create another new swatch, set Colour Type to Spot and Colour Mode to Pantone+ Solid Coated, type 212 to jump to Pantone 212 C, and add it.", "New Colour Swatch > Spot > Pantone+ Solid Coated > 212 C"),
            ("Select the Pantone swatch, choose New Tint Swatch from the panel menu and create a 30% tint for background panels.", "Swatches panel menu > New Tint Swatch"),
            ("Select the Colour Theme tool (nested with the Eyedropper, Shift+I) and click the cover photograph to extract a five-colour harmony; open the theme flyout and add the theme to Swatches.", "Shift+I = Colour Theme tool"),
            ("Draw a rectangle for a section divider, then open Window > Colour > Gradient and set Type to Linear.", "Window > Colour > Gradient"),
            ("Drag the Pantone 212 C swatch onto the left gradient stop and Paper onto the right stop to build a pink-to-white blend, then set the Angle to 90 degrees.", "Gradient panel  ·  Angle 90"),
            ("Save the blend permanently by choosing New Gradient Swatch from the Swatches panel menu so it can be reused across the magazine.", "Swatches panel menu > New Gradient Swatch"),
            ("Select the Gradient Swatch tool (G) and drag across the rectangle to reset the gradient's start point, end point and direction.", "G = Gradient Swatch tool"),
            ("From the Swatches panel menu choose Select All Unused, then Delete Swatch, to strip the palette of colours nobody applied.", "Swatches panel menu > Select All Unused"),
            ("Open Window > Output > Separations Preview, set View to Separations, confirm exactly Cyan, Magenta, Yellow, Black and PANTONE 212 C are listed, then save and record the palette on your specification sheet.", "Window > Output > Separations Preview  ·  File > Save"),
        ],
        test="Separations Preview lists exactly five plates — CMYK plus PANTONE 212 C — the Swatches panel contains only named swatches with no RGB icons, and the divider rectangle carries a saved gradient swatch.",
        troubleshoot="If Separations Preview shows six or seven plates, duplicate or misnamed spot colours exist: use the Swatches panel menu > Merge Swatches, or double-click a stray spot swatch and change Colour Type to Process. RGB swatches show a distinctive icon in the Swatches panel — double-click each one and switch Colour Mode to CMYK, accepting that saturated blues and greens will visibly dull.",
    ),
    dict(
        num=11, topic=2,
        title="Apply Transparency, Blending Modes and Effects for Print",
        lo="LO2",
        objective="Refine layout elements using transparency, blending modes and the Effects panel while selecting settings appropriate to the chosen print medium (TSC A3, A4).",
        scenario=(
            "The *Petals Quarterly* cover needs the masthead to sit over a full-bleed bouquet photograph "
            "with a soft dark gradient behind the type so the words stay readable. "
            "A previous attempt used a drop shadow set to Multiply at 100% opacity, and **Sun Ray Printers** "
            "returned the file with a transparency-flattening warning: the shadow had created a visible "
            "grey box on the proof where it crossed a spot-colour panel. "
            "Priya needs the cover finished by Wednesday and wants you to demonstrate that the effects will "
            "flatten predictably, because a second S$480 reprint is not in the budget."
        ),
        desc=(
            "Work through the Effects panel systematically — object, stroke, fill and text level opacity, "
            "blending modes, drop shadow, inner shadow, feather, gradient feather and bevel — then check the "
            "result with the Flattener Preview and the Separations Preview so the transparency behaves at "
            "output."
        ),
        build="HP_Magazine_3.indd cover with a gradient-feathered dark panel behind the masthead, a controlled drop shadow on the cover line, and a Flattener Preview showing no unexpected transparency interactions over the spot colour.",
        services="Adobe InDesign · Window > Effects · Blending modes · Object > Effects > Drop Shadow / Gradient Feather · Window > Output > Flattener Preview · Transparency Blend Space",
        questions=[
            "The Effects panel lists Object, Stroke, Fill and Text as separate targets. Why does InDesign separate them, and give a design case for applying an effect to Fill only.",
            "Explain what the Multiply blending mode actually does to the colours beneath it, and why it behaves differently over white than over a dark photograph.",
            "Why can transparency over a spot colour cause problems on press, and what does the Flattener Preview show you about it?",
            "A drop shadow looks correct on screen but prints as a hard grey rectangle. Identify the two most likely causes.",
            "Compare Feather, Directional Feather and Gradient Feather. Which would you choose to fade a photograph into a white margin, and why?",
        ],
        steps=[
            ("Open HP_Magazine_3.indd, go to the cover page and open Window > Effects.", "Window > Effects"),
            ("Select the bouquet photograph frame and reduce Object opacity to 80% in the Effects panel; observe how the whole frame including its stroke changes.", "Effects panel > Object > Opacity 80%"),
            ("Undo, then target Fill only in the Effects panel list and reduce its opacity, proving that the stroke stays fully opaque.", "Effects panel > Fill > Opacity"),
            ("Draw a dark rectangle across the lower third of the cover, set its blending mode to Multiply and study how it darkens the photograph without hiding it.", "Effects panel > Blending Mode > Multiply"),
            ("With the rectangle still selected, choose Object > Effects > Gradient Feather and drag the gradient so the panel fades from solid at the bottom to transparent at the top.", "Object > Effects > Gradient Feather"),
            ("Select the cover-line text frame and apply Object > Effects > Drop Shadow; set Mode Multiply, Opacity 60%, X and Y offset 1 mm, Size 2 mm and Blur appropriate to the type size.", "Object > Effects > Drop Shadow  ·  Multiply, 60%"),
            ("In the same Effects dialog, tick Preview and try Inner Shadow, Outer Glow and Bevel and Emboss on a duplicate object to compare their character.", "Object > Effects"),
            ("Use the fx icon at the foot of the Effects panel to copy an effect from one object to another by dragging it in the panel.", "Effects panel > drag fx icon"),
            ("Choose Edit > Transparency Blend Space > Document CMYK so transparency is calculated in the print colour space, not RGB.", "Edit > Transparency Blend Space > Document CMYK"),
            ("Open Window > Output > Flattener Preview, set Highlight to All Affected Objects, inspect where the shadow interacts with the spot-colour panel, adjust the shadow opacity until nothing unwanted is highlighted, and save.", "Window > Output > Flattener Preview  ·  File > Save"),
        ],
        test="The masthead is legible over a smoothly faded dark panel, Flattener Preview highlights no transparency crossing the spot-colour element unexpectedly, and Transparency Blend Space is set to Document CMYK.",
        troubleshoot="A grey box behind a shadow almost always means the shadow's blending mode was left at Normal, or the object sits over a spot colour in an RGB blend space — set Mode to Multiply and switch Edit > Transparency Blend Space to Document CMYK. If effects vanish on screen, View > Display Performance is set to Fast Display; switch to High Quality Display to judge the result.",
    ),
    dict(
        num=12, topic=2,
        title="Transform, Align and Organise Objects with Layers",
        lo="LO2",
        objective="Manage objects by transforming them precisely, aligning and distributing them to the document structure, and organising the file with layers so it can be handed over and maintained (TSC A2, A4).",
        scenario=(
            "**Harmony Petals** is producing an interactive PDF version of its outlet directory that must "
            "also print. Three language versions — English, Mandarin and Malay — will share the same layout, "
            "and Priya wants each language on its own layer so one file serves all three markets. "
            "The current file is a mess: 40 loose objects, a background photograph that keeps getting "
            "selected by accident, and six outlet icons that a reviewer said look \"randomly scattered\". "
            "The directory must be delivered to **Sun Ray Printers** for the print run and to the web agency "
            "as a PDF by Friday, so the file has to be genuinely maintainable, not just presentable."
        ),
        desc=(
            "Apply precise numeric and interactive transformations, stack and group objects, align and "
            "distribute a set of icons using the Align panel with Use Spacing, then restructure the whole "
            "document onto named layers with locking, visibility control and layer-based stacking order."
        ),
        build="HP_InteractiveDoc.indd restructured onto named layers (Background, Images, Text-EN, Text-ZH, Text-MS), with six outlet icons aligned and distributed at exact 8 mm spacing and the background layer locked.",
        services="Adobe InDesign · Window > Layers · Window > Object & Layout > Align · Transform panel & Control panel · Object > Transform · Object > Arrange · Group / Lock",
        questions=[
            "Explain the difference between the object stacking order within a layer and the stacking order of the layers themselves.",
            "Why is locking an object different from hiding it, and when would you use each?",
            "The Align panel offers Align to Selection, Align to Key Object, Align to Margins, Align to Page and Align to Spread. Give a production situation for Align to Key Object.",
            "Distribute Horizontal Centers and Distribute Spacing with Use Spacing can give different results for objects of unequal width. Explain why, and which one Priya's icon row needs.",
            "How does putting each language on its own layer save time compared with keeping three separate InDesign files?",
        ],
        steps=[
            ("Open HP_InteractiveDoc.indd and open Window > Layers.", "Open HP_InteractiveDoc.indd  ·  Window > Layers"),
            ("Create five layers using New Layer from the Layers panel menu, named Background, Images, Text-EN, Text-ZH and Text-MS, and drag them into the correct stacking order.", "Layers panel menu > New Layer"),
            ("Select the background photograph and drag the small coloured square beside the selected layer in the Layers panel to move the object onto the Background layer.", "Drag the coloured proxy square"),
            ("Move the remaining images and text frames onto their appropriate layers the same way, then lock the Background layer by clicking its lock column so it stops being selected by accident.", "Layers panel > lock column"),
            ("Toggle the eye icon on Text-ZH and Text-MS to hide them, confirming only the English version is visible.", "Layers panel > visibility eye"),
            ("Select an outlet icon and use the Control panel to set exact X, Y, W and H values; click the chain icon first to constrain proportions.", "Control panel  ·  X / Y / W / H"),
            ("Open Window > Object & Layout > Transform and rotate the icon 15 degrees, then use Object > Transform > Rotate for a numeric dialog with a Copy option.", "Object > Transform > Rotate"),
            ("Apply Object > Transform Again > Transform Again (Ctrl/Cmd+Alt/Opt+3) to repeat the last transformation on another object.", "Object > Transform Again  ·  Ctrl/Cmd+Alt/Opt+3"),
            ("Select all six icons, open Window > Object & Layout > Align, set Align To to Align to Selection, and click Align Vertical Centers.", "Align panel > Align Vertical Centers"),
            ("In the Distribute Spacing section tick Use Spacing, enter 8 mm and click Distribute Horizontal Spacing so the gaps are identical regardless of icon width.", "Align panel > Distribute Spacing > Use Spacing 8 mm"),
            ("Click one icon a second time to make it the Key Object (its border thickens), switch Align To to Align to Key Object, align the others to it, then group them with Object > Group and save.", "Align to Key Object  ·  Object > Group  ·  File > Save"),
        ],
        test="The Layers panel shows five correctly named layers with the Background locked, hiding Text-ZH and Text-MS leaves a complete English layout, and the six icons sit on one baseline with exactly 8 mm between them.",
        troubleshoot="If an object refuses to move to another layer, its current layer is locked — unlock it in the Layers panel first. If Bring to Front appears to do nothing, the object is on a lower layer: layer order always beats object order, so move the object to a higher layer rather than re-arranging within its own.",
    ),
]
