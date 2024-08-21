from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
root = Tk()
root.title("Accident Details from 2010") #Name of the gui 
root.configure(background = "white")
root.maxsize(5000, 5000)
root.minsize(1000, 1000)
root.geometry("500x100+10+23")
text = Label(root,text = "Choose your data")
text.pack()
Dataset = pd.read_csv ('accident_details_compiled.csv')
var = IntVar()  # variable class
item1 = Checkbutton(root, text="Date",
        variable=var, command=selectItems(var,"Date"))
item1.pack(anchor='w')
var2 = IntVar()  # variable class
item2 = Checkbutton(root, text="Date",
        variable=var2, command=selectItems(var2,"Time"))
item2.pack(anchor='w')
root.mainloop()

