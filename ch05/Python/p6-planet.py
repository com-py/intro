## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch05/p6-planet.py
import matplotlib.pyplot as plt
import numpy as np
GM = 4*np.pi**2
r = np.array([1.0, 0.0])
v = np.array([0.0, 2*np.pi])
dt = 0.01
t = 0.0
rlist = []
while t< 5.0:
    rlist.append(r)
    r = r + v*dt
    rmag = np.sqrt(r[0]**2 + r[1]**2)
    a = - GM * r/rmag**3
    v = v + a*dt
    t = t + dt

rlist = np.array(rlist)

ax = plt.subplot(111, aspect='equal')   # equal aspect ratio
ax.plot(rlist[:,0], rlist[:,1])
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')    
plt.show()