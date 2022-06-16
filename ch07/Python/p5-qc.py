## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch07/p5-qc.py
import numpy as np
from numpy.random import random

def Qubit():        # returns spin up [1,0]
    return np.array([1, 0])
    
def H(qubit):       # Hadamard gate
    hg = np.array([[1,1], [1,-1]])/np.sqrt(2.0)
    return np.dot(hg, qubit)
    
def M(qubit):       # Measurement
    return np.dot([1, 0], qubit)

s = 0.0     # spin count
N = 1000    # samplings
for i in range(N):    
    q = Qubit()
    hq = H(q)
    c1 = M(hq)      # amplitude
    r = random()
    if (r < c1**2): # spin up
        s = s + 1.0
        
print('Probability of spin up:', s/N)

