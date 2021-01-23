import numpy as np
from vpython import *
A, N ,m, k, d = 0.10, 50, 0.1, 10.0, 0.4
Unit_K= 2*pi/(N*d)
ang_fre=graph(width = 400, align = 'left', xtitle='wavevector',ytitle='angular frequency',background=vec(0.5,0.5,0.5))
ttt = gcurve(color=color.blue,graph = ang_fre)
finish = int((N/2)//1)
for i in range(1,finish):
    wavevec = i*Unit_K
    theta = wavevec*arange(N)*d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(theta), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    number = 0
    t = 0
    dt = 0.0002
    while True:
        rate(10000)
        t+=dt
        spring_len[-1] = (50*0.4+ball_pos[0] - ball_pos[-1]) 
        spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
        before = ball_v[-1]
        ball_v[0] += (spring_len[0] - d)*k/m*dt -(spring_len[-1] - d)*k/m*dt
        ball_v[1:] +=  (spring_len[1:] - d)*k/m*dt - (spring_len[:-1] - d)*k/m*dt 
        ball_pos += ball_v*dt
        if ball_v[-1] > 0 and before < 0:
            if number == 1:
                T=t
                omega = 2*pi/T
                break
            number += 1
            t = 0
    ttt.plot(pos=(wavevec , omega))

