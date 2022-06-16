## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch06/p2-threebody-osc-vp.py
import matplotlib.pyplot as plt
import numpy as np
import vpython as vp

k1, k2 = 1.0, 1.0
m1, m2, m3 = 1.0, 3.0, 1.0
u = np.array([1.0, 0.0, 0.5])
v = np.array([0.0, 0.0, 0.0])

t, dt = 0.0, 0.1
tlist, ulist = [], []
vp.canvas(background=vp.color.blue)
x0 = np.array([-3, 0, 3])         # initial positions
ball0 = vp.sphere(pos=vp.vector(x0[0],0,0), radius=0.5, color=vp.color.red)
ball1 = vp.sphere(pos=vp.vector(x0[1],0,0), radius=0.5, color=vp.color.green)
ball2 = vp.sphere(pos=vp.vector(x0[2],0,0), radius=0.5, color=vp.color.white)
while t< 20.0:
    tlist.append(t)
    ulist.append(u)
    
    vp.rate(20)
    ball0.pos.x = x0[0] + u[0]
    ball1.pos.x = x0[1] + u[1]
    ball2.pos.x = x0[2] + u[2]
    
    u = u + 0.5*v*dt          # leapfrog
    f12 = -k1*(u[0]-u[1])
    f23 = -k2*(u[1]-u[2])
    a = np.array([f12/m1, -f12/m2 + f23/m2, -f23/m3])
    v = v + a*dt
    u = u + 0.5*v*dt
    t = t + dt

ulist = np.array(ulist)
plt.plot(tlist, ulist[:,0], tlist, ulist[:,1], '-.', tlist, ulist[:,2], '--')
plt.xlabel('time (s)')
plt.ylabel('$u_{1,2,3}$ (m)')
plt.show()