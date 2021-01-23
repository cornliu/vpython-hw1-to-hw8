#https://youtu.be/eAjXLIkk_1M
from vpython import *
m,L,k=0.2,0.2,20
b = 0.05 * m * sqrt(k/m)

class obj:
    pass
wall_L,ball,spring=obj(),obj(),obj()

ball.pos = vector(L, 0 , 0) # ball initial position
ball.v = vector(0, 0, 0) # ball initial velocity
ball.m = m
spring.pos = vector(0, 0, 0)
omega = [0.1*i + 0.7*sqrt(k/m) for i in range(1, int(0.5*sqrt(k/m)/0.1))]

average_power=graph(width=400,align='left',xtitle='omega',ytitle='averaged power consumption',background=vec(0.7,0.7,0.7))
a=gcurve(color=color.white,graph=average_power)

def averagepower(omega_i):
    t, dt = 0, 0.001
    T=2*pi/omega_i
    times=1
    power=0
    power_t_before=0
    power_t_after=0
    while True:
        spring.axis = ball.pos - spring.pos # spring extended from spring endpoint A to ball
        spring_force = - k * (mag(spring.axis) - L) * norm(spring.axis) # spring force vector
        air_drag=-b*ball.v
        force=0.1*sin(omega_i*t)*vec(1,0,0)
        ball.a = (spring_force + air_drag + force) / ball.m # ball acceleration = spring force /m - damping
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
        power=dot(force,ball.v)
        power_t_after+=power
        if t/T > times:
            times+=1
            if abs(power_t_after-power_t_before)<0.00001:
                return power_t_after/T
            power_t_before=power_t_after
            power_t_after=0
saved=dict()
for i in omega:
    a.plot (pos=(i,averagepower(i)))
    saved[averagepower(i)]=i
max_saved=max(saved)
peak=saved[max_saved]
print(peak)





