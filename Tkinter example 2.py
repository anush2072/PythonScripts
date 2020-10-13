#https://matplotlib.org/3.1.1/gallery/pyplots/pyplot_two_subplots.html#sphx-glr-gallery-pyplots-pyplot-two-subplots-py
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
    
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# Variables, DataFrames etc
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


# The main tkinter window 
root = tk.Tk()
root.wm_title("Tkinter example#2 : Embedding in Tk")

figure1 = Figure(figsize=(5, 4), dpi=100)
figure1.add_subplot(111).plot(t1, f(t1), color='tab:blue', marker='o')
#plt.plot(t2, f(t2), color='red')

figure1.add_subplot(212).plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')
# #plt.show()



canvas = FigureCanvasTkAgg(figure1, master=root) 
canvas.mpl_connect("key_press_event", on_key_press)
canvas.draw()

#ToolBar
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# CLOSE button
button = tk.Button(master=root, text="CLOSE", command=_quit)
button.pack(side=tk.BOTTOM)


tk.mainloop()
