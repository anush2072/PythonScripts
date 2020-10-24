from tkinter import *

root = Tk()
root.title("Tk dropdown example")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options in the Year drop-down
choices = { '2016','2017','2018','2019','2020'}
tkvar.set('2020') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose an Year").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( "You chose year : " + tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()                                                                                                                                                     