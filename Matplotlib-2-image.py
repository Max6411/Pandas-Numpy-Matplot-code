import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2  # x的2次幂
plt.figure(num=3, figsize=(8, 5))  # 编号为3；大小为(8, 5) 大小是照片尺寸大小而不是坐标区间
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # 图像颜色/线宽/线格式
plt.show()