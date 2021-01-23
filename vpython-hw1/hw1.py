#https://youtu.be/FcYNQSB5zws youtube影片連結
from vpython import *
g=9.8
size = 0.25 
scene=canvas(width=800,height=800,center=vec(0,7.5,0),background=vec(0.5,0.5,0.5))
floor = box(length=30, height=0.01, width=10, color=color.blue) 
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05) 

ball.pos = vec( -15, 5, 0) 
ball.v = vec(6, 8 , 0) 
dt = 0.001 
a1 = arrow(color = color.green, shaftwidth = 0.05)
b1 = arrow(color = color.blue, shaftwidth = 0.05)
c1 = arrow(color = color.yellow, shaftwidth=0.05)
a1.visible = False
b1.visible = False
time = 0
length = 0

while ball.pos.y >= size:
 rate(1000) 
 ball.pos = ball.pos + ball.v*dt
 ball.v.y = ball.v.y - g*dt
 ball.v.x = ball.v.x
 a1.pos = ball.pos
 a1.axis = vec(0, ball.v.y, 0)
 b1.pos = a1.pos + a1.axis
 b1.axis = vec(ball.v.x, 0, 0)
 c1.pos = a1.pos
 c1.axis = a1.axis + b1.axis
 time = time +dt
 length = length + ((ball.v.x*dt)**2 + (ball.v.y*dt - 0.5*9.8*(dt**2))**2)**0.5
msg =text(text = "Displacement:" + str(((ball.pos.x+15)**2 + (ball.pos.y-5)**2)**0.5) +","+str(vec(ball.pos.x+15 , ball.pos.y -5, 0)) , pos = vec(-10, 10, 0))
msg =text(text = "flying time:" + str(time) , pos = vec(-10, 12, 0))
msg =text(text = "The length of the entire path:" + str(length) , pos = vec(-10, 14, 0))
msg.visible = True


