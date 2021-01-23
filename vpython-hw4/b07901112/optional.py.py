#https://youtu.be/q-jClx66kvk
from vpython import *
import math
g = 9.8
size, m = 0.1, 0.5
L, k = 2, 15000
theta=30*math.pi/180
omega= math.pi/(12*60*60) 

scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), background=vec(0.5, 0.5, 0))
ceiling = box(length=1.2, height=0.01, width=1.2, color=color.blue)
ball = sphere(radius=size, color=color.red, make_trail=True,trail_type="points",interval=20,retain=80)
spring = cylinder(radius=0.01)   # default pos = vec(0, 0, 0)
ball.v = vec(0, 0, 0)
ball.pos =vec(-L-m*g/k-(-L - m*g/k)*sin(pi/6),-(L+m*g/k)*cos(pi/6),0)
pos=vec(-L-m*g/k-(-L - m*g/k)*sin(pi/6),-(L+m*g/k)*cos(pi/6),0)


dt = 0.001
t = 0
a=0
while True:
    rate(100000)
    t += dt
    spring.axis = ball.pos - spring.pos                              # spring extended from endpoint to ball
    spring_force = - k * (mag(spring.axis) - L) * spring.axis.norm() # to get spring force vector
    ball.a = vector(0, - g, 0) + spring_force / m + 2*omega*vec(ball.v.z*math.sin(25*math.pi/180)-ball.v.y*math.cos(25*math.pi/180),-ball.v.x*math.sin(25*math.pi/180),ball.v.x*math.cos(25*math.pi/180))
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    if (pos.y-ball.pos.y<0) and (pos.y-ball.pos.y+ball.v.y*dt)>0 : 
        a+=1
    if a>=2000:
        print(atan((ball.pos.z)/(ball.pos.x)),'rad')
        break
