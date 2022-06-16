## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch08/p2-brownian.py
import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
import matplotlib.animation as am

def move():
    for i in range(N):
        fac = np.exp(-b*dt)
        r[i] += v[i]*(1-fac)/b
        v[i] = v[i]*fac
        phi = random()*2*np.pi              # apply kick
        v[i] += [dv*np.cos(phi), dv*np.sin(phi)]

def updatefig(*args):                       # update figure data
    move()
    plot.set_data(r[:,0], r[:,1])           # update positions
    return [plot]                           # return plot object

N = 500
r = np.zeros((N, 2))
v = np.zeros((N, 2))
b = 0.1
dt = 0.1
dv = 0.002      # impulse

fig = plt.figure()
plt.subplot(111, aspect='equal')
plot = plt.plot(r[:,0], r[:,1], '.')[0]     # create plot object
ani = am.FuncAnimation(fig, updatefig, interval=10, blit=True) # animate 
plt.xlim(-.75, .75)
plt.ylim(-.75, .75)
plt.show()
