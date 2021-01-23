#https://youtu.be/83Rvy-_4e1A
#我算出來的三次週期:
#18.184931506849313 years
#18.384246575342466 years
#18.373972602739727 years
from vpython import *
G = 6.67E-11
theta = 5.145*pi/180
scene = canvas(width=800,height=800,background=vec(0.5,0.5,0))
mass = {'sun':1.99E30,'earth':5.972E24,'moon':7.36E22}
radius = {'earth':6.371E6*10,'moon':1.317E6*10,'sun':6.95E8*10}
earth_orbit = {'r':1.495E11,'v':2.9783E4}
moon_orbit = {'r':3.84E8,'v':1.022E3}                              
scene.lights = []
def G_f(star1,star2):
    F = -G*star1.m*star2.m/(mag(star1.pos - star2.pos)**2)*norm(star1.pos - star2.pos)
    return F                                            
ce = moon_orbit['r']*(mass['moon']/(mass['moon']+mass['earth']))
cm = moon_orbit['r']*(mass['earth']/(mass['moon']+mass['earth'])) 
sun = sphere(pos=vec(0,0,0),radius=radius['sun'],m=mass['sun'],color=color.orange,emissive=True)
local_light(pos=vec(0,0,0))
earth = sphere(pos=vec(earth_orbit['r']-ce*cos(theta),-ce*sin(theta),0),radius=radius['earth'],m=mass['earth'],texture={'file':textures.earth})
moon = sphere(pos=vec(earth_orbit['r']+cm*cos(theta),cm*sin(theta),0),radius=radius['moon'],m=mass['moon'],texture={'file':textures.rough})
earth.v = vec(0,0,-earth_orbit['v'])
moon.v = vec(0,0,-(moon_orbit['v']*(mass['moon']+mass['earth'])/mass['earth'] + earth_orbit['v']))
a = arrow(color = color.white, shaftwidth = radius['earth']/3)
dt = 21600
t = 0
point = 0 #記數用
kiki = 0
ttt = 0
while True:
    rate(1000)
    t = t + dt    
    back = 5*radius['earth']*norm(cross(moon.pos-earth.pos,moon.v-earth.v)).x
    moon.a = (G_f(moon,sun)+G_f(moon,earth))/mass['moon']
    moon.v = moon.v + moon.a * dt
    earth.a = (G_f(earth,sun)+G_f(earth,moon))/mass['earth']
    earth.v = earth.v + earth.a * dt
    moon.pos = moon.pos + moon.v * dt
    earth.pos = earth.pos + earth.v * dt                                       
    a.axis = 5*radius['earth']*norm(cross(moon.pos-earth.pos,moon.v-earth.v))
    a.pos = earth.pos
    scene.center = earth.pos
    forth = a.axis.x
    ttt = forth - back
    if ttt > 0 and forth * back < 0 and point == 1:        
        print((t - kiki)/(86400*365) , 'years')
        kiki = t
    if ttt > 0 and forth * back < 0 and point == 0:        
        kiki = t
        point = 1
