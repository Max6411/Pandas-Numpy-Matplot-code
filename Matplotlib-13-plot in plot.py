import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.arange(1, 8)
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  # 先绘制一个大图, 这里是大图的属性:左下角的位置以及宽高  这里是百分比
ax1 = fig.add_axes([left, bottom, width, height])  # 在初始窗口中添加一个窗口 四个属性都是所占比例
ax1.plot(x, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25  # 准备添加一个小窗口 , 这里是它的属性
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, color='red')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title')

plt.axes([0.6, 0.2, 0.25, 0.25])  # 这里直接用plot进行操作
plt.plot(y[::-1], x, color='yellow')
plt.xlabel('x')  # 修改plot的x标签 , 直接.xlabel 而不是set_xlabel
plt.ylabel('y')
plt.title('the inside 2')
plt.show()