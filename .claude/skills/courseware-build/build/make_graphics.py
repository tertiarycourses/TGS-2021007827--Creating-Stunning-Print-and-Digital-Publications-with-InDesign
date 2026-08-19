#!/usr/bin/env python3
"""Generate the deck's custom concept graphics as crisp, on-brand PNG diagrams.

These are the visuals the legacy deck never had: the anatomy of a print page
(trim/bleed/slug/margin), the CMYK vs RGB gamut, the frame-vs-content model,
the text-threading flow, the styles cascade, the resolution ladder, the export
decision matrix and the InDesign workspace map. Rendered with PIL at 3x scale
so they stay sharp when placed on a 13.33in slide.

Run:  python3 make_graphics.py
Out:  courseware/assets/gen/*.png
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
def _find_repo(start):
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))
REPO = os.environ.get("COURSE_REPO") or _find_repo(HERE)
OUT = os.path.join(REPO, "courseware", "assets", "gen")
os.makedirs(OUT, exist_ok=True)

S = 3                                     # supersample factor
# When True the diagrams omit their internal title/subtitle — the slide supplies it.
HEADLESS = os.environ.get("GRAPHICS_HEADLESS", "1") == "1"
TOP_TRIM = 96                             # vertical space the heading would occupy
BLUE=(0x1F,0x6F,0xEB); TEAL=(0x10,0xB9,0x81); AMBER=(0xF5,0x9E,0x0B)
INK=(0x16,0x1B,0x26); GREY=(0x5B,0x63,0x72); LIGHT=(0xF5,0xF8,0xFC)
WHITE=(255,255,255); LINE=(0xE2,0xE8,0xF0); VIOLET=(0x7C,0x3A,0xED)
RED=(0xE1,0x1D,0x48); CYAN=(0x00,0xAE,0xEF); MAG=(0xEC,0x00,0x8C); YEL=(0xFF,0xF2,0x00)

FB="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FR="/System/Library/Fonts/Supplemental/Arial.ttf"
def fnt(sz, bold=False):
    return ImageFont.truetype(FB if bold else FR, sz*S)

def canvas(w, h, bg=WHITE):
    if HEADLESS: h -= TOP_TRIM
    im = Image.new("RGB", (w*S, h*S), bg)
    return im, ImageDraw.Draw(im)

def heading(d, title, sub, x=40, y=36):
    """Draw the diagram's own title/subtitle, unless the slide supplies it."""
    if HEADLESS: return
    text(d,(x,y),title,20,INK,True,raw=True)
    if sub: text(d,(x,y+32),sub,12,GREY,raw=True)

def Y(v):
    """Shift a y coordinate up when the internal heading is suppressed."""
    return v - TOP_TRIM if HEADLESS else v

