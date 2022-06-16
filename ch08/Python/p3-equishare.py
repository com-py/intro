## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch08/p3-equishare.py
from numpy.random import random, randint
import matplotlib.pyplot as plt, numpy as np
import matplotlib.animation as am

def exchange(L=20):                     # iterate L times
    for _ in range(L):
        donor = randint(0, N)           # random pair
        getor = randint(0, N) 
        while solid[donor] == 0:        # find a nonzero donor
            donor = randint(0, N)
        solid[donor] -= 1               # exchange energy
        solid[getor] += 1
            
def updateimg(*args):                   # args[0] = frame
    L = 20 if args[0]<400 else 200      # slower init rate
    exchange(L)
    plot.set_data(np.reshape(solid, (K,K)))  # update image
    return [plot]                       # return line object in a list
    
K = 16                  # grid dimension
N = K*K                                 
solid = [10]*N          # 10 units of energy/cell
fig = plt.figure()
img = np.reshape(solid, (K,K))          # shape to KxK image
plot = plt.imshow(img, interpolation='none', vmin=0, vmax=50)
plt.colorbar(plot)
plt.axis('off')
anim = am.FuncAnimation(fig, updateimg, interval=1, blit=True)  # animate
plt.show()