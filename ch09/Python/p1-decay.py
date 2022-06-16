## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch08/p1-decay.py
from numpy.random import random
import matplotlib.pyplot as plt

p = 0.05
N = 1000
Nlist = []

while N>10:
    Nlist.append(N)
    dN = 0
    for _ in range(N):
        if random() < p:
            dN = dN - 1
    N = N + dN

plt.plot(range(len(Nlist)), Nlist, '.')
plt.xlabel('time (arb.)')
plt.ylabel('$N$')
plt.show()
