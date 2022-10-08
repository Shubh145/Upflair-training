# GUI

#Libraries
#################
#1. Tkinter
#2. PyQT
#3. Turtle

import tkinter as ttk

from matplotlib.pyplot import text
app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

ttk.Label(app, text = 'top left dekh').place(x=250,y=170)
ttk.Label(app, text = 'top right dekh').place(x=10,y=10)
ttk.Label(app, text = 'abey just niche dekh').place(x=450,y=10)
ttk.Label(app, text = 'bottom left dekh').place(x=450,y=350)
ttk.Label(app, text = 'bhag Chodu Lund').place(x=10,y=350)









app.mainloop()

