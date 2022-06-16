## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch05/p1-const-v.py
import matplotlib.pyplot as plt
x0 = 0.0
v = 2.0
dt = 0.1
t = 0.0
tlist = []
xlist = []
for i in range(10):
    tlist.append(t)
    xlist.append(x0)
    x0 = x0 + v*dt
    t = t + dt
    
plt.plot(tlist, xlist)
plt.xlabel('time (s)')
plt.ylabel('x (m)')
plt.show()
