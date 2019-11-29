import matplotlib.pyplot as plt
import numpy as np

N = 1024
x = np.random.normal(0, 1, N)
y = np.random.normal(0, 1, N)  # 就是random.rann(0, 1, N)
T = np.arctan2(y, x)

plt.scatter(x, y, s=75, c=T, alpha=.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()
