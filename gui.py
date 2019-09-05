'tk toolkit'
import tkinter
from tkinter import *

'tk extension'
from tkinter import ttk

'''
    Function converts feet to meters
'''
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        raise('Value {} is incorrect'.format(value))

#sets up the main window and sets the title to Feet to Meters'
root = Tk()
root.title("Feet to Meters")

''' Creates a frame widget and places in the main window padding is for left, right, top and bottom
Width and height can be used to force the size of the frame otherwise, geometry manager makes it large enough
to accomodate all the widgets
'''
mainframe = ttk.Frame (root, padding="3 3 12 12")

''' Column and row indicates the column and row to start at for widgets
sticky means which edges of a cell a widget should stick to (it is essentially an anchor)'''
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# These lines say that if the main window is resized, the frame should expand take up the extra space based on the weight
mainframe.columnconfigure (0, weight= 1)
mainframe.rowconfigure (0, weight=1)

# String Variable class allows python to know when a change occurs.  These are global variables'
feet = StringVar ()
meters = StringVar ()

'''
Create a text entry box in the frame.  The textvariable is assigned the global variable feet.  This means if the entry
is changed the global variable is automatically updated
'''
feet_entry = ttk.Entry (mainframe, width=7, textvariable=feet)

# Indicates placement of the feet entry text box
feet_entry.grid (column=2, row=1, sticky= (W, E))

'''
Places the label that will display meters.  In this cases, if a widget changes text variable, the widget is automatically
updated
'''
ttk.Label (mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

'''
Adds a calculate button to the frame; command calls calculate function
Here when the textvariable is changed
'''

ttk.Button (mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)

# Adds 3 text labels to the frame
ttk.Label (mainframe, text="feet").grid(column = 3, row = 1, sticky = W)
ttk.Label (mainframe, text="is equivalent to").grid (column = 1, row = 2, sticky = E)
ttk.Label (mainframe, text="meters").grid(column = 3, row = 2, sticky = W)

'''
Loops through each widget in the frame and adds some padding to space the widgets
'''
for child in mainframe.winfo_children ():
    child.grid_configure (padx=5, pady=5)

# Puts the focus on the entry widget so user can start typing
feet_entry.focus ()

# This says that if the user hits return anywhere in the frame or the calculate button, call the calculate function
root.bind ('<Return>', calculate)

# Tells tk to enter its event loop which is required for program to run
root.mainloop()

# Used by Permission © 2007-2015 Mark Roseman (@markroseman)
#
