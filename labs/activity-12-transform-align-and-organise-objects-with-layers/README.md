# Activity 12 — Transform, Align and Organise Objects with Layers

**Topic 02: Basic InDesign Drawing Techniques**  ·  **LO2**  ·  TGS-2021007827

## The Situation

**Harmony Petals** is producing an interactive PDF version of its outlet directory that must also print. Three language versions — English, Mandarin and Malay — will share the same layout, and Priya wants each language on its own layer so one file serves all three markets. The current file is a mess: 40 loose objects, a background photograph that keeps getting selected by accident, and six outlet icons that a reviewer said look "randomly scattered". The directory must be delivered to **Sun Ray Printers** for the print run and to the web agency as a PDF by Friday, so the file has to be genuinely maintainable, not just presentable.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO2 |
| **Objective** | Manage objects by transforming them precisely, aligning and distributing them to the document structure, and organising the file with layers so it can be handed over and maintained (TSC A2, A4). |
| **You will produce** | HP_InteractiveDoc.indd restructured onto named layers (Background, Images, Text-EN, Text-ZH, Text-MS), with six outlet icons aligned and distributed at exact 8 mm spacing and the background layer locked. |
| **Tools and panels** | Adobe InDesign · Window > Layers · Window > Object & Layout > Align · Transform panel & Control panel · Object > Transform · Object > Arrange · Group / Lock |

## What You Will Do

Apply precise numeric and interactive transformations, stack and group objects, align and distribute a set of icons using the Align panel with Use Spacing, then restructure the whole document onto named layers with locking, visibility control and layer-based stacking order.

## Step-by-Step Procedure

1. Open HP_InteractiveDoc.indd and open Window > Layers.
   > `Open HP_InteractiveDoc.indd  ·  Window > Layers`
2. Create five layers using New Layer from the Layers panel menu, named Background, Images, Text-EN, Text-ZH and Text-MS, and drag them into the correct stacking order.
   > `Layers panel menu > New Layer`
3. Select the background photograph and drag the small coloured square beside the selected layer in the Layers panel to move the object onto the Background layer.
   > `Drag the coloured proxy square`
4. Move the remaining images and text frames onto their appropriate layers the same way, then lock the Background layer by clicking its lock column so it stops being selected by accident.
   > `Layers panel > lock column`
5. Toggle the eye icon on Text-ZH and Text-MS to hide them, confirming only the English version is visible.
   > `Layers panel > visibility eye`
6. Select an outlet icon and use the Control panel to set exact X, Y, W and H values; click the chain icon first to constrain proportions.
   > `Control panel  ·  X / Y / W / H`
7. Open Window > Object & Layout > Transform and rotate the icon 15 degrees, then use Object > Transform > Rotate for a numeric dialog with a Copy option.
   > `Object > Transform > Rotate`
8. Apply Object > Transform Again > Transform Again (Ctrl/Cmd+Alt/Opt+3) to repeat the last transformation on another object.
   > `Object > Transform Again  ·  Ctrl/Cmd+Alt/Opt+3`
9. Select all six icons, open Window > Object & Layout > Align, set Align To to Align to Selection, and click Align Vertical Centers.
   > `Align panel > Align Vertical Centers`
10. In the Distribute Spacing section tick Use Spacing, enter 8 mm and click Distribute Horizontal Spacing so the gaps are identical regardless of icon width.
   > `Align panel > Distribute Spacing > Use Spacing 8 mm`
11. Click one icon a second time to make it the Key Object (its border thickens), switch Align To to Align to Key Object, align the others to it, then group them with Object > Group and save.
   > `Align to Key Object  ·  Object > Group  ·  File > Save`

## Verify Your Work

> ✅ **Done when:** The Layers panel shows five correctly named layers with the Background locked, hiding Text-ZH and Text-MS leaves a complete English layout, and the six icons sit on one baseline with exactly 8 mm between them.

## If It Doesn't Work

If an object refuses to move to another layer, its current layer is locked — unlock it in the Layers panel first. If Bring to Front appears to do nothing, the object is on a lower layer: layer order always beats object order, so move the object to a higher layer rather than re-arranging within its own.

## Discussion Questions

1. Explain the difference between the object stacking order within a layer and the stacking order of the layers themselves.
2. Why is locking an object different from hiding it, and when would you use each?
3. The Align panel offers Align to Selection, Align to Key Object, Align to Margins, Align to Page and Align to Spread. Give a production situation for Align to Key Object.
4. Distribute Horizontal Centers and Distribute Spacing with Use Spacing can give different results for objects of unequal width. Explain why, and which one Priya's icon row needs.
5. How does putting each language on its own layer save time compared with keeping three separate InDesign files?

## Reference Artwork

![Activity 12](../../courseware/assets/screens/act_layers.png)

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
