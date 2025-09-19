# given a function, plot its direction field
import numpy as np
import matplotlib.pyplot as plt
import eulers 
from matplotlib.widgets import Slider

# define the meshgrid we are plotting over
x,y = np.meshgrid(np.linspace(-5,5,20),np.linspace(-5,5,20))

# define the function we are making the DF for
def fnc(x,y,t=4.9):
    return np.sin(x+t+y),np.cos(x-t)+np.sin(y)

u,v = fnc(x,y) # evaluate the fnc at each point

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25) # add space for the slider bar

quiver = ax.quiver(x,y,u,v) # initial vector field

# h update and euler's is defined first. Since the VF does not depend on the euler's apx,
# we use two different update functions
x0 = np.zeros((2,1),dtype=float)
a,b = 0,20
sln = eulers.sysfeuler(fnc,x0,a,b,s=4.9,h=1e-1)
line, = ax.plot(sln[0][:],sln[1][:],'b')

plt.subplots_adjust(left=0.25) # space for left slider bar
hslider_ax = plt.axes([.1,.2,.03,.65])
hslider = Slider(hslider_ax,'h',1e-3,1,valinit=1e-1,orientation="vertical")

def hupdate(hval):
    h = hslider.val
    sln_new = eulers.sysfeuler(fnc,x0,a,b,h=h,s=slider.val)
    line.set_data(sln_new[0][:],sln_new[1][:])
    fig.canvas.draw_idle()

hslider.on_changed(hupdate)

# add the slider axis
slider_ax = plt.axes([.2,.1,.65,.03])
slider = Slider(slider_ax,'s',0,2*np.pi,valinit=4.9)

def update(val):
    s = slider.val
    u_new,v_new = fnc(x,y,s)
    quiver.set_UVC(u_new,v_new)
    # now we recompute euler's method
    sln_new = eulers.sysfeuler(fnc,x0,a,b,h=hslider.val,s=s)
    line.set_data(sln_new[0][:],sln_new[1][:])
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()