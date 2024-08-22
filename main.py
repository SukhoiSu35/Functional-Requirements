import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('Csv file name')


name_df = original_df.drop["Column name here."]

#----Define Functions Below----#
def showOriginalData():
    subroot = Tk() 
    Label(subroot, text=original_df).pack()

def showUpdatedData():
    subroot = Tk()
    Label(subroot, text= name_df).pack()

def showCharts():
    name_df.plot(
                    kind='bar',
                    x='X Axis value here',
                    y='Y Axis value here',
                    color='blue',
                    alpha=0.3,
                    title='Title Here')
    plt.show()


print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the cost of a big mac in AUD
    4 - Quit Program
        """)
    
root = Tk()
Label(root, text="Intro Text Here").pack()
Label(root, text="Choose from the options below:").pack()
Button(root, text="Show Original Data Frame", command = showOriginalData)
Button(root, text="Show Updated Data Frame", command = showUpdatedData)
Button(root, text="Visualise Data", command = showCharts)
Button(root, text="Quit", command = root.destroy)
