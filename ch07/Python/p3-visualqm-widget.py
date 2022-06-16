## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch07/p3-visualqm-widget.py
import numpy as np, matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def updatefig(dummy):      # called when paras are changed
    A, B, n = sliders[0].val, sliders[1].val, sliders[2].val
    psi = A*np.sin(n*np.pi*x) + B*np.cos(n*np.pi*x)
    plot.set_ydata(psi)
    ax.set_ylim(-1.2,1.2)
    ax.set_xlim(0, 1)
    fig.canvas.draw_idle()      # necessary?
    
x = np.linspace(0, 1, 100)       # x grids
vars = ['A', 'B', 'n']           # A sin(kx) + B cos(kx)
vals = [[0, 1, 0.5], [0, 1, 0.5], [0, 10, 5.2]]     # min, max, start

fig = plt.figure()
fig.canvas.set_window_title('Square well potential')
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.15, bottom=0.35, top=.95)
plot = ax.plot(x, 0*x, '-r', lw=2)[0]     # initiate plot
plt.axhline(0, ls='--')        # y=0 axes
plt.text(.2, .8, '$A\, \sin(n\pi x) + B\, \cos(n \pi x)$')
plt.xlabel('$x$ (arb.)'), plt.ylabel('$\psi$ (arb.)')

sliders = []                        # draw sliders at bottom
xw, yw, offset, dx, dy = .15, .20, .05, .5, .03     # widgets pos.
for i in range(len(vars)):
    axes = fig.add_axes([xw, yw-i*offset, dx, dy])
    sliders.append(Slider(axes, vars[i], vals[i][0], vals[i][1], vals[i][2]))
    sliders[i].on_changed(updatefig)

updatefig(0)
plt.show()
