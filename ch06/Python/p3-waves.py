## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch06/p3-waves.py
import matplotlib.pyplot as plt, numpy as np
import matplotlib.animation as am
from numba import jit

@jit                        # optimization
def waves(u0, u1):
    u2 = 2*(1-b)*u1 - u0                     # unshifted terms 
    for i in range(1, len(u0)-1):
        u2[i] += b*( u1[i-1] + u1[i+1] )     # left, right 
    return u2
    
def updatefig(*args):                   # args[0] = frame
    global u0, u1                       
    u2 = waves(u0, u1)
    u0, u1 = u1, u2 
    plot.set_data(x, u0)                # update data 
        
N, b = 100, 1.0             # number of points, beta^2
x = np.linspace(0., 1., N)
u0 = np.sin(np.pi*x)**2     # initial cond
u1 = 0.98*u0

fig = plt.figure()
plot = plt.plot(x, u0)[0]           # create plot object 
ani = am.FuncAnimation(fig, updatefig, interval=5)     # animate 
plt.axis('off')     # don't need axes
plt.ylim(-1.2,1.2)
plt.show()
