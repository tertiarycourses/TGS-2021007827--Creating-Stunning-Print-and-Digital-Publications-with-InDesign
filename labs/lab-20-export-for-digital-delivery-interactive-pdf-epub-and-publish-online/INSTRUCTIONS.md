# Lab 20 - Export for Digital Delivery — Interactive PDF, EPUB and Publish Online

**Topic 03: Refine InDesign Drawings**  ·  **LO3**  ·  TGS-2021007827

## The Situation

The animated *Little Red Hen* is finished and **Harmony Petals** now has three audiences for the same file. The community library kiosk needs the animation intact. The National Library Board wants a copy for its e-lending catalogue that must reflow on a 6-inch e-reader with adjustable type size. Priya wants a link she can WhatsApp to the board of directors this afternoon without sending a 40 MB attachment, and she wants their comments back in one place. Exporting the wrong format to the wrong audience last year produced an EPUB with the illustrations stacked randomly and an embarrassing complaint from the library.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO3 |
| **Objective** | Identify and select the appropriate digital medium for a publication and export to it correctly, choosing between interactive PDF, reflowable EPUB, fixed-layout EPUB and Publish Online (TSC A1, A3, A4). |
| **You will produce** | Four exports from Little_Red_Hen-anim-after.indd — an interactive PDF, a reflowable EPUB, a fixed-layout EPUB and a Publish Online URL — plus a Share for Review link with at least one comment received. |
| **Tools and panels** | Adobe InDesign · File > Export > Adobe PDF (Interactive) · EPUB (Reflowable) & EPUB (Fixed Layout) · Articles panel · Object Export Options · Publish Online · Share for Review |
| **Starter InDesign file** | `Little_Red_Hen-anim-after.indd` |
| **Final filename** | `Lab-20-Completed.indd` |

## What You Will Do

Match each audience to the correct export path and produce all of them from one source file: an interactive PDF for the kiosk, a reflowable EPUB with a correct Articles-panel reading order and object export metadata for the e-reader, a fixed-layout EPUB to preserve the animation, a Publish Online link for the board, and a Share for Review link to collect comments.

## Phase 1 - Prepare and Baseline

1. Read this guide completely, then duplicate `Little_Red_Hen-anim-after.indd` as `Lab-20-Working.indd`.
2. Create an `Evidence/` folder beside the working file.
3. Open the working copy and capture the starting Pages, Links or Preflight panel most relevant to the task.
4. Keep every linked asset inside this lab folder; never relink to Downloads, Desktop or a network path.

> **Starter role:** Completed interactive publication used to compare output formats, reading order, accessibility and review workflows.

## Phase 2 - Build


## Step-by-Step Procedure

1. Open Little_Red_Hen-anim-after.indd and list the three audiences and the format each one needs before exporting anything.
   > `Open Little_Red_Hen-anim-after.indd`
2. Choose File > Export, set Format to Adobe PDF (Interactive), and in the dialog tick Include All in Hyperlinks, set Page Transitions to From Document, and enable Interactive Elements: Include All.
   > `File > Export > Adobe PDF (Interactive)`
3. Open the exported PDF in Acrobat and confirm the buttons and page transitions still function.
4. Open Window > Articles and drag the story frames into the panel in true reading order, ticking Include When Exporting.
   > `Window > Articles`
5. Select each illustration and choose Object > Object Export Options; on the Alt Text tab set the source to Custom and write a meaningful description.
   > `Object > Object Export Options > Alt Text`
6. On the EPUB and HTML tab of the same dialog set Custom Rasterization to 150 ppi PNG so the images travel well on an e-reader.
   > `Object Export Options > EPUB and HTML`
7. Choose File > Export > EPUB (Reflowable). In General set Order to Same as Articles Panel, and in Text set Bullets and Numbers to Map to Unordered Lists.
   > `File > Export > EPUB (Reflowable)`
8. Open the reflowable EPUB in an EPUB reader, change the reader's text size, and confirm the text reflows and the alt text is present.
9. Export again with File > Export > EPUB (Fixed Layout), ticking Include Interactive Elements, and confirm the animation survives.
   > `File > Export > EPUB (Fixed Layout)`
10. Choose File > Publish Online, give the document a title and description, choose the pages to include, publish, and copy the generated URL.
   > `File > Publish Online`
11. Choose File > Share for Review, create the review link, send it to a classmate acting as Priya, then open Window > Comments to read their returned comment and mark it resolved.
   > `File > Share for Review  ·  Window > Comments`

## Verify Your Work

> ✅ **Done when:** The interactive PDF plays its transitions, the reflowable EPUB reflows and reads in the Articles-panel order with alt text intact, the fixed-layout EPUB retains the animation, and the Publish Online and Share for Review links both open with a comment visible in the Comments panel.

## Evidence and Submission

- [ ] Interactive PDF and EPUB exports
- [ ] Articles/alt-text screenshots
- [ ] Publish Online or Share for Review evidence
- [ ] Final native file saved as `Lab-20-Completed.indd`
- [ ] All linked assets remain inside this lab folder or its subfolders
- [ ] No overset text, missing fonts or missing links remain unless the task explicitly asks you to diagnose them

## Recovery Path

1. If the working file is damaged, close it without saving and duplicate `Little_Red_Hen-anim-after.indd` again.
2. If links are missing, use the Links panel Relink command and select the matching file inside this lab folder.
3. If fonts are missing, activate Adobe Fonts or substitute an approved font, then check for reflow and overset text.
4. Re-run the verification gate and recapture evidence after recovery.

## If It Doesn't Work

EPUB content appearing in a jumbled order is the classic symptom of an unset reading order — populate the Articles panel and set Order to Same as Articles Panel on export. If your animation is missing, you exported the reflowable EPUB, which discards interactivity: use fixed layout, an Interactive PDF or Publish Online instead. Publish Online greyed out means it is disabled in Preferences or by your organisation's Creative Cloud administrator.

## Stretch Challenge

Create a format decision record for print PDF, interactive PDF, reflowable EPUB, fixed-layout EPUB and Publish Online, including one limitation of each.

## Discussion Questions

1. State the single most important difference between a reflowable and a fixed-layout EPUB, and give one publication type that suits each.
2. The Articles panel controls EPUB reading order. What determines the order if you never open that panel, and why is that risky on a designed spread?
3. Alt text is set in Object Export Options. Beyond accessibility compliance, what practical benefit does it deliver?
4. Publish Online places the document on Adobe's servers with a public URL. What are the confidentiality implications for a client's unreleased pricing, and how would you manage them?
5. A client wants comments on a draft. Compare Share for Review with emailing a PDF, in terms of version control and consolidating feedback.

## Reference Artwork

![Lab 20](Reference.png)

## Reference Basis

ACP guide domain 5: publish to print, web and digital devices; export settings, accessibility and quality checks.

Current Adobe Help: https://helpx.adobe.com/indesign/desktop/save-export-and-publish/save-and-export/export-pdfs-for-printing.html

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
