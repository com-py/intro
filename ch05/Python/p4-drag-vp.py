## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch05/p4-drag-vp.py
import matplotlib.pyplot as plt
import numpy as np
import vpython as vp

c1 = 0.0
c2 = 0.2
g = 9.8
ag = np.array([0.0, -g])
r = np.array([0.0, 0.0])
v = np.array([4.0, 9.0])
dt = 0.02
t = 0.0
tlist = []
rlist = []
vlist = []

vp.canvas(background=vp.color.blue)
ball = vp.sphere(radius=0.1, make_trail=True)
while r[1] >= 0.0:      # y-position above 0
    vp.rate(10)
    ball.pos=vp.vector(r[0], r[1], 0)
    tlist.append(t)
    rlist.append(r)
    vlist.append(v)
    speed = np.sqrt(v[0]**2 + v[1]**2)
    a = ag - c1*v - c2*speed*v
    r = r + v*dt
    v = v + a*dt
    t = t + dt
    
rlist = np.array(rlist)
vlist = np.array(vlist)

plt.plot(tlist, rlist[:,0], tlist, rlist[:,1])
plt.xlabel('time (s)')
plt.ylabel('x, y (m)')
plt.figure()
plt.plot(tlist, vlist[:,0], tlist, vlist[:,1])
plt.xlabel('time (s)')
plt.ylabel('vx, vy (m/s)')    
plt.show()