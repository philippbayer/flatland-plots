""" In Flatland, women are just lines.
This script initializes the view to the "most dangerous" view in which women are completely hidden from the view (due to height not existing).
"""

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# woman
x = [0,1]
y = [0,0]
ax.plot(x,y,zs=0, color="k")
ax.view_init(elev=0, azim=0)
plt.show()

