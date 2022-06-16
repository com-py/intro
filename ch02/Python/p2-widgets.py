## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch03/p2-widgets.py
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, CheckButtons
import numpy as np

x = np.linspace(-1, 1, 101)     # grid

def updatefig(*args):           # update figure data
    k = slider.val
    if func.value_selected == fs[0]:           # sin
        f = np.sin(k*np.pi*x)
    else:
        f = np.cos(k*np.pi*x)
    if refresh.get_status()[0]:     # checkbox 0 val
        plot.set_ydata(f)
        ax.set_ylim(min(f), max(f))
    fig.canvas.draw_idle()
    
fig = plt.figure()
fig.canvas.set_window_title('Interactive plotting')
fig.subplots_adjust(left=0.15, bottom=0.35, top=.95)
ax = fig.add_subplot(111)
plot = ax.plot(x, [0]*len(x))[0]

axes = fig.add_axes([.15, .20, .75, .03])       # k slider
slider = Slider(axes, '$k$', 0, 2, 1)           # range, init val
slider.on_changed(updatefig)

fs  = ['sin', 'cos']         # radio buttons    
rbox =fig.add_axes([.15, .02, .15, .15])
func = RadioButtons(rbox, fs, 0)    # active = sin (0)

cbox = fig.add_axes([.4, .02, .15, .15])        # checkbox, real+extra
refresh = CheckButtons(cbox, ['refresh', 'extra'], [1,0])
func.on_clicked(updatefig)  
refresh.on_clicked(updatefig)  

updatefig(None)
plt.show()
