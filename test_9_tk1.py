from Tkinter import *
root = Tk()

c = Canvas(root, width = 200, height = 200)

c.create_rectangle(50, 50, 150, 150, fill = 'yellow')
c.create_oval(50, 50, 150, 150, fill = 'green')
c.create_line(0, 0, 200, 200, fill = 'red')
c.create_line(0, 200, 200, 0, fill = 'red')
c.create_text(100, 180, text = 'Tkinter Canvas', fill = 'blue')

c.pack()
mainloop()