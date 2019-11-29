import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1*y1
fig, ax1 = plt.subplots() # 返回初始窗口fig, 和分好的窗口
ax2 = ax1.twinx()  # 生成如同镜面效果后的ax2
ax1.plot(x, y1, color='green')
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='green')

ax2.plot(x, y2, color='blue')
ax2.set_ylabel('Y2 data', color="blue")

plt.show()