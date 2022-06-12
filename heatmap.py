from matplotlib import pyplot as plt

import seaborn as sns

import numpy as np

def onpick(event):
    #print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #      ('double' if event.dblclick else 'single', event.button,
    #       event.x, event.y, event.xdata, event.ydata))
    print(event)
    try:
        event.xydata += 1
    except:
        pass


uniform_data = np.random.rand(28, 28)
ax = sns.heatmap(uniform_data)
ax.figure.canvas.mpl_connect("motion_notify_event", onpick)
plt.show()
