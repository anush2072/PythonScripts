from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title('Tkinter example #1')
root.geometry("1200x1040")

def graph():
	prices = np.random.normal(200, 250,500)
	plt.hist(prices, 50)
	plt.show()

btn = Button(root, text="Graph it!", command=graph)
btn.pack()
root.mainloop()