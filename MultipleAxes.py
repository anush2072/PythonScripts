from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

fig = plt.figure()
x = np.linspace(start=0, stop=10, num=50)

ax1 = fig.add_axes([0.1,0.6,0.8,0.4])
ax1.plot(x, np.sin(x))
ax1.set_ylabel('sin(x)', color='m')

ax2 = fig.add_axes([0.1,0.1,0.75,0.4])
ax2.plot(x, np.cos(x))
ax2.set_ylabel('cos(x)', color='b')

plt.show()