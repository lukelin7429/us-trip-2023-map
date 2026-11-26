# Street-level context around each public stop (2.5 km radius), in batches. Only stop coordinates are sent.
import json,urllib.request,urllib.parse,time,sys
C=json.load(open('coords.json'))
skip={'bronx910','cam97','mn'}
pts=[v for k,v in C.items() if k not in skip]+[(40.6895,-74.1745),(40.6437,-74.0735),(40.6892,-74.0445),(42.7179,-73.8335),(42.3670,-71.1056),(40.8448,-73.8648)]
EPS=['https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter']
els={}
for b in range(0,len(pts),8):
    chunk=pts[b:b+8]
    def around(sel): return ''.join(f'{sel}(around:2500,{la},{lo});' for la,lo in chunk)
    q='[out:json][timeout:170];('+around('way["highway"~"^(primary|secondary|tertiary)$"]')+around('way["leisure"~"^(park|nature_reserve|golf_course)$"]')+around('way["natural"="water"]')+around('relation["natural"="water"]')+around('way["landuse"="cemetery"]')+');out geom;'
    for a in range(8):
        ep=EPS[a%2]
        try:
            d=json.loads(urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers={'User-Agent':'trip-map-script/1.0'}),timeout=200).read())
            for x in d['elements']: els[(x['type'],x['id'])]=x
            print(b,len(d['elements']),flush=True);break
        except Exception as ex: print(b,'retry',ex,flush=True);time.sleep(15)
    else: sys.exit('batch failed')
json.dump({'elements':list(els.values())},open('osm/local.json','w'));print('total',len(els))
