import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1
plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)  # 可能还会有z轴，所以传入的是一个列表，后面可以加上 逗号，
ax = plt.gca()
ax.spines['right'].set_color('none')  # 使右边框透明
ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))  # 把下边框的位置设置在纵坐标为0的地方
ax.xaxis.set_ticks_position('bottom')
ax.spines['left'].set_position(('data', 0))  # 注意这里面有两层括号
ax.yaxis.set_ticks_position('left')
x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)  # 用k颜色的--线连线 横坐标集+纵坐标集
plt.scatter([x0, ], [y0, ], s=50, color='b')  # scatter描点， s是size color是颜色 坐标：【x0，y0】
plt.annotate('2x+1=%s' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),  # xycoords='data' 是说基于数据的值来选位置
             textcoords='offset points', fontsize=16,  # xytext=(+30, -30) 和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3, rad=.2"))  #  arrowprops是对图中箭头类型的一些设置
plt.text(-3.7, 3, 'This is the some text', fontdict={'size': 16, 'color': 'r'})  # text可以在图中加入注释  -3，7， 3 是选择位置

plt.show()
