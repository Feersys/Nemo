import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
xx, yy = np.meshgrid(x, y)
print(xx, yy)
res = np.sin(xx) + np.cos(yy)
circle = np.where(xx**2 + yy**2 < 10**2)
res[circle] = 0
plt.imshow(res, cmap='seismic')
plt.show()