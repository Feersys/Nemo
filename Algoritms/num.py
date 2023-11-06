import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
xx, yy = np.meshgrid(x, y)
print(xx, yy)
res = np.sin(xx) + np.cos(yy)
res2 = np.sin(yy) + np.cos(xx)
res3 = np.sin(xx) + np.cos(yy)
hyperbole = np.where(xx * yy < 10)
parable = np.where(yy > xx ** 2)
circle = np.where(xx ** 2 + yy ** 2 < 10 ** 2)
res[circle] = 0
res2[hyperbole] = 0
res3[parable] = 0
plt.imshow(res, cmap='seismic')
# plt.imshow(res2, cmap="seismic")
# plt.imshow(res3, cmap="seismic")
plt.show()
# plt.axis([xmin, xmax, ymin, ymax]) диапазон для осей
