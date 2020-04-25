'''
Out of all the GUI methods, tkinter is the most commonly used method. 
It is a standard Python interface to the Tk GUI toolkit shipped with Python. 
To create a tkinter app:
    1-Importing the module – tkinter
    2-Create the main window (container)
    3-Add any number of widgets to the main window
    4-Apply the event Trigger on the widgets.
There are two main methods:
-Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1):
    To create a main window
-mainloop(): is used when your application is ready to run. 
    mainloop() is an infinite loop used to run the application, wait for an event
    to occur and process the event as long as the window is not closed. 

'''
import tkinter as tk 

# r = tk.Tk() 
# r.title('Counting Seconds') 
# button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
# button.pack()
# r.mainloop() 

# master = tk.Tk() 
# w = tk.Canvas(master, width=40, height=60) 
# w.pack() 
# canvas_height=40
# canvas_width=400
# y = int(canvas_height / 2) 
# w.create_line(0, y, canvas_width, y ) 
# master.mainloop()


# #from tkinter import *
# master = tk.Tk() 
# var1 = tk.IntVar() 
# tk.Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=tk.W) 
# var2 = tk.IntVar() 
# tk.Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=tk.W) 
# tk.mainloop() 

from tkinter import *

# master = Tk() 
# Label(master, text='First Name').grid(row=0) 
# Label(master, text='Last Name').grid(row=1) 
# e1 = Entry(master) 
# e2 = Entry(master) 
# e1.grid(row=0, column=1) 
# e2.grid(row=1, column=1) 
# mainloop() 

# root = Tk() 
# frame = Frame(root) 
# frame.pack() 
# bottomframe = Frame(root) 
# bottomframe.pack( side = BOTTOM ) 
# redbutton = Button(frame, text = 'Red', fg ='red') 
# redbutton.pack( side = LEFT) 
# greenbutton = Button(frame, text = 'Brown', fg='brown') 
# greenbutton.pack( side = LEFT ) 
# bluebutton = Button(frame, text ='Blue', fg ='blue') 
# bluebutton.pack( side = LEFT ) 
# blackbutton = Button(bottomframe, text ='Black', fg ='black') 
# blackbutton.pack( side = BOTTOM) 
# root.mainloop() 

# top = Tk() 
# Lb = Listbox(top) 
# Lb.insert(1, 'Python') 
# Lb.insert(2, 'Java') 
# Lb.insert(3, 'C++') 
# Lb.insert(4, 'Any other') 
# Lb.pack() 
# top.mainloop() 

# root = Tk() 
# menu = Menu(root) 
# root.config(menu=menu) 
# filemenu = Menu(menu) 
# menu.add_cascade(label='File', menu=filemenu) 
# filemenu.add_command(label='New') 
# filemenu.add_command(label='Open...') 
# filemenu.add_separator() 
# filemenu.add_command(label='Exit', command=root.quit) 
# helpmenu = Menu(menu) 
# menu.add_cascade(label='Help', menu=helpmenu) 
# helpmenu.add_command(label='About') 
# ourMessage ='This is our Message'
# messageVar = Message(root, text = ourMessage) 
# messageVar.config(bg='lightgreen') 
# messageVar.pack() 
# root.mainloop() 


# from tkinter import *
# root = Tk() 
# v = IntVar() 
# Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W) 
# Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W) 
# w = Scale(root, from_=0, to=42) 
# w.pack() 
# w = Scale(root, from_=0, to=200, orient=HORIZONTAL) 
# w.pack() 
# mainloop() 


# from tkinter import *
# root = Tk() 
# scrollbar = Scrollbar(root) 
# scrollbar.pack( side = RIGHT, fill = Y ) 
# mylist = Listbox(root, yscrollcommand = scrollbar.set ) 
# for line in range(100): 
#    mylist.insert(END, 'This is line number' + str(line)) 
# mylist.pack( side = LEFT, fill = BOTH ) 
# scrollbar.config( command = mylist.yview ) 
# mainloop() 


from tkinter import *
root = Tk() 
root.title('GfG') 
top = Toplevel() 
top.title('Python') 
top.mainloop() 

