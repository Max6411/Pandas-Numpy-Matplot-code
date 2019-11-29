import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)  # x 为-1到1的50个散列点
y = 2 * x + 1
plt.figure()  # 定义一个图像窗口
plt.plot(x, y)  # 使用plt.plot画(x ,y)曲线.
plt.show()  # 显示连线后的图像  而不是散列点
