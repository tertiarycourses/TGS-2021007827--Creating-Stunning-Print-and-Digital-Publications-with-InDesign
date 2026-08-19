# Activity 17 — Add Hyperlinks, Buttons and QR Codes for an Interactive Document

**Topic 03: Refine InDesign Drawings**  ·  **LO3**  ·  TGS-2021007827

## The Situation

**Harmony Petals** is emailing a digital gift catalogue to its 4,200-strong corporate mailing list ahead of Chinese New Year. The first draft went out last year as a flat PDF; the e-commerce report showed only 11 clicks because none of the product names were linked and customers had to retype the URL. Priya wants every product to link to its online store page, a prominent 'Order Now' button on the cover, and a QR code on the back page so recipients reading a printed copy at the office can scan straight to the WhatsApp ordering line.

## At a Glance

| | |
|---|---|
| **Learning outcome** | LO3 |
| **Objective** | Refine a publication for a digital medium by adding hyperlinks, interactive buttons and generated QR codes that function reliably in the exported file (TSC A3, A4). |
| **You will produce** | HP_InteractiveDoc_A.indd with every product name hyperlinked to its store URL, a working 'Order Now' button with a rollover state, and a scannable vector QR code on the back page. |
| **Tools and panels** | Adobe InDesign · Hyperlinks panel · Buttons and Forms panel · Object > Generate QR Code · EPUB Interactivity Preview · Window > Interactive |

## What You Will Do

Turn a static catalogue into a working interactive document: create and manage URL and cross-reference hyperlinks with shared destinations, convert an object into a button with a rollover appearance and a Go To URL action, and generate a live vector QR code directly in InDesign. You then test everything before export.

## Step-by-Step Procedure

1. Open HP_InteractiveDoc_A.indd and switch to the Interactive workspace so the relevant panels are visible.
   > `Window > Workspace > Interactive for PDF`
2. Select the first product name with the Type tool, open Window > Interactive > Hyperlinks and choose New Hyperlink from the panel menu.
   > `Window > Interactive > Hyperlinks > New Hyperlink`
3. Set Link To: URL, enter the store URL, tick Shared Hyperlink Destination, and assign the character style 'Hyperlink' so links look clickable.
   > `New Hyperlink > Link To: URL  ·  Shared Hyperlink Destination`
4. Repeat for the remaining products, reusing the shared destination from the URL dropdown where two products point at the same category page.
5. Create an internal cross-reference from the contents page to the 'Delivery Terms' heading using New Cross-Reference in the Hyperlinks panel menu.
   > `Hyperlinks panel menu > New Cross-Reference`
6. Draw the 'Order Now' shape on the cover, select it, and choose Object > Interactive > Convert to Button.
   > `Object > Interactive > Convert to Button`
7. In Window > Interactive > Buttons and Forms, name the button 'OrderNow', set Event to On Release or Tap and add the action Go To URL with the store address.
   > `Buttons and Forms > Event: On Release or Tap  ·  Action: Go To URL`
8. Click [Rollover] in the Appearance list and change the fill to the darker house green so the button responds to the cursor.
   > `Buttons and Forms > Appearance > [Rollover]`
9. Go to the back page, choose Object > Generate QR Code, select Type: Web Hyperlink and enter the WhatsApp ordering link, then set the colour swatch.
   > `Object > Generate QR Code`
10. Click OK and place the loaded QR cursor in a frame at least 25 x 25 mm so it remains scannable in print.
11. Test everything with Window > Interactive > EPUB Interactivity Preview, click Play, and verify each link, the button rollover and the cross-reference.
   > `Window > Interactive > EPUB Interactivity Preview`

## Verify Your Work

> ✅ **Done when:** Every product name opens its store page and the 'Order Now' button changes colour on rollover in the EPUB Interactivity Preview, and a phone camera scanning the QR code opens the WhatsApp ordering line.

## If It Doesn't Work

Links dead in the exported PDF? You exported Adobe PDF (Print) with Hyperlinks unticked — re-export using File > Export > Adobe PDF (Interactive), or tick Include Hyperlinks in the Print PDF's General pane. A QR code that will not scan is almost always too small or too low-contrast: enlarge it past 25 mm and keep it a dark colour on a plain light background with clear space around it.

## Discussion Questions

1. What is the difference between a hyperlink and a button in InDesign, and which export formats support each?
2. Shared hyperlink destinations let one URL serve many links. Why does that matter when the store changes its domain?
3. A button needs a Normal and a Rollover appearance. Why does a Rollover state improve conversion, and where does it have no effect at all?
4. InDesign generates QR codes as live vector objects rather than placed images. What two practical advantages does that give the print production team?
5. Your hyperlinks work in the InDesign preview but not in the exported PDF. Name the two most likely causes in the export settings.

## Reference Artwork

![Activity 17](../../courseware/assets/screens/act_hyperlink.png)

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
