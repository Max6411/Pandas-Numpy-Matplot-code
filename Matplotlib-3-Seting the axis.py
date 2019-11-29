import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = x**2
plt.xlim((-2, 2))  # 限制x轴的区间
plt.ylim((-1, 4))
plt.xlabel('i am x axis')  # 给x轴命名
plt.ylabel('i am y axis')
plt.plot(x, y)
plt.show()
# show()之后plt所设置的属性都会消除


new_x = np.linspace(-1, 4, 5)  #
#  print(new_x)  [-1.    0.25  1.5   2.75  4.  ]
plt.xticks(new_x)  # 使用新定义的x轴坐标值(仅起标注作用，无法限制）
plt.yticks([-2, -1, 4, 0, 5],['one', 'two', 'three', 'four', 'five'])  # 自定义y轴坐标刻度以及显示
plt.plot(x, y)
ax = plt.gca()  # 使用plt.gca获取当前坐标轴信息
ax.spines['right'].set_color('blue')  # 设置右边框的颜色/不是坐标轴 <>left
ax.spines['bottom'].set_color('orange')  # 下边框即X轴 <>top
ax.xaxis.set_ticks_position('top')  # 设置x坐标刻度的位置 top是上边框而不是x轴上方（top/bottom/both/default/none)
ax.spines['bottom'].set_position(('data', 3))  # 设置边框的位置 bottom：x轴/ 设置到y轴值为3的位置
plt.show()