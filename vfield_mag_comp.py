# create a colored VF plot to compare slightly perturbed VFs.
# This is not a general program, and is only relevant to the blog post. 
import numpy as np
import matplotlib.pyplot as plt

# define the meshgrid we are plotting over
x,y = np.meshgrid(np.linspace(-5,5,20),np.linspace(-5,5,20))

# define the function we are making the DF for
def fnc(x,y,t=0):
    return np.sin(x+t+y),np.cos(x-t)+np.sin(y)

t1, t2 = 4.8,4.9 # slightly different parameter values
u1,v1 = fnc(x,y,t=t1)
u2,v2 = fnc(x,y,t=t2)
u = u1-u2
v = v1-v2

# magnitude of vectors for coloring
magnitude = np.sqrt(u**2 + v**2)

fig, ax = plt.subplots()
quiver = ax.quiver(x,y,u,v,magnitude,cmap='plasma',scale_units="xy",angles="xy") # initial vector field

# add colorbar for reference
cbar = fig.colorbar(quiver, ax=ax)
cbar.set_label("Vector magnitude")

ax.set_title("Perturbed Vector Field Difference")
plt.show()