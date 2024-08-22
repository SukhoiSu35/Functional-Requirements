import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('accident_details_compiled.csv')


name_df = original_df.drop(columns=["Date"])

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
                    x='Location',
                    y='Fatalities',
                    color='blue',
                    alpha=0.3,
                    title='Accidents')
    plt.show()


print("""Air Crash Investigation
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the accidents
    4 - Quit Program
        """)
    
root = Tk()
Label(root, text="Welcome to aircrash data").pack()
Label(root, text="Choose from the options below:").pack()
Button(root, text="Show Original Data Frame", command = showOriginalData).pack()
Button(root, text="Show Updated Data Frame", command = showUpdatedData).pack()
Button(root, text="Visualise Data", command = showCharts).pack()
Button(root, text="Quit", command = root.destroy).pack()
root.mainloop()
