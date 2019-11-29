import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x
plt.figure()
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
for label in ax.get_xticklabels() + ax.get_yticklabels():  # 操控x，y轴的属性
    label.set_fontsize(12)  # x，y轴上的坐标显示字体大小
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7, zorder=2))
# bbox与目的类容的透明度相关， 前景色/边框色/透明度/zorder 在Z轴上的层数
plt.show()