# candidate photos (no faces or Luke-only, not screenshots) -> thumbs/ (new JPEG, no EXIF)
import json,os
from PIL import Image, ImageOps
d=json.load(open('photos.json'))
us=[p for p in d if '2023-08-22'<=p['date'][:10]<='2023-09-11']
us.sort(key=lambda p:p['date'])
meta=[]
for p in us:
    per=set(p.get('persons') or [])
    ok = (not per) or per=={'Apple'}
    if not ok or p.get('screenshot'): continue
    ders=[x for x in (p.get('path_derivatives') or []) if os.path.exists(x) and x.lower().endswith(('.jpeg','.jpg','.heic'))]
    if not ders: print('none',p['uuid'][:8],p['date']); continue
    src=max(ders,key=os.path.getsize)
    out=f"thumbs/{p['date'][5:10]}_{p['date'][11:16].replace(':','')}_{p['uuid'][:8]}.jpg"
    if not os.path.exists(out):
        im=ImageOps.exif_transpose(Image.open(src)).convert('RGB'); im.thumbnail((900,900)); im.save(out,'JPEG',quality=78)
    meta.append({'uuid':p['uuid'],'file':out,'date':p['date'],'lat':p['latitude'],'lon':p['longitude'],'luke':'Apple' in per,'video':p['ismovie'],'place':(p.get('place') or {}).get('name'),'caption':p.get('ai_caption')})
json.dump(meta,open('thumbs.json','w'),ensure_ascii=False,indent=1)
print(len(meta))
