## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch03/p8-numba.py
import numpy as np, time
from numba import jit

@jit                        # optimization
def calc(u0, u1):
    u2 = - u0     
    for n in range(1, N-1):
        u2[n] += u1[n-1] + u1[n+1]      # left, right 
    return u2

N = 5000
u0 = np.random.random(N)
u1 = 0.9*u0
    
tc = time.perf_counter()
for i in range(2000):
    u2 = calc(u0, u1)
    u0, u1 = u1, u2 
    
tc = time.perf_counter() - tc
print(tc)
