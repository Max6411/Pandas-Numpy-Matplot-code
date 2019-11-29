import matplotlib.pyplot as plt
import numpy as np

def f(x, y):  # 输入x，y返回高z的函数
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

N = 256
x = np.linspace(-3, 3, N)
y = np.linspace(-3, 3, N)
X, Y = np.meshgrid(x, y)  # meshgrid在二维平面中将每一个x和每一个y分别对应起来，编织成栅格


plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='hot')  # 8表示填充8种颜色
plt.contourf(X, Y, f(X, Y), 8, colors='black', linewidth=.5)  # 8代表等高线的密集程度
plt.show()