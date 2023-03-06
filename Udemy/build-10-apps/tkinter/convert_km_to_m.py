#!/usr/bin/env python3

from tkinter import *

def km_to_miles():
    try:
        miles = float(e1_value.get()) * 0.62
        t1.delete("1.0",END)
        t1.insert(END,round(miles,2))
    except:
        t1.delete("1.0",END)
        t1.insert(END, "error")



window=Tk()
window.title("Convert Km to Miles")

b1 = Button(window,text="Convert", command = km_to_miles)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1, width=20)
t1.grid(row=0,column=2)


window.mainloop()