# Albers equal-area conic for the contiguous US; map units = K per km, y grows downward.
import math
K=10.0
R=6371.0
_p1,_p2,_p0,_l0=map(math.radians,(29.5,45.5,37.5,-96.0))
_n=(math.sin(_p1)+math.sin(_p2))/2
_C=math.cos(_p1)**2+2*_n*math.sin(_p1)
_r0=R*math.sqrt(_C-2*_n*math.sin(_p0))/_n
def P(lat,lon):
    p,l=math.radians(lat),math.radians(lon)
    r=R*math.sqrt(_C-2*_n*math.sin(p))/_n
    t=_n*(l-_l0)
    return (round(r*math.sin(t)*K,1), round(-( _r0-r*math.cos(t))*K,1))
def gc(a,b,n=64):
    """great-circle points between (lat,lon) a and b"""
    la1,lo1,la2,lo2=map(math.radians,(*a,*b))
    d=2*math.asin(math.sqrt(math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2))
    out=[]
    for i in range(n+1):
        f=i/n;A=math.sin((1-f)*d)/math.sin(d);B=math.sin(f*d)/math.sin(d)
        x=A*math.cos(la1)*math.cos(lo1)+B*math.cos(la2)*math.cos(lo2)
        y=A*math.cos(la1)*math.sin(lo1)+B*math.cos(la2)*math.sin(lo2)
        z=A*math.sin(la1)+B*math.sin(la2)
        out.append((math.degrees(math.atan2(z,math.hypot(x,y))),math.degrees(math.atan2(y,x))))
    return out, d*R
