import matplotlib.pyplot as plt
import numpy as np

N = 12
x = np.arange(N)
y1 = (1 - x/float(N)) * np.random.uniform(0.5, 1.0, N)
y2 = (1 - x/float(N)) * np.random.uniform(0.5, 1.0, N)

plt.bar(x, +y1, facecolor='red', edgecolor='blue')
plt.bar(x, -y2)

plt.xlim(-.5, N)  # 第一条柱形会到x<0的区域， 需要大于-0.5而不是0
plt.ylim(-1.25, 1.25)

z1 = zip(x, y1)
z2 = zip(x, y2)
for x, y in z1:
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')  # 注释的位置 就是x，y的坐标 显示纵坐标y
for x, y in z2:
    plt.text(x, -y, '%.2f' % y, ha='center', va='top')  # ha是水平位置，va是竖直位置。 va=top就是柱形图的外部

plt.show()
