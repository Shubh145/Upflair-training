# GUI

#Libraries
#################
#1. Tkinter
#2. PyQT
#3. Turtle

import tkinter as ttk
from turtle import color

from matplotlib.pyplot import show, text
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


f1=ttk.Variable(app)
f1.set('0')
f2=ttk.Variable(app)
f2.set('0')
result=ttk.Variable(app)

ttk.Entry(app,textvariable=f1,width=5,font=('Arial',22)).place(x=50,y=200)
ttk.Entry(app,textvariable=f2,width=5,font=('Arial',22)).place(x=150,y=200)
ttk.Label(app,text='Result').place(x=100,y=300)
ttk.Label(app,textvariable=result,font=('Ariel,22')).place(x=100,y=330)

def calci(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app,text='+',command=lambda:calci('+'),font=('Arial',22)).place(x=50,y=240)
ttk.Button(app,text='-',command=lambda:calci('-'),font=('Arial',22)).place(x=100,y=240)
ttk.Button(app,text='*',command=lambda:calci('*'),font=('Arial',22)).place(x=150,y=240)
ttk.Button(app,text='/',command=lambda:calci('/'),font=('Arial',22)).place(x=200,y=240)


box=ttk.Listbox(app,height=5,fg='red',activestyle='dotbox')
box.insert(1,'Sample1')
box.insert(1,'Sample2')
box.insert(1,'Sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))
ttk.Button(app,text='show',command=show).place(x=350,y=250)





app.mainloop()