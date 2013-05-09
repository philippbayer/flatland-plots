""" The narrator of Flatland is a humble square. """

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# let's just draw a square
x = [0, 0, 1, 1, 0, 0]
y = [0, 0, 0, 1, 1, 0]
ax.plot(x,y,zs=0, color="k")
ax.view_init(elev=0, azim=0) 

plt.show()
