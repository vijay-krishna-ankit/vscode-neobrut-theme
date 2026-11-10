"""Build the geometric NeuBrut product icon font (requires fonttools)."""
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Coordinates use a 16 by 16 grid, with the origin at the bottom left.
def poly(pen, pts):
    pen.moveTo(tuple(int(v * 64) for v in pts[0]))
    for pt in pts[1:]: pen.lineTo(tuple(int(v * 64) for v in pt))
    pen.closePath()
def rect(p, x, y, w, h): poly(p, [(x,y),(x,y+h),(x+w,y+h),(x+w,y)])
def line(p, x1,y1,x2,y2,w=1.5):
    dx,dy=x2-x1,y2-y1; length=math.hypot(dx,dy); nx,ny=-dy*w/length/2,dx*w/length/2
    poly(p,[(x1+nx,y1+ny),(x2+nx,y2+ny),(x2-nx,y2-ny),(x1-nx,y1-ny)])
def frame(p,x,y,w,h,t=1.4):
    rect(p,x,y,w,t); rect(p,x,y+h-t,w,t); rect(p,x,y+t,t,h-2*t); rect(p,x+w-t,y+t,t,h-2*t)
def explorer(p):
    frame(p,2,2,10,12); rect(p,5,0.8,9,1.3); rect(p,12.7,1,1.3,10); rect(p,4,11,5,1.1)
def search(p):
    # Octagonal lens and a blocky diagonal handle.
    poly(p, [(2,7),(2,11),(4,13),(8,13),(10,11),(10,7),(8,5),(4,5)])
    poly(p, [(3.5,7.7),(4.7,6.5),(7.3,6.5),(8.5,7.7),(8.5,10.3),(7.3,11.5),(4.7,11.5),(3.5,10.3)])
    line(p,9,5.8,13.7,1.4,1.8)
def source(p):
    frame(p,2,11,3.4,3.4,1); frame(p,2,1,3.4,3.4,1); frame(p,10.5,10.5,3.4,3.4,1); rect(p,3.1,4,1.3,7.5); line(p,4,6,12,11,1.3)
def run(p):
    # Squared-off scarab: split rectangular shell, compact head and angular legs.
    poly(p, [(3.5,4),(3.5,11.5),(4.5,12.5),(7.2,12.5),(7.2,3),(4.5,3)])
    poly(p, [(8.8,3),(8.8,12.5),(11.5,12.5),(12.5,11.5),(12.5,4),(11.5,3)])
    rect(p,5.5,12.7,5,1.5)
    line(p,6,13.6,5,15,1); line(p,10,13.6,11,15,1)
    rect(p,1.5,10,2.3,1.2); rect(p,12.2,10,2.3,1.2)
    rect(p,1.5,7,2.3,1.2); rect(p,12.2,7,2.3,1.2)
    line(p,3.8,4.8,1.8,3.3,1.2); line(p,12.2,4.8,14.2,3.3,1.2)
def extensions(p):
    # Integer-aligned, squared strokes keep the outline crisp at small sizes.
    points=[(2,9),(2,13),(6,13),(6,15),(9,15),(9,13),
            (12,13),(12,9),(14,9),(14,6),(12,6),(12,2),
            (9,2),(9,4),(6,4),(6,2),(2,2),(2,6),(4,6),(4,9)]
    for (x1,y1),(x2,y2) in zip(points,points[1:]+points[:1]):
        if x1 == x2: rect(p,x1-0.75,min(y1,y2)-0.75,1.5,abs(y2-y1)+1.5)
        else: rect(p,min(x1,x2)-0.75,y1-0.75,abs(x2-x1)+1.5,1.5)
def test(p):
    rect(p,5,13,6,1.4); rect(p,6,9,1.4,4); rect(p,8.6,9,1.4,4); line(p,6.7,9,2.5,2.3,1.5); line(p,9.3,9,13.5,2.3,1.5); rect(p,2,1.4,12,1.5); rect(p,4,4.2,8,1.3)
def settings(p):
    frame(p,2,2,12,12,2); frame(p,5.2,5.2,5.6,5.6,1.4); rect(p,7,0,2,3); rect(p,7,13,2,3); rect(p,0,7,3,2); rect(p,13,7,3,2)
def account(p):
    frame(p,5,9,6,6,1.5); frame(p,2,1,12,6,1.5)
names={'explorer-view-icon':explorer,'search-view-icon':search,'source-control-view-icon':source,'run-view-icon':run,'extensions-view-icon':extensions,'test-view-icon':test,'settings-view-bar-icon':settings,'accounts-view-bar-icon':account}
fb=FontBuilder(1024,isTTF=True); glyphs={}; metrics={}; cmap={}; order=['.notdef']+list(names)
for index,name in enumerate(order):
    pen=TTGlyphPen(None)
    if name != '.notdef': names[name](pen); cmap[0xE900+index-1]=name
    glyph=pen.glyph()
    if name != '.notdef' and glyph.numberOfContours:
        glyph.recalcBounds({})
        shift=round((1024-glyph.xMin-glyph.xMax)/2)
        glyph.coordinates.translate((shift,0))
    glyphs[name]=glyph; metrics[name]=(1024,0)
fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics)
fb.setupHorizontalHeader(ascent=1024,descent=0); fb.setupNameTable({'familyName':'NeuBrut Icons','styleName':'Regular','uniqueFontIdentifier':'NeuBrut Icons Regular','fullName':'NeuBrut Icons Regular','psName':'NeuBrutIcons-Regular'})
fb.setupOS2(sTypoAscender=1024,sTypoDescender=0,usWinAscent=1024,usWinDescent=0); fb.setupPost(); fb.setupMaxp()
fb.font.flavor='woff'; fb.save(ROOT/'producticons'/'neubrut-icons.woff')
