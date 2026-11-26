# Build projected vector basemap layers -> geo.json
import json, math
from shapely.geometry import LineString, Polygon, box, MultiPolygon, shape
from shapely.ops import unary_union, polygonize, transform, linemerge
from proj import P

def topo_geoms(path, obj):
    t=json.load(open(path)); sc,tr=t['transform']['scale'],t['transform']['translate']
    arcs=[]
    for a in t['arcs']:
        x=y=0;pts=[]
        for dx,dy in a: x+=dx;y+=dy;pts.append((x*sc[0]+tr[0],y*sc[1]+tr[1]))
        arcs.append(pts)
    def ring(r): return [p for i in r for p in (arcs[i] if i>=0 else arcs[~i][::-1])]
    out=[]
    for g in t['objects'][obj]['geometries']:
        polys=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]
        for poly in polys:
            rs=[ring(r) for r in poly]
            out.append((rs[0],rs[1:],g.get('properties',{})))
    return out
def proj_poly(outer,holes,ok=lambda lo,la:True):
    if not any(ok(lo,la) for lo,la in outer): return None
    pg=Polygon([P(la,lo) for lo,la in outer],[[P(la,lo) for lo,la in h] for h in holes]).buffer(0)
    return pg

NA=lambda lo,la: -135<=lo<=-55 and 14<=la<=60
# coarse land: Natural Earth 10m land around North America
coarse=[]
for o,h,_ in topo_geoms('osm/land-10m.json','land'):
    pg=proj_poly(o,h,NA)
    if pg is not None: coarse.append(pg)
clipbox=box(*P(60,-135)[:1],-1,1,1)  # placeholder
coarse=unary_union(coarse)
x0,y0=P(52,-128)[0],P(53,-75)[1]
x1,y1=P(22,-66)[0],P(22,-100)[1]
frame=box(min(x0,-27000),min(y0,-17000),max(x1,26000),max(y1,9000))
coarse=coarse.intersection(frame).simplify(8)
# states outline
states=[]
for o,h,pr in topo_geoms('osm/states-10m.json','states'):
    pg=proj_poly(o,h)
    if pg is not None: states.append(pg.simplify(6))

def osm(name): return json.load(open(f'osm/{name}.json'))['elements']
def line(e): return LineString([P(g['lat'],g['lon']) for g in e['geometry']])
def fine_land(name,S,W,N,E):
    raw=osm(name); bb=Polygon([P(S,W),P(S,E),P(N,E),P(N,W)])
    coast=[line(e) for e in raw if e['type']=='way' and e.get('tags',{}).get('natural')=='coastline']
    faces=list(polygonize(unary_union(coast+[bb.exterior])))
    def is_land(face):
        pt=face.representative_point();best=None
        for ln in coast:
            if ln.distance(pt)>(best[0] if best else 1e18): continue
            cs=list(ln.coords)
            for a,b in zip(cs,cs[1:]):
                dd=LineString([a,b]).distance(pt)
                if best is None or dd<best[0]: best=(dd,a,b)
        _,a,b=best
        return (b[0]-a[0])*(pt.y-a[1])-(b[1]-a[1])*(pt.x-a[0])<0
    land=unary_union([f for f in faces if f.within(bb.buffer(1)) and is_land(f)])
    return bb,land.simplify(0.4)
REG={'boston':(42.22,-71.30,42.72,-70.58),'nyc':(40.50,-74.35,41.00,-73.70),'albany':(42.55,-74.00,42.85,-73.60)}
land=coarse
for nm in ('boston','nyc'):
    bb,fl=fine_land(nm,*REG[nm])
    land=land.difference(bb).union(fl)
    print(nm,'fine land',fl.area)

