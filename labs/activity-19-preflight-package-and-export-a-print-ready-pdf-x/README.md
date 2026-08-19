# Activity 19 — Preflight, Package and Export a Print-Ready PDF/X

**Topic 03: Refine InDesign Drawings**  ·  **LO3**  ·  TGS-2021007827

## The Situation

**Sun Ray Printers** has rejected the Harmony Petals magazine file two hours before the press booking. Their prepress report lists four faults: one image is linked to a designer's desktop and is missing, a second image has an effective resolution of 96 ppi, there is overset text in a caption frame, and two fonts are not embedded. The press slot costs S$1,150 and rolls over to next Tuesday if missed. Priya needs a clean preflight, a proper package for the printer, and a PDF/X-1a file supplied within the hour.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO3 |
| **Objective** | Refine and validate a document against print production requirements, then package the job and export a press-ready PDF/X file with correct bleed and marks (TSC A1, A3, A4). |
| **You will produce** | A Harmony Petals package folder containing the .indd, Links, Document Fonts and an instructions file, plus HP_Magazine_7_PRINT.pdf exported as PDF/X-1a:2001 with 3 mm bleed and crop marks. |
| **Tools and panels** | Adobe InDesign · Preflight panel & profiles · Links panel · File > Package · File > Export > Adobe PDF (Print) · PDF/X-1a:2001 |

## What You Will Do

Use InDesign's live Preflight to define and run a production profile, resolve every error in the Links panel, clear overset text, then package the job with fonts and links and export a PDF/X-1a file carrying 3 mm bleed and crop marks — the exact deliverable a commercial litho printer expects.

## Step-by-Step Procedure

1. Open HP_Magazine_7.indd and open Window > Output > Preflight; note the red error count in the status bar.
   > `Window > Output > Preflight`
2. From the Preflight panel menu choose Define Profiles, create a profile named 'Sun Ray Litho', and enable Missing Links, Image Resolution minimum 300 ppi, Overset Text and Non-Proportional Scaling.
   > `Preflight panel menu > Define Profiles`
3. Set the Profile dropdown to 'Sun Ray Litho' and expand the error list to see each offending page.
4. Open Window > Links, select the missing link, click Relink and navigate to the correct file in the Links folder.
   > `Window > Links > Relink`
5. Select the low-resolution image in the Links panel and read Effective PPI in the Link Info section; replace it with the 300 ppi version supplied by the photographer.
   > `Links panel > Link Info > Effective PPI`
6. Double-click the Overset Text error in Preflight to jump to the caption frame, then fix it by enlarging the frame or editing the copy — not by deleting the frame.
   > `Preflight > double-click error to navigate`
7. Use Type > Find Font to confirm every font is available and, if necessary, replace the two unembedded fonts with licensed equivalents.
   > `Type > Find Font`
8. Re-run preflight and confirm the status bar reads 'No errors' before going any further.
9. Choose File > Package, review the Summary, then click Package and tick Copy Fonts, Copy Linked Graphics, Update Graphic Links in Package and Include Fonts and Links From Hidden Content.
   > `File > Package`
10. Choose File > Export, set Format to Adobe PDF (Print), name the file HP_Magazine_7_PRINT.pdf and click Save.
   > `File > Export > Adobe PDF (Print)`
11. In the Export dialog select the [PDF/X-1a:2001] preset, tick Crop Marks and Use Document Bleed Settings in Marks and Bleeds, then open the PDF and check the artwork extends 3 mm past the crop marks.
   > `Marks and Bleeds > Crop Marks · Use Document Bleed Settings`

## Verify Your Work

> ✅ **Done when:** The Preflight panel reports 'No errors' against the Sun Ray Litho profile, the package folder contains the document, Links and Document Fonts, and the exported PDF/X-1a shows crop marks with artwork bleeding 3 mm beyond the trim.

## If It Doesn't Work

Preflight still reports errors after relinking? The panel caches until you re-run it — toggle the profile or click the panel refresh. If the exported PDF has crop marks but no bleed, you ticked Crop Marks without ticking Use Document Bleed Settings, so the marks sit on a document that was set to 0 mm bleed; fix the bleed in File > Document Setup and export again.

## Discussion Questions

1. The default [Basic] preflight profile passes a file that the printer rejects. Why, and what should you do about it?
2. Explain effective resolution versus actual resolution, and why scaling a 300 ppi image to 200% is a production error.
3. File > Package creates a Document Fonts folder. What licensing condition governs your use of those fonts, and who may open them?
4. What is the difference between PDF/X-1a and PDF/X-4, and which would you supply for a job with live transparency?
5. You set 3 mm bleed in Document Setup but the exported PDF has none. Which specific export setting was missed?

## Reference Artwork

![Activity 19](../../courseware/assets/screens/preflight_gate.png)

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
