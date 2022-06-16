## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch05/p3-projectile.py
import matplotlib.pyplot as plt
import numpy as np
g = 9.8
a = np.array([0.0, -g])
r = np.array([0.0, 0.0])
v = np.array([4.0, 9.0])
dt = 0.1
t = 0.0
tlist = []
rlist = []
vlist = []
for i in range(20):
    tlist.append(t)
    rlist.append(r)
    vlist.append(v)    
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