water=[];rivers=[];roads=[];runway=[]
for nm in REG:
    for e in osm(nm):
        t=e.get('tags',{})
        if t.get('natural')=='water':
            try:
                if e['type']=='way' and len(e['geometry'])>3:
                    pg=Polygon([P(g['lat'],g['lon']) for g in e['geometry']]).buffer(0)
                    if pg.area>15: water.append(pg)
                elif e['type']=='relation':
                    outs=[line({'geometry':m['geometry']}) for m in e.get('members',[]) if m.get('role')=='outer' and m.get('geometry')]
                    inn=[line({'geometry':m['geometry']}) for m in e.get('members',[]) if m.get('role')=='inner' and m.get('geometry')]
                    po=unary_union(list(polygonize(unary_union(outs))))
                    if inn: po=po.difference(unary_union(list(polygonize(unary_union(inn)))))
                    if po.area>15: water.append(po)
            except Exception as ex: pass
        elif t.get('waterway')=='river': rivers.append(line(e).simplify(0.6))
        elif t.get('highway')=='motorway' or t.get('highway')=='trunk': roads.append(line(e).simplify(0.8))
        elif t.get('aeroway')=='runway': runway.append(line(e))

# street-level context around stops
parks=[];minor=[]
import os
if os.path.exists('osm/local.json') and os.path.getsize('osm/local.json')>0:
    for e in osm('local'):
        t=e.get('tags',{})
        try:
            if t.get('highway'): minor.append(line(e).simplify(0.3))
            elif t.get('leisure') or t.get('landuse')=='cemetery':
                if len(e['geometry'])>3:
                    pg=Polygon([P(g['lat'],g['lon']) for g in e['geometry']]).buffer(0)
                    if pg.area>0.5: parks.append(pg)
            elif t.get('natural')=='water':
                if e['type']=='way' and len(e['geometry'])>3:
                    pg=Polygon([P(g['lat'],g['lon']) for g in e['geometry']]).buffer(0)
                    if pg.area>0.3: water.append(pg)
                elif e['type']=='relation':
                    outs=[line({'geometry':m['geometry']}) for m in e.get('members',[]) if m.get('role')=='outer' and m.get('geometry')]
                    po=unary_union(list(polygonize(unary_union(outs))))
                    if po.area>0.3: water.append(po)
        except Exception: pass
water=unary_union(water).simplify(0.3)
from shapely.geometry import Point
_C=json.load(open('coords.json'));_skip={'bronx910','cam97','mn'}
_pts=[v for k,v in _C.items() if k not in _skip]+[(40.6895,-74.1745),(40.6437,-74.0735),(40.6892,-74.0445),(42.7179,-73.8335),(42.3670,-71.1056),(40.8448,-73.8648)]
zone=unary_union([Point(*P(la,lo)).buffer(30) for la,lo in _pts])
parks=unary_union(parks).intersection(zone).simplify(0.3) if parks else Polygon()
minor=linemerge(unary_union(minor)).intersection(zone) if minor else None

def d_poly(g,nd=1):
    gs=[g] if g.geom_type=='Polygon' else list(getattr(g,'geoms',[]))
    out=[]
    for pg in gs:
        if pg.is_empty or pg.geom_type!='Polygon': continue
        for r in [pg.exterior,*pg.interiors]:
            cs=list(r.coords)
            out.append('M'+'L'.join(f'{x:.{nd}f},{y:.{nd}f}'.replace('.0,',',').rstrip('0').rstrip('.') if False else f'{round(x,nd):g},{round(y,nd):g}' for x,y in cs)+'Z')
    return ''.join(out)
def d_lines(ls,nd=1):
    out=[]
    for l in ls:
        gs=[l] if l.geom_type=='LineString' else list(getattr(l,'geoms',[]))
        for g in gs:
            cs=list(g.coords)
            if len(cs)>1: out.append('M'+'L'.join(f'{round(x,nd):g},{round(y,nd):g}' for x,y in cs))
    return ''.join(out)
roads=linemerge(unary_union(roads)) if roads else []
rivers=linemerge(unary_union(rivers))
geo={'frame':[round(v) for v in frame.bounds],
     'land':d_poly(land),'states':''.join(d_poly(s,0).replace('Z','') for s in states),
     'water':d_poly(water),'rivers':d_lines([rivers]),'roads':d_lines([roads]),'runway':d_lines(runway),'parks':d_poly(parks),'minor':d_lines([minor]) if minor is not None else ''}
json.dump(geo,open('geo.json','w'),separators=(',',':'))
for k,v in geo.items(): print(k,len(v) if isinstance(v,str) else v)
