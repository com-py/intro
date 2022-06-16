## Introduction to computation in physical sciences
## J Wang and A Wang, https://github.com/com-py/intro
## ch03/p4-vpython.py
import vpython as vp

scene = vp.canvas(title=('right drag to change camera,' +
                         'double drag to zoom'))
ball = vp.sphere()
box = vp.box(pos=vp.vector(0,0,-1.1), length=10, height=5, width=.2, 
                 color=vp.color.cyan)

t = 0
while t<10:
    vp.rate(10)
    ball.pos = vp.vector(2*vp.sin(2*t),0,0)
    t = t + 0.1                 