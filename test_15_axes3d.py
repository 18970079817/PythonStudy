from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig1 = plt.figure()
ax1 = Axes3D(fig1)
plt.show()

fig2 = plt.figure()
ax2 = Axes3D(fig2)
X = np.arange(-2, 2, 0.25)
Y = np.arange(-2, 2, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax2.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'rainbow')
ax2.set_xlabel('x label', color = 'r')
ax2.set_ylabel('y label', color = 'g')
ax2.set_zlabel('z label', color = 'b')
plt.show()