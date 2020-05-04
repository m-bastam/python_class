#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

# Modify adding a Label
a_label = ttk.Label(win, text="A Label" )
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get() + ' ' + str(chVarEn.get()))

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable = name)
name_entered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                 # <= change column to 2

# Creating three checkbuttons
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable = number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn , command = click_me)
check2.deselect()
check2.grid(column=1, row=4)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4)                     

# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold",  "Red", "Aliceblue", "Orange", "Brown", "White", "Silver"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    win.configure(background = colors[radSel])
  

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Radiobutton Globals
# COLOR1 = "AliceBlue"
# COLOR2 = "Gold"
# COLOR3 = "Red"
# rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=0, command=radCall)
# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)   

# rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=1, command=radCall)
# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)  


# rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=2, command=radCall)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)
# rad3.select()
# Next we are selecting a non-existing index value for radVar. If we did not set the default value
# to a value outside the range of ourRadiobutton widgets, one of the radio buttons would be 
# selected when the GUI appears.
radVar.set(20)                                 
 
# Now we are creating all three Radiobutton widgets within one loop
for col in range(8):                             
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,value=col, command=radCall)          
    curRad.grid(column=col, row=5) 

# Using a scrolled Text control    
scrol_w  = 30
scrol_h  =  3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

name_entered.focus()      # Place cursor into name Entry

#======================
# Start GUI
#======================
win.mainloop()