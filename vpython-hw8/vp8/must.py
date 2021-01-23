from vpython import *
from diatomic import *
N = 20 
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50  
m = 14E-3/6E23  
k, T = 1.38E-23, 298.0    
initial_v = (3*k*T/m)**0.5   

scene = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1))
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow,pos=vec(0,0,0) )  

energies = graph(width = 600, align = 'left', ymin=0)  
c_avg_com_K = gcurve(color = color.green)
c_avg_v_P = gcurve(color = color.red)
c_avg_v_K = gcurve(color = color.purple)
c_avg_r_K = gcurve(color = color.blue) 

COs=[]   
for i in range(N): 
    O_pos = vec(random()-0.5, random()-0.5, random()-0.5)*L   
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0)) 
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random())
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random())
    COs.append(CO)
times = 0   
t,dt =0, 5E-16
tot_com_K,tot_v_K,tot_v_P,tot_r_K=0,0,0,0

while True:
    rate(3000)
    t+=dt
    for CO in COs:
        CO.time_lapse(dt)
    for i in range(N-1):
        for j in range(i+1,N):
            if mag(COs[i].C.pos-COs[j].C.pos) <= 2*size and dot(COs[i].C.pos-COs[j].C.pos,COs[i].C.v-COs[j].C.v) <= 0: COs[i].C.v,COs[j].C.v = collision(COs[i].C, COs[j].C)
            if mag(COs[i].C.pos-COs[j].O.pos) <= 2*size and dot(COs[i].C.pos-COs[j].O.pos,COs[i].C.v-COs[j].O.v) <= 0: COs[i].C.v,COs[j].O.v = collision(COs[i].C, COs[j].O)
            if mag(COs[i].O.pos-COs[j].C.pos) <= 2*size and dot(COs[i].O.pos-COs[j].C.pos,COs[i].O.v-COs[j].C.v) <= 0: COs[i].O.v,COs[j].C.v = collision(COs[i].O, COs[j].C)
            if mag(COs[i].O.pos-COs[j].O.pos) <= 2*size and dot(COs[i].O.pos-COs[j].O.pos,COs[i].O.v-COs[j].O.v) <= 0: COs[i].O.v,COs[j].O.v = collision(COs[i].O, COs[j].O)
    for CO in COs:
        if abs(CO.C.pos.x)>(L-size): CO.C.v.x *=-1  
        if abs(CO.C.pos.y)>(L-size): CO.C.v.y *=-1            
        if abs(CO.C.pos.z)>(L-size): CO.C.v.z *=-1             
        if abs(CO.O.pos.x)>(L-size): CO.O.v.x *=-1            
        if abs(CO.O.pos.y)>(L-size): CO.O.v.y *=-1            
        if abs(CO.O.pos.z)>(L-size): CO.O.v.z *=-1            
        tot_com_K += CO.com_K()
        tot_v_K += CO.v_K()
        tot_v_P += CO.v_P()
        tot_r_K += CO.r_K()
    times+=1
    c_avg_com_K.plot(times,(tot_com_K/times))
    c_avg_v_P.plot(times,(tot_v_P/times))
    c_avg_v_K.plot(times,(tot_v_K/times))
    c_avg_r_K.plot(times,(tot_r_K/times))
     
