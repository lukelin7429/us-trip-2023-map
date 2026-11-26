import json
from PIL import Image, ImageDraw, ImageFont
m=json.load(open('thumbs.json'))
f=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',18)
W=240;H=240;cols=8;N=48
for s in range(0,len(m),N):
    chunk=m[s:s+N]; rows=(len(chunk)+cols-1)//cols
    sh=Image.new('RGB',(cols*W,rows*(H+24)),'white'); dr=ImageDraw.Draw(sh)
    for i,x in enumerate(chunk):
        im=Image.open(x['file']); im.thumbnail((W-6,H-6))
        cx=(i%cols)*W; cy=(i//cols)*(H+24)
        sh.paste(im,(cx+3,cy+3)); dr.text((cx+4,cy+H+1),f"{s+i} {x['date'][5:16].replace('T',' ')}{' L' if x['luke'] else ''}{' V' if x['video'] else ''}",fill='black',font=f)
    sh.save(f'sheets/s{s//N:02d}.jpg',quality=72)
print((len(m)+N-1)//N)
