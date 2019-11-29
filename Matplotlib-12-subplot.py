import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
plt.subplot(2, 2, 1) # 将整个图像窗口分为2行2列, 当前位置为1  可以简写成plt.subplot(221)
plt.plot([0, 1], [0, 2])  # 在第1个位置创建一个图像 x:0->1 y:0->2  .

plt.subplot(2, 2, 2)    # 将整个图像窗口分为2行2列, 当前位置为2
plt.plot([0, 1], [0, 3])  # 在第2个位置创建一个图像， 这会和第一个图像同时存在

plt.subplot(212)  # 按照2,1 分配则下半部分的位置为2
plt.plot([0, 1], [0, 5])  # 在当前分配情况下的第2个位置创建一个图像

plt.show()

# 多格显示i  subplot2grid

plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # 将图像分成(3,3) 目前位置在(0,0) 创建一个图像(列跨3列) 默认是行1列1
ax1.plot([0, 1], [0, 1])  # 上行是把图像分格,ax1是其中的一个格子, 现在在ax1上画图像
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax4.scatter([1, 2], [2, 2])  # ax4是一个格子, 现在在这上面画图像  scatter 是描点不是描直线  这里只会出现两个点!
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')  # 这里ax4可以看做一个普通的plot, 可以做任何属性修改
plt.show()


# gridspec
plt.figure()  # 创建一个默认的图像窗口
gs = gridspec.GridSpec(3, 3)  # 将窗口分成(3,3)
ax6 = plt.subplot(gs[0, :])  # 将0行 整列划分成一个区域
ax7 = plt.subplot(gs[1:, 2])  # 将1行到最后一行, 第2列划分为一个区域
ax8 = plt.subplot(gs[1, :2])  # 到2但不包含2
ax9 = plt.subplot(gs[-1, 0])  # 倒数第一行
ax10 = plt.subplot(gs[-1, -2])  # 通过gridspec把窗口分成和上面一样的形式
plt.show()

f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)  # 返回值会返回一个figure我们用f保存,还有四个窗口
ax11.scatter([0, 1], [0, 2])
plt.show()