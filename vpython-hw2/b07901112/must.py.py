#https://youtu.be/AdCCz1SpIvY
from vpython import *
g = 9.8
size = 0.25
C_drag = 0.9
scene = canvas(center=vec(0,5,0), width=600, background=vec(0.5,0.5,0))
floor = box(length=30, height=0.01, width=4, color=color.blue)
ball = sphere(radius=size, color=color.red, make_trail=True, trail_radius=size/3)
ball.pos = vec(-15,0.25,0)
ball.v = vec(10*2**0.5,10*2**0.5,0)
dt = 0.001
s=0
height=0
t=0
velocity = graph(width=450)#,center=vec(20,10,0)) #align='right'
function = gcurve(graph=velocity, color=color.blue, width=4)
while ball.pos.x<=50:
    rate(1000)
    ball.v += vec(0, -g, 0)*dt - C_drag*ball.v*dt
    ball.pos += ball.v*dt
    function.plot(pos=(t,ball.v.mag))
    t+=dt
    if ball.pos.y >= height:
        height = ball.pos.y
    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y = -ball.v.y
        s = s + 1
    if s>=3:
        msg =text(text ='displacement:' + str(((ball.pos.x+15)**2 + (ball.pos.y-0.25)**2)**0.5),pos =vec(-5,10,0))
        msg =text(text = 'height of the hightest point:'+str(height),pos =vec(-5,12,0))
        msg.visible = True
        break
