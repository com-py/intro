## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch05/p5-sho-vp.py
import matplotlib.pyplot as plt
import numpy as np
import vpython as vp

omega = 1.0
r = np.array([1.0, 1.5])
v = np.array([1.0, 0.0])
dt = 0.1
tlist = []
rlist = []

t = 0.0
vp.canvas(background=vp.color.blue)
ball = vp.sphere(radius=0.1, make_trail=True)
while t< 10.0:
    vp.rate(10)
    ball.pos=vp.vector(r[0],r[1],0)
    tlist.append(t)
    rlist.append(r)
    r = r + v*dt
    a = - omega**2 * r
    v = v + a*dt
    t = t + dt
    
rlist = np.array(rlist)
plt.plot(tlist, rlist[:,0], tlist, rlist[:,1])
plt.xlabel('time (s)')
plt.ylabel('x, y (m)')
plt.figure()
plt.plot(rlist[:,0], rlist[:,1])
plt.xlabel('x (m)')
plt.ylabel('y (m)')    
plt.show()