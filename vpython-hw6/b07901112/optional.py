from vpython import *
m,L,k=0.2,0.2,20
K,l=5,0.2
dt=0.001
size=0.02
b_1 = 0.05 * m * sqrt(k/m)
b_2 = 0.0025 * m * sqrt(k/m)

scene = canvas(width=600, height=400, range = 0.3, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue,pos=vec(0,0,0)) # left wall
wall_right = box(length=0.005, height=0.3, width=0.3, color=color.blue,pos=vec(L*3,0,0))

ball_1 = sphere(radius = size, color=color.red) 
ball_2 = sphere(radius = size, color=color.blue)

spring1 = helix(radius=0.015, thickness =0.01)
spring2 = helix(radius=0.015, thickness =0.01)
spring3 = helix(radius=0.015, thickness =0.01)

oscillation = graph(width = 400, align = 'left', xtitle='t',ytitle='x',background=vec(0.5,0.5,0))
x=gcurve(color=color.red,graph = oscillation)
oscillation2 = graph(width = 400, align = 'left',xtitle='t',ytitle='average_power',background=vec(0.5,0.5,0.5))
p=gdots(color=color.blue,graph=oscillation2)

ball_1.pos = vector(L, 0 , 0) # ball initial position
ball_2.pos = vector(L*2, 0 , 0)

ball_1.v = vector(0, 0, 0) # ball initial velocity
ball_2.v = vector(0, 0, 0)

ball_1.m , ball_2.m = m , m

spring1.pos , spring2.pos , spring3.pos = wall_left.pos , ball_1.pos , ball_2.pos

omega = sqrt((k+K)/m)
average_power=graph(width=400,align='left',xtitle='omega',ytitle='averaged power consumption',background=vec(0.7,0.7,0.7))
a=gcurve(color=color.white,graph=average_power)

work=0
t=0
n=1
T=2*pi/omega
while True:
    rate(1000)
    t+=dt
    force=0.1*sin(omega*t)*vec(1,0,0)
    spring1.axis , spring2.axis , spring3.axis = ball_1.pos-spring1.pos , ball_2.pos-ball_1.pos ,wall_right.pos-ball_2.pos
    spring2.pos=ball_1.pos
    spring3.pos = ball_2.pos
    spring1_force = -k*(mag(spring1.axis)-L)*norm(spring1.axis)
    spring2_force = -K*(mag(spring2.axis)-L)*norm(spring2.axis)
    spring3_force = -k*(mag(spring3.axis)-L)*norm(spring3.axis)
    ball_1.a , ball_2.a = (spring1_force - b_1*ball_1.v + force - spring2_force)/m , (spring2_force - b_2*ball_2.v - spring3_force) /m 
    ball_1.v , ball_2.v = ball_1.v+ball_1.a *dt, ball_2.v+ball_2.a *dt
    ball_1.pos , ball_2.pos = ball_1.pos+ball_1.v*dt , ball_2.pos+ball_2.v*dt
    x.plot(pos=(t,ball_1.pos.x - L))
    work+=dot(force,ball_1.v)*dt
    if t/T>n:
        p.plot(pos=(t,work/T))
        n+=1
        work=0


    



