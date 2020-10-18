import matplotlib
matplotlib.use("TkAgg")
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# ------------------------- Replace this block to populate data from DataFrame --------------------
data1 = {'Date': ['3/31/2018','6/30/2018','9/30/2018','12/31/2018','3/31/2019','6/30/2019','9/30/2019','12/31/2019','3/31/2020','6/30/2020'],
         'Revenue': [32498000,34448000,36820000,40797000,45556000,46173000,49797000,58936000,62924000,74663000]
        }
df1 = DataFrame(data1,columns=['Date','Revenue'])
quarterly_x_labels = df1["Revenue"].pct_change(periods = 1)*100
quarterly_x_labels[0] = 0
for i in range(len(quarterly_x_labels)):
    quarterly_x_labels[i] = float("{:.2f}".format(quarterly_x_labels[i]))

data2 = {'Year': ['12/31/2017','12/31/2018','12/31/2019'],
         'AnnualRevenue': [1.05E+08,1.45E+08,2E+08]
        }
df2 = DataFrame(data2,columns=['Year','AnnualRevenue'])
#print(pd.to_datetime(df2.Year))
annual_x_labels = df2["AnnualRevenue"].pct_change(periods = 1)*100
annual_x_labels[0] = 0
for i in range(len(annual_x_labels)):
    annual_x_labels[i] = float("{:.2f}".format(annual_x_labels[i]))
#--------------------------------------------------------------------------------------------------

class MorningStarCharts:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.fig, self.ax = plt.subplots()
		self.canvas = FigureCanvasTkAgg(self.fig, self.master)
		self.config_window()
		self.displayAnnual = False
		self.draw_Annual()
		self.frame.place()

	def config_window(self):
		toolbar = NavigationToolbar2Tk(self.canvas, self.master)
		toolbar.update()
		self.canvas.get_tk_widget().place(relheight=0.8, relwidth=1)	
		
		# Quarterly button
		self.btn1 = Button(self.master, text="Quaterly Graph", cursor="hand2", command=self.draw_Quarterly)
		self.btn1.place(relx=0.30, rely=0.812, relheight=0.05, relwidth=0.2)

		# Annual button
		self.btn2 = Button(self.master, text="Annual Graph", cursor="hand2", command=self.draw_Annual)
		self.btn2.place(relx=0.55, rely=0.812, relheight=0.05, relwidth=0.2)

		# CLOSE button
		self.button = Button(self.master, text="CLOSE", cursor="hand1", command=self._quit, fg="red")
		self.button.place(relx=0.40, rely=0.875, relheight=0.05, relwidth=0.2)

	def _quit(self):
		self.master.quit()     # stops mainloop
		self.master.destroy()  # this is necessary on Windows to prevent Fatal Python Error: PyEval_RestoreThread: NULL tstate

	def draw_Quarterly(self):
		print('Displaying quarterly charts')
		if self.displayAnnual is True:
			self.ax.cla() # clear current figure
			figure = self.ax.bar(df1.Date,df1.Revenue, color='g')
			i = 0
			for rect in figure:
				if i != 0:
					height = rect.get_height()
					self.ax.annotate(quarterly_x_labels[i], xy=(rect.get_x() + rect.get_width() / 2, height), ha='center', va='bottom')
				i = i+1
			self.ax.tick_params('x', labelrotation=45, labelsize=7)
			self.ax.set(title='Quarterly Revenue ( x 10 millions )')
			self.canvas.draw()
			self.displayAnnual = False
	
	def draw_Annual(self):
		print('Displaying Annual chart')
		if self.displayAnnual is False:
			self.ax.cla() # clear current axes
			figure = self.ax.bar(df2.Year,df2.AnnualRevenue, color='y')
			i = 0
			for rect in figure:
				if i != 0:
					height = rect.get_height()
					self.ax.annotate(annual_x_labels[i], xy=(rect.get_x() + rect.get_width() / 2, height), ha='center', va='bottom')
				i = i+1
			self.ax.tick_params('x', labelrotation=25, labelsize='small')
			self.ax.set(title='Annual Revenue ( x 100 millions )')
			self.canvas.draw()
			self.displayAnnual = True

def main():
	root = Tk()
	root.title('MorningStar Charts')
	root.geometry("600x600")
	MorningStarCharts(root)
	root.mainloop()

if __name__ == '__main__':
    main()