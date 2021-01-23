#https://youtu.be/Ev5fbaX_W4o
from vpython import *
import math
N,NN,size=3,5,0.2
theta= 30*math.pi/180
g=vec(0,-9.8,0)
k,L=15000,2
m=1.0
scene= canvas(width=800,height=800,center=vector(0,-L/2,0),background=vec(0.5,0.5,0))
ceiling= box(length=3,width=1,height=0.02,color=color.blue)
strings=[]
balls=[]
for i in range(5):
    balls.append(sphere(radius=size,color=color.red))
    balls[i].v=vec(0,0,0)
    if i <N:
        balls[i].pos=vec((i-2)*2*size-L*math.sin(theta),-L*math.cos(theta),0)
    else:
        balls[i].pos=vec((i-2)*2*size,-L,0)
    strings.append(cylinder(radius=0.005,pos=vec((i-2)*2*size,0,0),color=color.white))
    strings[i].axis=balls[i].pos-strings[i].pos

def af_col_v(v1, v2, x1, x2): # function after collision velocity
    v1_prime = v1 + (x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + (x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)
def force(l):
    return -k*(mag(l)-L)*l.norm()
string_force=[]
for i in range(5): 
    string_force.append(vec(0,0,0)) 
dt=0.001
while True:
    rate(1000)
    for i in range(5):
        balls[i].v += (g+string_force[i]/m)*dt
        balls[i].pos += balls[i].v*dt
        strings[i].axis=balls[i].pos-strings[i].pos
        string_force[i]= force(strings[i].axis)
        if i ==0:
            if (mag(balls[1].pos - balls[0].pos) <= 2*size and dot(balls[0].pos-balls[1].pos, balls[0].v-balls[1].v) <= 0) :
                balls[0].v,balls[1].v= af_col_v(balls[0].v,balls[1].v,balls[0].pos,balls[1].pos)
        if i>=1 and i<=4:
            if (mag(balls[i].pos - balls[i-1].pos) <= 2*size and dot(balls[i-1].pos-balls[i].pos, balls[i-1].v-balls[i].v) <= 0) :
                balls[i-1].v,balls[i].v= af_col_v(balls[i-1].v,balls[i].v,balls[i-1].pos,balls[i].pos)