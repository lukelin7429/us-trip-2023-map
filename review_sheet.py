# Contact sheet of every photo the page publishes, grouped by stop (for Luke to review).
import json
from PIL import Image, ImageDraw, ImageFont
d=json.load(open('docs/data.json'))
F=ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc',20,index=0)
FT=ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc',26,index=0)
W,H,cols=210,150,9
rows=[]
for s in d['stops']:
    if s['photos']: rows.append(s)
pages=[rows[:24],rows[24:48],rows[48:]]
for pi,rs in enumerate(pages):
    hgt=sum(40+((len(s['photos'])+cols-1)//cols)*(H+8) for s in rs)+20
    img=Image.new('RGB',(cols*W+20,hgt),'#faf7f2');dr=ImageDraw.Draw(img);y=10
    for s in rs:
        dr.text((10,y),f"{d['days'][s['day']]['d']} {s['t']}  {s['zh']}",fill='#222',font=FT);y+=36
        for i,p in enumerate(s['photos']):
            im=Image.open(f"docs/img/{p['id']}_s.jpg");im.thumbnail((W-8,H-8))
            x=10+(i%cols)*W;yy=y+(i//cols)*(H+8);img.paste(im,(x,yy))
        y+=((len(s['photos'])+cols-1)//cols)*(H+8)+4
    img.save(f'shots/review_{pi+1}.jpg',quality=78)
print('ok')
