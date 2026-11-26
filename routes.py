# Driving geometry between public stops via the public OSRM demo server (only these coordinates are sent).
import json,urllib.request,time,os
C=json.load(open('coords.json'))
A={  # city-level anchors (no lodging coordinates are sent or drawn)
 'colonie':(42.7179,-73.8335),'bronx':(40.8448,-73.8648),'cambridge':(42.3670,-71.1056),'alb_airport':(42.7483,-73.8017),
 'ewr':(40.6895,-74.1745),'lincoln_nj':(40.7660,-74.0300)}
def pt(k): return tuple(C[k]) if k in C else A[k]
ROUTES={
 'd1':['alb_airport','lunch823','crossings'],
 'd2':['colonie','hmart','bronx'],
 'd3':['bronx','gwb'],
 'd4a':['gwb2','cranford'],'d4b':['cranford','lincoln','dewitt'],
 'd8':['bronx','colonie'],
 'd9':['colonie','mcphs','cambridge'],
 'd10':['cambridge','halibut','glou','stagefort','cambridge'],
 'd13':['cambridge','malden'],
 'd16':['cambridge','latham99','esp'],
 'd17':['colonie','bronx','ewr'],
}
os.makedirs('routes',exist_ok=True)
out={}
for k,seq in ROUTES.items():
    f=f'routes/{k}.json'
    if not os.path.exists(f):
        cs=';'.join(f'{pt(s)[1]},{pt(s)[0]}' for s in seq)
        u=f'https://router.project-osrm.org/route/v1/driving/{cs}?overview=full&geometries=geojson'
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'trip-map-script/1.0'}),timeout=60).read()
        open(f,'wb').write(r); time.sleep(1.2)
    d=json.load(open(f))
    rt=d['routes'][0]
    out[k]={'wp':[pt(s) for s in seq],'coords':[(la,lo) for lo,la in rt['geometry']['coordinates']],'km':round(rt['distance']/1000,1),'legs':[round(l['distance']/1000,1) for l in rt['legs']]}
    print(k,out[k]['km'],out[k]['legs'],len(out[k]['coords']))
json.dump({'anchors':A,'routes':out},open('routes.json','w'))
