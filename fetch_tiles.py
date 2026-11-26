# NYC basemap in small tiles (the full box times out); merged into osm/nyc.json
import urllib.request,urllib.parse,json,time,sys
EPS=['https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter']
S,W,N,E=40.50,-74.35,41.00,-73.70
tiles=[(S+i*(N-S)/3,W+j*(E-W)/3,S+(i+1)*(N-S)/3,W+(j+1)*(E-W)/3) for i in range(3) for j in range(3)]
els={}
for k,(s,w,n,e) in enumerate(tiles):
    B=f'{s},{w},{n},{e}'
    q=f'[out:json][timeout:120];(way["natural"="coastline"]({B});way["natural"="water"]["name"]({B});relation["natural"="water"]["name"]({B});way["waterway"="river"]["name"]({B});way["highway"="motorway"]({B});way["aeroway"="runway"]({B}););out geom;'
    for a in range(6):
        ep=EPS[a%2]
        try:
            r=urllib.request.urlopen(urllib.request.Request(ep,data=urllib.parse.urlencode({'data':q}).encode(),headers={'User-Agent':'trip-map-script/1.0'}),timeout=150).read()
            d=json.loads(r);[els.__setitem__((x['type'],x['id']),x) for x in d['elements']];print(k,len(d['elements']),flush=True);break
        except Exception as ex: print(k,'retry',ep[8:20],ex,flush=True);time.sleep(10)
    else: sys.exit('tile failed')
json.dump({'elements':list(els.values())},open('osm/nyc.json','w'))
print('nyc total',len(els))
