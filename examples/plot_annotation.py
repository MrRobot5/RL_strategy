"""
Matplotlib 中的 annotate 示例
annotate 用于在图形上给数据添加文本注解，而且支持带箭头的划线工具，方便我们在合适的位置添加描述信息。

@since 2023年12月20日11:05:34
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 绘制一个余弦曲线
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

# 绘制一个黑色，两端缩进的箭头
# 注释文本的内容 'local max'
# xytext：注释文本的坐标点，也是二维元组，默认与xy相同
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            xycoords='data',
            # arrowprops：箭头的样式，dict（字典）型数据
            arrowprops=dict(facecolor='black', shrink=0.05)
            )
ax.set_ylim(-2, 2)
plt.show()