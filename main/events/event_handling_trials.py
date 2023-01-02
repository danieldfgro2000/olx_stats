
# fig, ax = plt.subplots()
# ax.plot(np.random.rand(10))
#
#
# def onclick(event):
# 	print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f'
# 	      % ('double' if event.dblclick else 'single', event.button, event.x, event.y, event.xdata, event.ydata))
#
#
# cid = fig.canvas.mpl_connect('button_press_event', onclick)
# fig.canvas.mpl_disconnect(cid)
#
#
# fig, ax = plt.subplots()
# ax.set_title('click on points')
#
# line, = ax.plot(np.random.rand(100), 'o',
#                 picker=True, pickradius=5)  # 5 points tolerance
#
# def onpick(event):
#     thisline = event.artist
#     xdata = thisline.get_xdata()
#     ydata = thisline.get_ydata()
#     ind = event.ind
#     points = tuple(zip(xdata[ind], ydata[ind]))
#     print('onpick points:', points)
#
# fig.canvas.mpl_connect('pick_event', onpick)
#
# plt.show()