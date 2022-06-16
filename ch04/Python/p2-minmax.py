## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch04/p2-minmax.py
import numpy as np
import matplotlib.pyplot as plt

def minmax(y):      # return indices of minima and maxima
    mini = (y[1:-1]<=y[:-2])*(y[1:-1]<=y[2:])   # minima array
    maxi = (y[1:-1]>=y[:-2])*(y[1:-1]>=y[2:])   # maxima array
    mini = 1 + np.where(mini)[0]                # indices of minima
    maxi = 1 + np.where(maxi)[0]                # indices of maxima
    return mini, maxi

x = np.linspace(0, 5, 100)
y = np.exp(-x/2)*np.sin(2*np.pi*x)
mini, maxi = minmax(y)

plt.plot(x, y, '-o', mfc='none')                # open circle marker
plt.plot(x[mini], y[mini], 'kv', label='minima')
plt.plot(x[maxi], y[maxi], 'r^', label='maxima')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
