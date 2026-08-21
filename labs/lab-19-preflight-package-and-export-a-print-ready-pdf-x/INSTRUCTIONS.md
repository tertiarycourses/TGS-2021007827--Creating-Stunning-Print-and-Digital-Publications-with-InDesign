# Lab 19 - Preflight, Package and Export a Print-Ready PDF/X

**Topic 03: Refine InDesign Drawings**  ·  **LO3**  ·  TGS-2021007827

## The Situation

**Sun Ray Printers** has rejected a travel-magazine production file two hours before the press booking. Their prepress report lists four faults: one image is linked to a designer's desktop and is missing, a second image has an effective resolution of 96 ppi, there is overset text in a caption frame, and two fonts are not embedded. The press slot costs S$1,150 and rolls over to next Tuesday if missed. The editor needs a clean preflight, a proper package for the printer, and a PDF/X-1a file supplied within the hour.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO3 |
| **Objective** | Refine and validate a document against print production requirements, then package the job and export a press-ready PDF/X file with correct bleed and marks (TSC A1, A3, A4). |
| **You will produce** | A repaired travel-magazine package containing the .indd, IDML, Links, available Document Fonts and instructions, plus travel_magazine_PRINT.pdf exported as PDF/X-1a:2001 with 3 mm bleed and crop marks. |
| **Tools and panels** | Adobe InDesign · Preflight panel & profiles · Links panel · File > Package · File > Export > Adobe PDF (Print) · PDF/X-1a:2001 |
| **Starter InDesign file** | `travel_magazine_tutorial.indd` |
| **Final filename** | `Lab-19-Completed.indd` |

## What You Will Do

Use InDesign's live Preflight to define and run a production profile, resolve every error in the Links panel, clear overset text, then package the job with fonts and links and export a PDF/X-1a file carrying 3 mm bleed and crop marks — the exact deliverable a commercial litho printer expects.

## Phase 1 - Prepare and Baseline

1. Read this guide completely, then duplicate `travel_magazine_tutorial.indd` as `Lab-19-Working.indd`.
2. Create an `Evidence/` folder beside the working file.
3. Open the working copy and capture the starting Pages, Links or Preflight panel most relevant to the task.
4. Keep every linked asset inside this lab folder; never relink to Downloads, Desktop or a network path.

> **Starter role:** Production file for a realistic preflight, relink, package and PDF/X handoff. Missing large raster links are intentional faults for diagnosis.

## Phase 2 - Build


## Step-by-Step Procedure

1. Open travel_magazine_tutorial.indd and compare it with Reference-Output.pdf before opening Window > Output > Preflight; note the red error count in the status bar.
   > `Open travel_magazine_tutorial.indd  ·  Window > Output > Preflight`
2. From the Preflight panel menu choose Define Profiles, create a profile named 'Sun Ray Litho', and enable Missing Links, Image Resolution minimum 300 ppi, Overset Text and Non-Proportional Scaling.
   > `Preflight panel menu > Define Profiles`
3. Set the Profile dropdown to 'Sun Ray Litho' and expand the error list to see each offending page.
4. Open Window > Links, select a missing link, click Relink and choose a suitable file in Replacement Assets. Missing large raster links are deliberate faults in this exercise.
   > `Window > Links > Relink  ·  Replacement Assets/`
5. Select each replacement image in the Links panel and read Effective PPI in the Link Info section; scale or replace it until it meets the profile threshold without distortion.
   > `Links panel > Link Info > Effective PPI`
6. Double-click the Overset Text error in Preflight to jump to the caption frame, then fix it by enlarging the frame or editing the copy — not by deleting the frame.
   > `Preflight > double-click error to navigate`
7. Use Type > Find Font to confirm every font is available and, if necessary, replace the two unembedded fonts with licensed equivalents.
   > `Type > Find Font`
8. Re-run preflight and confirm the status bar reads 'No errors' before going any further.
9. Choose File > Package, review the Summary, then click Package and tick Copy Fonts, Copy Linked Graphics, Update Graphic Links in Package and Include Fonts and Links From Hidden Content.
   > `File > Package`
10. Choose File > Export, set Format to Adobe PDF (Print), name the file travel_magazine_PRINT.pdf and click Save.
   > `File > Export > Adobe PDF (Print)`
11. In the Export dialog select the [PDF/X-1a:2001] preset, tick Crop Marks and Use Document Bleed Settings in Marks and Bleeds, then open the PDF and check the artwork extends 3 mm past the crop marks.
   > `Marks and Bleeds > Crop Marks · Use Document Bleed Settings`

## Verify Your Work

> ✅ **Done when:** The Preflight panel reports 'No errors' against the Sun Ray Litho profile, the travel-magazine package contains the document, IDML, collected links and available fonts, and the exported PDF/X-1a shows crop marks with artwork bleeding 3 mm beyond the trim.

## Evidence and Submission

- [ ] Repaired travel_magazine_tutorial.indd
- [ ] Zero-error Preflight screenshot
- [ ] Packaged folder and PDF/X proof
- [ ] Final native file saved as `Lab-19-Completed.indd`
- [ ] All linked assets remain inside this lab folder or its subfolders
- [ ] No overset text, missing fonts or missing links remain unless the task explicitly asks you to diagnose them

## Recovery Path

1. If the working file is damaged, close it without saving and duplicate `travel_magazine_tutorial.indd` again.
2. If links are missing, use the Links panel Relink command and select the matching file inside this lab folder.
3. If fonts are missing, activate Adobe Fonts or substitute an approved font, then check for reflow and overset text.
4. Re-run the verification gate and recapture evidence after recovery.

## If It Doesn't Work

Preflight still reports errors after relinking? The panel caches until you re-run it — toggle the profile or click the panel refresh. If the exported PDF has crop marks but no bleed, you ticked Crop Marks without ticking Use Document Bleed Settings, so the marks sit on a document that was set to 0 mm bleed; fix the bleed in File > Document Setup and export again.

## Stretch Challenge

Create a stricter printer profile that flags RGB, spot colours and effective PPI below 300, then compare it with Basic Preflight.

## Discussion Questions

1. The default [Basic] preflight profile passes a file that the printer rejects. Why, and what should you do about it?
2. Explain effective resolution versus actual resolution, and why scaling a 300 ppi image to 200% is a production error.
3. File > Package creates a Document Fonts folder. What licensing condition governs your use of those fonts, and who may open them?
4. What is the difference between PDF/X-1a and PDF/X-4, and which would you supply for a job with live transparency?
5. You set 3 mm bleed in Document Setup but the exported PDF has none. Which specific export setting was missed?

## Reference Artwork

![Lab 19](Reference.png)

## Reference Basis

ACP guide domain 5: preflight, fault resolution, package, IDML/PDF inclusion and print-ready export.

Current Adobe Help: https://helpx.adobe.com/indesign/desktop/print/preflight/package-files-for-output.html

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
