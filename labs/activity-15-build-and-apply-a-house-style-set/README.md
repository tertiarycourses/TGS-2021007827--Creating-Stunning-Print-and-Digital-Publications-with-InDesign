# Activity 15 — Build and Apply a House Style Set

**Topic 03: Refine InDesign Drawings**  ·  **LO3**  ·  TGS-2021007827

## The Situation

**Harmony Petals** has grown to three outlets and Priya now commissions two freelance designers alongside you. The three of you have produced the same brochure template three different ways: one used 11 pt Helvetica headings, one 12 pt Arial, one 11.5 pt with a different green. A franchise partner spotted the inconsistency and asked whether the brand guidelines were real. Priya wants a single locked style set built into the brochure template so that any designer who opens it produces identical typography, and a global colour change takes seconds not hours.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO3 |
| **Objective** | Refine drawings to project requirements by constructing a reusable paragraph, character and object style set that enforces a consistent house look across a publication (TSC A1, A4). |
| **You will produce** | HP_Brochure_7.indd carrying a complete house style set — Body / Body First / Heading 1 / Heading 2 / Caption paragraph styles with Based On and Next Style, two character styles, and an object style for image frames. |
| **Tools and panels** | Adobe InDesign · Paragraph Styles panel · Character Styles panel · Object Styles panel · Based On · Next Style · Quick Apply |

## What You Will Do

Convert manually formatted text into a structured style system: build paragraph styles with Based On inheritance, character styles for local emphasis, object styles for picture frames and callout boxes, then chain the styles with Next Style so a whole article formats in one command. Finally, prove the value of the system by changing one parent style.

## Step-by-Step Procedure

1. Open HP_Brochure_7.indd and inspect the manually formatted text — note the three different heading treatments across the spread.
   > `Open HP_Brochure_7.indd`
2. Click into a well-formatted body paragraph, then open Window > Styles > Paragraph Styles and choose New Paragraph Style from the panel menu; the sampled formatting is pre-loaded.
   > `Window > Styles > Paragraph Styles > New Paragraph Style`
3. Name it 'Body', confirm 10 pt / 13 pt in Basic Character Formats, set a 3 mm Space After in Indents and Spacing, and click OK.
   > `Style Name: Body  ·  Space After 3 mm`
4. Create 'Body First' with Based On set to Body, and override only one thing — First Line Indent 0 mm — to prove inheritance.
   > `New Paragraph Style > Based On: Body`
5. Create 'Heading 1' at 20 pt bold in the Harmony Petals green, with Space Before 6 mm and Keep With Next 2 lines in the Keep Options pane.
   > `Keep Options > Keep with Next 2 lines`
6. Create 'Heading 2' Based On Heading 1 at 14 pt, then create 'Caption' at 8 pt italic.
7. Edit Heading 1 and set Next Style to Body First; edit Body First and set Next Style to Body, so the chain runs automatically.
   > `Style Options > General > Next Style`
8. Select the whole article, right-click Heading 1 in the panel and choose 'Apply Heading 1 then Next Style' to format the article in one action.
   > `Right-click style > Apply [style] then Next Style`
9. Clear any remaining local overrides by Alt/Option-clicking the style name, and confirm the plus sign disappears from the panel.
   > `Alt/Option + click the style name`
10. Select a formatted image frame with a 0.5 pt green stroke and a 2 mm text wrap, then choose New Object Style from the Object Styles panel menu and name it 'Product Image'.
   > `Window > Styles > Object Styles > New Object Style`
11. Apply 'Product Image' to the other three picture frames, then edit the 'Body' style's typeface once and watch every dependent style update across the document.

## Verify Your Work

> ✅ **Done when:** Every paragraph in the brochure shows a style name with no plus sign, all four image frames report the 'Product Image' object style, and changing the Body typeface propagates to Body First automatically.

## If It Doesn't Work

A style applies but the text does not change? Local overrides are winning — Alt/Option-click the style name to apply and clear overrides, or use Clear Overrides in the panel footer. If editing the parent does not change a child, the child's own definition overrides that attribute; delete the attribute from the child rather than editing it again.

## Discussion Questions

1. What does the Based On field actually inherit, and what happens to every child style when you change the parent's typeface?
2. A style name in the Paragraph Styles panel shows a plus sign next to it. What does that mean and how do you clear it?
3. Explain when you would use a character style rather than a second paragraph style.
4. Next Style lets you format an entire article in one command. What must be true about the text's paragraph order for that to work?
5. An object style can control fill, stroke, effects, text wrap and frame fitting. Why is that more valuable on a 40-page catalogue than on a one-page flyer?

## Reference Artwork

![Activity 15](../../courseware/assets/screens/nested_styles.png)

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
