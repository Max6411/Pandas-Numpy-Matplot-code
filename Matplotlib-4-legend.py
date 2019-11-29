import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure()
plt.xlim((-1, 2))
plt.ylim((-2, 3))
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], ['really bad', 'bad', 'normal', 'good', 'really good'])
l1, = plt.plot(x, y1, label='linear line')  # plot以逗号结尾， 因为返回的是一个列表
l2, = plt.plot(x, y2, label='square line', color='red', linewidth='1.0', linestyle='--')
plt.legend(loc='upper right')  # legend显示的是上述线段的label
plt.legend(handles=[l1, l2], labels=['Straigth', 'Bend'], loc='best')  # legend可以同时修改两个图例
""" legend的位置loc有以下选择， 最佳位置排名
 'best' : 0,          
 'upper right'  : 1,
 'upper left'   : 2,
 'lower left'   : 3,
 'lower right'  : 4,
 'right'        : 5,
 'center left'  : 6,
 'center right' : 7,
 'lower center' : 8,
 'upper center' : 9,
 'center'       : 10,
"""