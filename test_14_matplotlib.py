import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4)
plt.plot(x, x * 0.5, 'r-', label = 'y = 0.5x')
plt.plot(x, x * 1.5, 'g--', label = 'y = 1.5x')
plt.plot(x, x * 3.0, 'b:', label = 'y = 3.0x')
plt.legend(loc='upper left', shadow=True)
plt.show()

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(X)
S = np.sin(X)
plt.plot(X, C, color = 'blue', linewidth = 2.0, linestyle = '-', label = 'cos')
plt.plot(X, S, color = 'red', linewidth = 2.0, linestyle = '--', label = 'sin')
plt.legend()
plt.show()

i = np.random.rand(200)
j = np.random.rand(200)
plt.scatter(i, j)
plt.show()

k = np.random.rand(90, 2)
label = list(np.ones(40)) + list(2 * np.ones(30)) + list(3 * np.ones(20))
label = np.array(label)
idx1 = np.where(label==1)
idx2 = np.where(label==2)
idx3 = np.where(label==3)
p1 = plt.scatter(k[idx1, 0], k[idx1, 1], marker = 'x', color = 'r', label = '1', s =40)
p2 = plt.scatter(k[idx2, 0], k[idx2, 1], marker = '+', color = 'b', label = '2', s =30)
p3 = plt.scatter(k[idx3, 0], k[idx3, 1], marker = 'o', color = 'g', label = '3', s =20)
plt.legend(loc='upper left')
plt.show()