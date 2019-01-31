# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
textlable = Label(root, text='Tkinter test')
textlable.pack()
photo = PhotoImage(file="400.gif")
imagelable = Label(root, image = photo)
imagelable.pack()
root.mainloop()