def save(im, name):
    w, h = im.size
    im = im.resize((w//S, h//S), Image.LANCZOS)
    p = os.path.join(OUT, name + ".png")
    im.save(p, optimize=True)
    print("  ", name + ".png", im.size)

# Every y coordinate is shifted up by TOP_TRIM in headless mode, so the existing
# layout numbers stay valid and the whole diagram simply moves into the freed space.
DY = -TOP_TRIM if HEADLESS else 0
_DY_DEFAULT = DY

def _b(box):
    """Offset a [x0,y0,x1,y1] box vertically."""
    return [box[0], box[1]+DY, box[2], box[3]+DY]

def rr(d, box, r, fill=None, outline=None, width=2):
    d.rounded_rectangle([b*S for b in _b(box)], radius=r*S, fill=fill, outline=outline,
                        width=int(width*S))

def rect(d, box, fill=None, outline=None, width=2):
    d.rectangle([b*S for b in _b(box)], fill=fill, outline=outline, width=int(width*S))

def text(d, xy, s, size=14, color=INK, bold=False, anchor="la", raw=False):
    y = xy[1] if raw else xy[1]+DY
    d.text((xy[0]*S, y*S), s, font=fnt(size, bold), fill=color, anchor=anchor)

def ctext(d, cx, cy, s, size=14, color=INK, bold=False):
    text(d, (cx, cy), s, size, color, bold, anchor="mm")

def arrow(d, p1, p2, color=BLUE, width=3, head=9):
    x1,y1=p1[0]*S,(p1[1]+DY)*S; x2,y2=p2[0]*S,(p2[1]+DY)*S
    d.line([x1,y1,x2,y2], fill=color, width=int(width*S))
    a=math.atan2(y2-y1, x2-x1); h=head*S
    d.polygon([(x2,y2),
               (x2-h*math.cos(a-0.42), y2-h*math.sin(a-0.42)),
               (x2-h*math.cos(a+0.42), y2-h*math.sin(a+0.42))], fill=color)

def dashed(d, p1, p2, color, width=2, dash=8, gap=6):
    x1,y1=p1[0],p1[1]+DY; x2,y2=p2[0],p2[1]+DY
    L=math.hypot(x2-x1,y2-y1)
    if L==0: return
    ux,uy=(x2-x1)/L,(y2-y1)/L; t=0
    while t < L:
        e=min(t+dash, L)
        d.line([(x1+ux*t)*S,(y1+uy*t)*S,(x1+ux*e)*S,(y1+uy*e)*S], fill=color, width=int(width*S))
        t=e+gap

def wrap(d, s, size, bold, maxw):
    f=fnt(size,bold); words=s.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t, font=f) <= maxw*S: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def tick(d, cx, cy, r=7, color=WHITE, width=2.4):
    """A drawn check mark — Arial has no U+2713 glyph, which renders as a box."""
    pts=[(cx-r*0.55, cy+r*0.05), (cx-r*0.12, cy+r*0.48), (cx+r*0.6, cy-r*0.45)]
    d.line([(p[0]*S,(p[1]+DY)*S) for p in pts], fill=color, width=int(width*S), joint="curve")

def para(d, xy, s, size=12, color=GREY, bold=False, maxw=200, lh=None):
    lh = lh or size+4
    for i,ln in enumerate(wrap(d,s,size,bold,maxw)):
        text(d,(xy[0], xy[1]+i*lh), ln, size, color, bold)
    return len(wrap(d,s,size,bold,maxw))*lh


# ---------------------------------------------------------------- 1. page anatomy
def g_page_anatomy():
    # This diagram's artwork already starts at the very top of its canvas, so it
    # opts out of the headless up-shift and simply uses a canvas with no heading band.
    global DY
    DY = 0
    im,d = canvas(900, 470+TOP_TRIM)
    ox,oy = 330, 60
    W,H = 270, 350
    B = 20           # bleed band
    M = 30           # margin inset
    # slug
    rect(d,[ox-B-24, oy-B-24, ox+W+B+24, oy+H+B+24], fill=(0xFA,0xFA,0xFC), outline=LINE, width=1)
    # bleed
    rect(d,[ox-B, oy-B, ox+W+B, oy+H+B], fill=(0xFD,0xE7,0xEC), outline=None)
    # trim (the page)
    rect(d,[ox, oy, ox+W, oy+H], fill=WHITE, outline=INK, width=2)
    # photo bleeding off the bottom edge — clipped to the bleed box, drawn first
    rect(d,[ox-B, oy+H-90, ox+W+B, oy+H+B], fill=(0xCF,0xE6,0xDC))
    rect(d,[ox, oy, ox+W, oy+H], outline=INK, width=2)
    ctext(d, ox+W/2, oy+H-46, "photo runs off the trim", 10, (0x2F,0x6F,0x5C), True)
    # margin
    dashed(d,(ox+M,oy+M),(ox+W-M,oy+M),MAG,2); dashed(d,(ox+M,oy+H-M),(ox+W-M,oy+H-M),MAG,2)
    dashed(d,(ox+M,oy+M),(ox+M,oy+H-M),MAG,2); dashed(d,(ox+W-M,oy+M),(ox+W-M,oy+H-M),MAG,2)
    # live matter block
    rect(d,[ox+M+6, oy+M+10, ox+W-M-6, oy+M+74], fill=(0xE8,0xF0,0xFE))
    ctext(d, ox+W/2, oy+M+42, "LIVE MATTER", 11, BLUE, True)
    for i in range(6):
        y=oy+M+92+i*15
        rect(d,[ox+M+6, y, ox+W-M-6-(0 if i<5 else 56), y+6], fill=(0xE6,0xEA,0xF0))
    # leader labels on the right
    for ly, lt, lc in [(oy-B+4,"bleed",RED),(oy+4,"trim",INK),(oy+M+2,"margin",MAG)]:
        dashed(d,(ox+W+B+4,ly),(ox+W+B+22,ly),lc,1,4,3)
        text(d,(ox+W+B+26,ly-6),lt,9,lc,True)

    heading(d,"Anatomy of a Print Page","Every specification a printer needs.")
    items=[(RED,"Bleed  ·  3 mm","Artwork extends past the trim so a 1 mm cutting drift never shows a white sliver."),
           (INK,"Trim  ·  210 x 148 mm","The finished cut size — the 'page size' you type into New Document."),
           (MAG,"Margin  ·  5 mm","Safety zone. No live matter (text, logos, prices) may sit outside it."),
           (GREY,"Slug","Area outside the bleed carrying job name, colour bars and printer's marks."),
           ((0x2F,0x6F,0x5C),"Live matter","Everything that must survive the cut — held inside the margin.")]
    y=112
    for col,t,c in items:
        rect(d,[40,y+3,52,y+15], fill=col)
        text(d,(62,y),t,13,INK,True)
        y += 20
        y += para(d,(62,y),c,11,GREY,maxw=210)
        y += 12
    save(im,"page_anatomy")
    DY = _DY_DEFAULT

# ---------------------------------------------------------------- 2. colour modes
def g_colour_modes():
    im,d = canvas(900, 470)
    heading(d,"Colour Mode Follows the Output","Choosing the wrong mode in New Document silently sets the wrong colour space for the whole job.")

    # CMYK subtractive
    cx,cy=210,220; r=68
    for col,dx,dy in [(CYAN,-34,-20),(MAG,34,-20),(YEL,0,34)]:
        ov=Image.new("RGBA",(im.size[0],im.size[1]),(0,0,0,0)); od=ImageDraw.Draw(ov)
        od.ellipse([(cx+dx-r)*S,(cy+dy-r+DY)*S,(cx+dx+r)*S,(cy+dy+r+DY)*S], fill=col+(150,))
        im.alpha_composite(ov) if im.mode=="RGBA" else im.paste(Image.alpha_composite(im.convert("RGBA"),ov).convert("RGB"),(0,0))
    d=ImageDraw.Draw(im)
    ctext(d,cx,cy+124,"CMYK  ·  Subtractive",15,INK,True)
    ctext(d,cx,cy+148,"Ink on paper. Inks absorb light;",11,GREY)
    ctext(d,cx,cy+165,"more ink = darker. For print.",11,GREY)

    # RGB additive
    cx=690
    for col,dx,dy in [((255,0,0),-34,-20),((0,255,0),34,-20),((0,0,255),0,34)]:
        ov=Image.new("RGBA",(im.size[0],im.size[1]),(0,0,0,0)); od=ImageDraw.Draw(ov)
        od.ellipse([(cx+dx-r)*S,(cy+dy-r+DY)*S,(cx+dx+r)*S,(cy+dy+r+DY)*S], fill=col+(140,))
        im.paste(Image.alpha_composite(im.convert("RGBA"),ov).convert("RGB"),(0,0))
    d=ImageDraw.Draw(im)
    ctext(d,cx,cy+124,"RGB  ·  Additive",15,INK,True)
    ctext(d,cx,cy+148,"Light on a screen. More light",11,GREY)
    ctext(d,cx,cy+165,"= brighter. For digital.",11,GREY)

    # verdict band
    rr(d,[40,406,860,458],8,fill=(0xFF,0xF7,0xE8),outline=AMBER,width=2)
    text(d,(60,416),"WATCH OUT",10,AMBER,True)
    text(d,(60,432),"RGB has a wider gamut than CMYK. Bright RGB greens and oranges shift visibly when converted for press — always proof in CMYK.",11,INK)
    save(im,"colour_modes")

# ---------------------------------------------------------------- 3. frame vs content
def g_frame_content():
    im,d = canvas(900, 400)
    heading(d,"The Frame and Its Content Are Two Different Things","Almost every beginner problem in InDesign is a wrong-selection-tool problem.")

    for i,(x, tool, key, col, cap, sub) in enumerate([
        (60,  "Selection tool", "V", BLUE, "Selects the FRAME",
         "Moves and resizes the container. The picture inside is cropped, not scaled."),
        (480, "Direct Selection", "A", TEAL, "Selects the CONTENT",
         "Moves and scales the image inside the frame, or edits a path's anchor points."),
    ]):
        rr(d,[x,110,x+360,360],10,fill=LIGHT,outline=LINE,width=2)
        rect(d,[x,110,x+360,118],fill=col)
        rr(d,[x+22,136,x+62,176],6,fill=col)
        ctext(d,x+42,156,key,18,WHITE,True)
        text(d,(x+76,140),tool,15,INK,True)
        text(d,(x+76,162),cap,12,col,True)
        # mini illustration: frame with photo
        # mini illustration below
        rect(d,[x+30,200,x+180,308], fill=(0xDC,0xE9,0xF8), outline=col if i==0 else LINE, width=3 if i==0 else 1)
        rect(d,[x+52,214,x+204,296], fill=(0xB9,0xD8,0xC9), outline=col if i==1 else LINE, width=3 if i==1 else 1)
        ctext(d,x+128,255,"content",10,(0x2F,0x6F,0x5C),True)
        # handles
        hs = [(x+30,200),(x+180,200),(x+30,308),(x+180,308)] if i==0 else [(x+52,214),(x+204,214),(x+52,296),(x+204,296)]
        for hx,hy in hs:
            rect(d,[hx-4,hy-4,hx+4,hy+4], fill=col)
        para(d,(x+218,206),sub,11,GREY,maxw=128)
    save(im,"frame_content")

# ---------------------------------------------------------------- 4. threading
def g_threading():
    im,d = canvas(900, 400)
    heading(d,"Threading: One Story, Many Frames","Click the out port, then click the next frame. A red + means overset text — copy with nowhere to sit.")
    xs=[70, 330, 590]
    for i,x in enumerate(xs):
        rect(d,[x,120,x+210,320], fill=WHITE, outline=(BLUE if i<2 else RED), width=2)
        for r in range(9):
            w = 178 if r<8 else 110
            rect(d,[x+16,140+r*19, x+16+w,140+r*19+7], fill=(0xE3,0xE9,0xF2))
        # in port (top-left) / out port (bottom-right)
        rect(d,[x-7,127,x+7,141], fill=(WHITE if i==0 else BLUE), outline=BLUE, width=2)
        ocol = RED if i==2 else BLUE
        rect(d,[x+203,299,x+217,313], fill=(WHITE if i==2 else ocol), outline=ocol, width=2)
        if i==2:
            ctext(d,x+210,306,"+",13,RED,True)
        ctext(d,x+105,338,f"Frame {i+1}",12,INK,True)
        if i<2:
            arrow(d,(x+222,306),(xs[i+1]-14,134),BLUE,3,9)
    rr(d,[590,120,800,320],0,fill=None,outline=RED,width=2)
    text(d,(70,360),"in port",10,GREY); text(d,(232,360),"out port",10,GREY)
    rr(d,[590,352,860,392],8,fill=(0xFE,0xEC,0xF0),outline=RED,width=2)
    text(d,(606,362),"OVERSET",10,RED,True)
    text(d,(606,376),"Thread another frame, or the copy never prints.",10,INK)
    save(im,"threading")

# ---------------------------------------------------------------- 5. styles cascade
def g_styles():
    im,d = canvas(900, 420)
    heading(d,"The Styles Cascade — Change Once, Update Everywhere","The single largest productivity multiplier in InDesign.")
    tiers=[("Parent style","[Basic Paragraph] — the root all others are Based On",VIOLET,110),
           ("Paragraph style","Body Text · 10/12 pt Minion · justified · 3 mm indent",BLUE,190),
           ("Character style","Lead-in Bold — overrides only the selected characters",TEAL,270),
           ("Object / Table / Cell style","Frame, stroke, effects, table borders and cell insets",AMBER,350)]
    for name,desc,col,y in tiers:
        rr(d,[60,y,520,y+58],8,fill=LIGHT,outline=LINE,width=2)
        rect(d,[60,y,70,y+58], fill=col)
        text(d,(88,y+11),name,14,INK,True)
        text(d,(88,y+33),desc,11,GREY)
        if y<350: arrow(d,(290,y+60),(290,y+76),col,3,8)
    # right: the payoff
    rr(d,[560,110,860,298],8,fill=(0xEE,0xF7,0xF3),outline=TEAL,width=2)
    text(d,(582,126),"WHY IT MATTERS",10,TEAL,True)
    para(d,(582,148),"Redefine 'Body Text' from 10 pt to 9.5 pt and every one of 200 pages reflows in a second.",12,INK,maxw=258,lh=17)
    para(d,(582,214),"A '+' beside a style name means a local override — the warning sign that someone formatted by hand.",11,GREY,maxw=258,lh=15)
    rr(d,[560,316,860,392],8,fill=(0xFF,0xF7,0xE8),outline=AMBER,width=2)
    text(d,(582,330),"BASED ON  +  NEXT STYLE",10,AMBER,True)
    para(d,(582,350),"Based On cascades global changes. Next Style makes a heading flow straight into body copy as you type.",10,INK,maxw=258,lh=14)
    save(im,"styles_cascade")

# ---------------------------------------------------------------- 6. resolution ladder
def g_resolution():
    im,d = canvas(900, 380)
    heading(d,"Resolution Follows the Medium","Effective PPI — not the file's native PPI — is what actually prints.")
    rows=[("300 ppi","Offset & digital print",TEAL,"Sharp at final size. The printer's minimum for photographs.",300),
          ("150 ppi","Large format / posters",BLUE,"Viewed from a distance, so a lower resolution is acceptable.",150),
          ("72 ppi","Screen, EPUB, web PDF",AMBER,"Matches the display. Larger files bring no visible benefit.",72),
          ("Vector","Logos, type, icons",VIOLET,"Resolution-independent. Scales to any size without loss.",380)]
    y=110
    for label,use,col,note,bar in rows:
        rr(d,[60,y,840,y+56],8,fill=LIGHT,outline=LINE,width=1)
        rect(d,[60,y,70,y+56], fill=col)
        text(d,(88,y+8),label,15,col,True)
        text(d,(88,y+32),use,11,GREY)
        rect(d,[250,y+22,250+bar*0.62,y+34], fill=col)
        text(d,(560,y+20),note,11,INK)
        y+=66
    rr(d,[60,y,840,y+52],8,fill=(0xFE,0xEC,0xF0),outline=RED,width=2)
    text(d,(80,y+10),"SCALE UP = RESOLUTION DOWN",10,RED,True)
    text(d,(80,y+28),"Enlarge a 300 ppi photo to 200% in InDesign and its effective resolution halves to 150 ppi. Check the Links panel, every time.",11,INK)
    save(im,"resolution_ladder")

# ---------------------------------------------------------------- 7. export matrix
def g_export():
    im,d = canvas(900, 330)
    heading(d,"Choose the Export by the Destination","One layout, many outputs — each with its own non-negotiable settings.")
    cards=[("PDF/X-1a  ·  PDF/X-4","Commercial print",TEAL,
            ["CMYK, flattened (X-1a)","3 mm bleed + crop marks","Fonts embedded","Send to Sun Ray Printers"]),
           ("PDF (Interactive)","On-screen document",BLUE,
            ["RGB, hyperlinks live","Buttons and page transitions","Video and audio play","E-mail or LMS delivery"]),
           ("EPUB Reflowable","Text-led e-book",VIOLET,
            ["Text reflows to the device","Reader controls type size","Styles map to CSS","Novels, reports, guides"]),
           ("EPUB Fixed Layout","Design-led e-book",AMBER,
            ["Layout preserved exactly","Animation survives","Larger file size","Children's books, magazines"])]
    x=48
    for title,use,col,pts in cards:
        rr(d,[x,104,x+196,306],10,fill=LIGHT,outline=LINE,width=2)
        rect(d,[x,104,x+196,114], fill=col)
        for i,ln in enumerate(wrap(d,title,13,True,168)):
            text(d,(x+16,126+i*18),ln,13,INK,True)
        text(d,(x+16,170),use,11,col,True)
        yy=196
        for p in pts:
            d.ellipse([(x+18)*S,(yy+4+DY)*S,(x+24)*S,(yy+10+DY)*S], fill=col)
            n=para(d,(x+32,yy),p,10,GREY,maxw=150,lh=13)
            yy+=max(n,13)+8
        x+=210
    save(im,"export_matrix")

# ---------------------------------------------------------------- 8. workspace map
def g_workspace():
    im,d = canvas(900, 430)
    heading(d,"The InDesign Workspace","Save your own arrangement: Window > Workspace > New Workspace.")
    # app chrome
    rr(d,[50,96,850,404],8,fill=(0xF7,0xF9,0xFC),outline=LINE,width=2)
    rect(d,[50,96,850,124], fill=(0x2B,0x31,0x3D))
    text(d,(66,103),"Adobe InDesign  —  Harmony_Flyer.indd @ 100%",11,WHITE,True)
    # control panel
    rect(d,[50,124,850,152], fill=(0xE8,0xEC,0xF2))
    text(d,(66,131),"Control panel  ·  changes with what you have selected",11,INK,True)
    # tools
    rect(d,[50,152,96,404], fill=(0x3A,0x41,0x4F))
    for i in range(11):
        rect(d,[62,166+i*20,84,182+i*20], fill=(0x9A,0xA4,0xB4) if i not in (0,3) else BLUE)
    text(d,(60,392),"Tools",9,WHITE,True)
    # document window + page
    rect(d,[96,152,610,404], fill=(0xDE,0xE3,0xEA))
    rect(d,[212,182,494,376], fill=WHITE, outline=INK, width=2)
    dashed(d,(228,198),(478,198),MAG,1); dashed(d,(228,360),(478,360),MAG,1)
    dashed(d,(228,198),(228,360),MAG,1); dashed(d,(478,198),(478,360),MAG,1)
    rect(d,[240,214,466,268], fill=(0xE8,0xF0,0xFE))
    for r in range(4):
        rect(d,[240,286+r*18,466-(0 if r<3 else 90),292+r*18], fill=(0xE6,0xEA,0xF0))
    ctext(d,353,392,"pasteboard  ·  document window",10,GREY)
    # panel dock
    rect(d,[610,152,850,404], fill=(0xEE,0xF1,0xF6))
    panels=[("Pages",BLUE),("Links",TEAL),("Swatches",AMBER),("Paragraph Styles",VIOLET),
            ("Character Styles",BLUE),("Layers",TEAL),("Effects",AMBER),("Preflight",TEAL)]
    for i,(p,c) in enumerate(panels):
        yy=166+i*29
        rr(d,[622,yy,838,yy+24],4,fill=WHITE,outline=LINE,width=1)
        rect(d,[622,yy,628,yy+24], fill=c)
        text(d,(640,yy+6),p,11,INK,True)
    save(im,"workspace_map")

# ---------------------------------------------------------------- 9. preflight gate
def g_preflight():
    im,d = canvas(900, 400)
    heading(d,"The Preflight Gate — Before Every Export","A green light in the status bar is the professional's final check.")
    checks=[("Links","All linked, none modified or missing",TEAL),
            ("Resolution","Effective PPI at or above 300 for print",TEAL),
            ("Overset text","No red + on any text frame",TEAL),
            ("Colour","No stray RGB images in a CMYK job",AMBER),
            ("Fonts","Every font present and licensed",TEAL),
            ("Bleed","3 mm on all four sides, artwork extends into it",AMBER)]
    y=112
    for i,(n,desc,col) in enumerate(checks):
        x = 60 if i%2==0 else 460
        if i%2==0 and i>0: y+=76
        rr(d,[x,y,x+380,y+62],8,fill=LIGHT,outline=LINE,width=1)
        d.ellipse([(x+18)*S,(y+20+DY)*S,(x+42)*S,(y+44+DY)*S], fill=col)
        tick(d,x+30,y+32,7,WHITE,2.4)
        text(d,(x+56,y+13),n,14,INK,True)
        text(d,(x+56,y+35),desc,11,GREY)
    y+=82
    rr(d,[60,y,840,y+52],8,fill=(0xEE,0xF7,0xF3),outline=TEAL,width=2)
    text(d,(80,y+10),"THEN PACKAGE",10,TEAL,True)
    text(d,(80,y+28),"File > Package collects the INDD, every link, every font and a printing report into one folder — the correct hand-off.",11,INK)
    save(im,"preflight_gate")

# ---------------------------------------------------------------- 10. app roles
def g_app_roles():
    im,d = canvas(900, 360)
    heading(d,"Which Application Owns Which Job?","Knowing this is the single biggest efficiency gain for a junior designer.")
    apps=[("Ps","Photoshop","Pixels",BLUE,["Retouch and colour-correct photographs","Composite and mask images","Export as PSD, TIFF or JPEG"]),
          ("Ai","Illustrator","Vectors",AMBER,["Draw logos and icons","Build illustrations and maps","Export as AI, EPS or SVG"]),
          ("Id","InDesign","Layout",MAG,["Assemble type, images and artwork","Multi-page, styles, parent pages","Export print PDF, EPUB, interactive"])]
    x=60
    for code,name,role,col,pts in apps:
        rr(d,[x,110,x+250,322],10,fill=LIGHT,outline=LINE,width=2)
        rr(d,[x+20,130,x+72,182],8,fill=col)
        ctext(d,x+46,156,code,22,WHITE,True)
        text(d,(x+86,134),name,16,INK,True)
        text(d,(x+86,158),role,12,col,True)
        yy=200
        for p in pts:
            d.ellipse([(x+22)*S,(yy+4+DY)*S,(x+28)*S,(yy+10+DY)*S], fill=col)
            n=para(d,(x+38,yy),p,11,GREY,maxw=190,lh=14)
            yy+=max(n,14)+8
        if x<560: arrow(d,(x+256,216),(x+276,216),GREY,3,8)
        x+=280
    save(im,"app_roles")


if __name__ == "__main__":
    print("Generating concept graphics ->", OUT)
    for f in (g_page_anatomy, g_colour_modes, g_frame_content, g_threading, g_styles,
              g_resolution, g_export, g_workspace, g_preflight, g_app_roles):
        f()
    print("Done.")
