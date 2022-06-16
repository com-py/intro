## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch05/p2-const-a.py
import matplotlib.pyplot as plt
a = 1.0
v = 2.0
x = 0.0
dt = 0.1
t = 0.0
tlist = []
xlist = []
vlist = []
for i in range(20):
    tlist.append(t)
    xlist.append(x)
    vlist.append(v)    
    x = x + v*dt
    v = v + a*dt
    t = t + dt
    
plt.plot(tlist, xlist)
plt.xlabel('time (s)')
plt.ylabel('x (m)')
plt.figure()
plt.plot(tlist, vlist)
plt.xlabel('time (s)')
plt.ylabel('v (m/s)')    
plt.show()