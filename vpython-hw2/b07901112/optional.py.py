#https://youtu.be/496Xd8CnNnI
from vpython import *
g=9.8
size=0.25
C_drag=0.3
scene = canvas(center=vec(0,5,0),width=600,background=vec(0.5,0.5,0))
ball=sphere(radius=size,color=color.red,make_trail=True,trail_radius=size/3)
ball.pos = vec(0,15,0)
ball.v = vec(0,0,0)
dt=0.001
m=1
t=0
velocity = graph(width=450,calign='right')
function = gcurve(graph=velocity, color=color.blue, width=4)
while m>=0.01:
    rate(1000)
    ball.v.y += -g*dt - C_drag*ball.v.y*dt
    ball.pos += ball.v*dt
    function.plot(pos=(t,ball.v.mag))
    t=t+dt
    m=(ball.v.y-g*dt - C_drag*ball.v.y*dt-ball.v.y)/(-dt)
print('the terminal velocity is'+str(ball.v.y))