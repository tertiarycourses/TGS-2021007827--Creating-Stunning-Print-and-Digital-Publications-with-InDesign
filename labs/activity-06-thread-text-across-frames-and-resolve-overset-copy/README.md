# Activity 6 — Thread Text Across Frames and Resolve Overset Copy

**Topic 02: Basic InDesign Drawing Techniques**  ·  **LO2**  ·  TGS-2021007827

## The Situation

The Bellow Flower feature article, **HP_Brochure_BellowFlower.docx**, runs to about 900 words and must flow across four panels of the **Harmony Petals** brochure. Yesterday the file went to **Sun Ray Printers** with a red overset marker nobody noticed; the proof came back with the last paragraph of the founder's story simply missing, and the client refused to approve it. Priya has asked you to re-do the flow properly and to demonstrate, in front of her, that no copy is hidden. She also wants the article to autoflow so that if the copywriter adds two more paragraphs on Friday, the brochure extends itself rather than silently truncating.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO2 |
| **Objective** | Refine a text layout by threading a story across multiple frames and pages, and diagnose and resolve overset text so no client copy is lost at output (TSC A2, A4). |
| **You will produce** | HP_Brochure_2.indd with the Bellow Flower story threaded across four frames, zero overset text, visible thread indicators, and a Preflight panel reporting no errors. |
| **Tools and panels** | Adobe InDesign · In/out ports · Autoflow (Shift-click) · Semi-autoflow (Alt/Opt-click) · View > Extras > Show Text Threads · Edit > Edit in Story Editor · Preflight panel |

## What You Will Do

Import a long story and thread it manually between frames using the in and out ports, then repeat the flow using semi-autoflow and autoflow with modifier keys. You learn to spot the red plus sign of overset text, use Story Editor and Preflight to prove nothing is lost, and unthread a frame without deleting its content.

## Step-by-Step Procedure

1. Open HP_Brochure_2.indd and turn on View > Extras > Show Text Threads so the links between frames are visible when frames are selected.
   > `View > Extras > Show Text Threads`
2. With nothing selected, choose File > Place and select HP_Brochure_BellowFlower.docx; the cursor becomes a loaded text icon.
   > `File > Place  ·  HP_Brochure_BellowFlower.docx`
3. Click once inside the first panel guide area to place the story into a single frame; note the red plus sign in the out port at the lower right.
4. Switch to the Selection tool (V), click the red out port once — the cursor reloads — then click or drag in the second panel to thread the continuation.
   > `V, then click the out port`
5. Repeat for the third panel to confirm you can control the flow frame by frame.
6. Undo back to the loaded cursor, then hold Alt (Windows) or Option (macOS) and click to use semi-autoflow, which keeps the cursor loaded after each placement.
   > `Alt/Opt-click = semi-autoflow`
7. Undo again and hold Shift while clicking to autoflow the whole story, letting InDesign add frames and pages until the copy is exhausted.
   > `Shift-click = autoflow`
8. Select a middle frame and choose Edit > Edit in Story Editor; scroll to the end and confirm no text sits below the overset depth line.
   > `Edit > Edit in Story Editor  ·  Ctrl/Cmd+Y`
9. Open Window > Output > Preflight, enable it, and confirm the [Basic] profile reports 0 errors with no overset text entry.
   > `Window > Output > Preflight`
10. Select the final frame and click its in port, then click the out port of the preceding frame to break the thread; observe that the text re-flows back rather than being deleted.
   > `Click in port to unthread`
11. Re-thread the final frame, then use Layout > Pages and the Pages panel to verify no unintended pages were added by autoflow. Save the file.
   > `File > Save`

## Verify Your Work

> ✅ **Done when:** Preflight reports 0 errors, Story Editor shows no copy below the overset line, and selecting any frame displays continuous thread arrows through all four panels.

## If It Doesn't Work

If clicking the out port creates a brand-new empty frame instead of continuing the story, you clicked with the Type tool rather than the Selection tool — press V first. If autoflow silently added six unwanted pages, you Shift-clicked with Smart Text Reflow enabled; undo, reduce the type size or enlarge the frames, then re-flow.

## Discussion Questions

1. A red plus sign appears in the out port of a text frame. Explain precisely what it means and name three different ways to resolve it.
2. Compare manual flow, semi-autoflow and autoflow. Which modifier key triggers each, and in what production situation would you deliberately choose the slowest of the three?
3. You delete a threaded frame in the middle of a story. What happens to the text it contained, and why?
4. Why is Story Editor a more reliable way to find overset copy than scrolling the layout looking for red markers?
5. Priya's overset paragraph was invisible on screen but caused a rejected proof. What preflight or handover check should be standard before any file leaves the studio?

## Reference Artwork

![Activity 6](../../courseware/assets/screens/act_threading.png)

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
