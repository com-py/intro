## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch04/p1-curvefit.py
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from numpy.random import random
import numpy as np

def lin(t, a, b):
    return a + b*t
    
def quad(t, a, b, c):
    return a + b*t + c*t*t

N = 101
t = np.linspace(0, 0.5, N)
x = 5*t - 4.9*t*t + 0.2*random(N)

cl = curve_fit(lin, t, x)[0]
cq = curve_fit(quad, t, x)[0]
print(cl, cq)

plt.plot(t, x, 'o')
plt.plot(t, lin(t, cl[0], cl[1]), 'k--')
plt.plot(t, quad(t, cq[0], cq[1], cq[2]), 'r-')
plt.xlabel('t (s)'), plt.ylabel('f (m)')
plt.show()