# create a colored VF plot to show the change in angle between two VFs.
# this is not a general program, and is only suited for the blog post
import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

def fnc(x, y, t=0):
    return np.sin(x + t + y), np.cos(x - t) + np.sin(y)

t1, t2 = 4.8, 4.9
u1, v1 = fnc(x, y, t=t1)
u2, v2 = fnc(x, y, t=t2)

# normalize both fields to unit vectors
mag1 = np.sqrt(u1**2 + v1**2)
mag2 = np.sqrt(u2**2 + v2**2)

u1n, v1n = u1 / mag1, v1 / mag1
u2n, v2n = u2 / mag2, v2 / mag2

# compute angle difference
theta1 = np.arctan2(v1n, u1n)
theta2 = np.arctan2(v2n, u2n)
dtheta = theta1 - theta2
# wrap into [-pi, pi]
dtheta = (dtheta + np.pi) % (2 * np.pi) - np.pi

# plot arrows with unit length, colored by angle difference
fig, ax = plt.subplots(figsize=(6,6))
quiver = ax.quiver(
    x, y, u1n - u2n, v1n - v2n, dtheta,
    cmap="twilight", scale=0.5, scale_units="xy", angles="xy"
)

cbar = fig.colorbar(quiver, ax=ax)
cbar.set_label("Angle difference (radians)")

ax.set_title("Change in Angle")
ax.set_aspect("equal")
plt.show()
