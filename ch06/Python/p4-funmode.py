## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch06/p4-funmode.py
from scipy.linalg import eigh       # eigenvalue solver
import numpy as np, matplotlib.pyplot as plt

N = 101         # number of grids
x = np.linspace(0., 1., N)   # grids

A = np.diag([2.]*(N-2))                                 # diagonal
A += np.diag([-1.]*(N-3),1) + np.diag([-1.]*(N-3),-1)   # off diags
A = A/(x[1]-x[0])**2        # delta x = x_1 - x_0

lamb, X = eigh(A)           # solve for eigenvals and eigenvecs

sty = ['-','--','-.',':']
print (np.sqrt(lamb[:len(sty)])/np.pi)             # wave vector k/pi

for i in range(len(sty)):   # plot a few standing waves
    Xi = np.insert(X[:,i], [0, N-2], [0., 0.])  # insert end points
    plt.plot(x, Xi, sty[i], label=repr(i+1))
    
plt.xlabel('$x$'), plt.ylabel('$X$')
plt.legend(loc='lower right'), plt.show()
