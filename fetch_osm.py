# Download basemap layers for the three trip regions from OpenStreetMap (only bounding boxes are sent).
import urllib.request,urllib.parse,json,collections,time,sys
R={'albany':'42.55,-74.00,42.85,-73.60','boston':'42.22,-71.30,42.72,-70.58','nyc':'40.50,-74.35,41.00,-73.70'}
for name,B in R.items():
    if len(sys.argv)>1 and name not in sys.argv[1:]: continue
    q=f'''[out:json][timeout:300];
(
 way["natural"="coastline"]({B});
 way["natural"="water"]["name"]({B});
 relation["natural"="water"]["name"]({B});
 way["waterway"="river"]["name"]({B});
 way["highway"~"^(motorway|trunk)$"]({B});
 way["aeroway"="runway"]({B});
);
out geom;'''
    for attempt in range(3):
        try:
            r=urllib.request.urlopen(urllib.request.Request('https://overpass.kumi.systems/api/interpreter',data=urllib.parse.urlencode({'data':q}).encode(),headers={'User-Agent':'trip-map-script/1.0'}),timeout=360)
            open(f'osm/{name}.json','wb').write(r.read());break
        except Exception as e: print(name,'retry',e); time.sleep(20)
    d=json.load(open(f'osm/{name}.json'));c=collections.Counter()
    for e in d['elements']:
        t=e.get('tags',{});c[(e['type'],t.get('natural') or t.get('waterway') or t.get('highway') or t.get('aeroway'))]+=1
    print(name,dict(c))
