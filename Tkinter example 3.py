from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

data1 = {'Date': ['3/31/2018','6/30/2018','9/30/2018','12/31/2018','3/31/2019','6/30/2019','9/30/2019','12/31/2019','3/31/2020','6/30/2020'],
         'Revenue': [32498000,34448000,36820000,40797000,45556000,46173000,49797000,58936000,62924000,74663000]
        }
df1 = DataFrame(data1,columns=['Date','Revenue'])


data2 = {'Year': ['12/31/2017','12/31/2018','12/31/2019'],
         'AnnualRevenue': [1.05E+08,1.45E+08,2E+08]
        }
df2 = DataFrame(data2,columns=['Year','AnnualRevenue'])
annual_x_labels = df2["AnnualRevenue"].pct_change(periods = 1)*100
annual_x_labels[0] = 0
for i in range(len(annual_x_labels)):
    annual_x_labels[i] = float("{:.2f}".format(annual_x_labels[i]))

root = Tk()
root.title('Tkinter example #3')
root.geometry("250x200")

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent Fatal Python Error: PyEval_RestoreThread: NULL tstate

def quarterly():
	plt.bar(df1.Date,df1.Revenue)
	plt.xticks(rotation=45)
	plt.ylabel('Total ( x 10 millions )')
	plt.show()

def annual():
	fig, ax = plt.subplots()
	figure = ax.bar(df2.Year,df2.AnnualRevenue)
	i = 0
	for rect in figure:
		if i != 0:
			height = rect.get_height()
			ax.annotate(annual_x_labels[i], 
				xy=(rect.get_x() + rect.get_width() / 2, height),
				ha='center', va='bottom')
		i = i+1

	ax.set_ylabel('Total ( x 100 millions )')	
	fig.tight_layout()
	plt.show()

# Quarterly button
btn1 = Button(root, text="Quaterly Graph", command=quarterly)
btn1.pack()

# Annual button
btn2 = Button(root, text="Annual Graph", command=annual)
btn2.pack()

# CLOSE button
button = Button(master=root, text="CLOSE", command=_quit, fg="red")
button.pack(side=BOTTOM)

root.mainloop()