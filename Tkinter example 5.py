# Scroll backwards and forwards through matplotlib plots
# An easy way to achieve that is storing in a list a tuple of the x and y arrays and then 
#	use a handler event that picks the next (x,y) pair to be plotted
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# define your x and y arrays to be plotted
t = np.linspace(start=0, stop=2*np.pi, num=100)
y1 = np.cos(t)
y2 = np.sin(t)
y3 = np.tan(t)
plots = [(t,y1), (t,y2), (t,y3)]

np.random.seed(1)

N = 100
y = np.random.randint(10,100,100)
now = dt.datetime.now()
then = now + dt.timedelta(days=100)
days = mdates.drange(now,then,dt.timedelta(days=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
plt.plot(days, days)

# now the real code :) 
# curr_pos = 0

# def key_event(e):
    # global curr_pos

    # if e.key == "right":
        # curr_pos = curr_pos + 1
    # elif e.key == "left":
        # curr_pos = curr_pos - 1
    # else:
        # return
    # curr_pos = curr_pos % len(plots)

    # ax.cla()
    # ax.plot(plots[curr_pos][0], plots[curr_pos][1])
    # fig.canvas.draw()

# fig = plt.figure()
# fig.canvas.mpl_connect('key_press_event', key_event)
# ax = fig.add_subplot(111)
# ax.plot(t,y1)
plt.show()