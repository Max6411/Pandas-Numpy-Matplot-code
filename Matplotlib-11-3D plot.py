import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()  # 先创建一个plt窗口
ax = Axes3D(fig)    # 再将窗口传入Axes3D中

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(x, y)  # 把每一个x和每一个y分别对应起来，编织成栅格
r = np.sqrt(X**2 + Y**2)  # 这里的r不是一个元素而是一个列表
Z = np.sin(r)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# rstride 和 cstride 分别代表 row 和 column 的跨度。
ax.contour(X, Y, Z, zdir='z', offset=1, cmap=plt.get_cmap('rainbow'))  # 投影 zdir是去掉哪个轴投影
plt.show()