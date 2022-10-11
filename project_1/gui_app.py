# GUI

#Libraries
#################
#1. Tkinter
#2. PyQT
#3. Turtle

import tkinter as ttk
from turtle import color

from matplotlib.pyplot import text
app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

msg=ttk.Variable(app)
print(msg.get())
msg.set('kese ho chodulund')
print(msg.get())

ttk.Label(app, text = 'chodu lund ka app').place(x=15,y=15)
ttk.Label(app,textvariable=msg).place(x=100,y=70)
def abc():
    print('papa se bakchodi ni')
    msg.set('chodu lund ka papa')
ttk.Button(app,text='isko click kr',command=abc).place(x=100,y=100)
ttk.Button(app,text='isko kr k dekh', command=lambda:msg.set('chodu lund ki mummy')).place(x=100,y=130)
    











app.mainloop()

