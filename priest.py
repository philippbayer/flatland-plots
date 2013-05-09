# Priests, as highest members of the society, are circles.

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
circle = Circle((0.5,0.5), 0.2, facecolor="none")
ax.add_patch(circle)
ax.view_init(elev=-2.7, azim=0) # bit annoying - for some reason, elev=0 doesn't work in this case.
art3d.pathpatch_2d_to_3d(circle, z=0, zdir="z")
plt.show()
