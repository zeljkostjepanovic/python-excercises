from tkinter import *
import tkinter.font as tk_font
from tkinter import ttk

def kg_to_other():
    try:
        grams = float(kg_value.get()) * 1000.00
        g1.delete("1.0", END)
        g1.insert(END,round(grams,4))
        pounds = float(kg_value.get()) * 2.20462
        p1.delete("1.0", END)
        p1.insert(END, round(pounds,4))
        ounces = float(kg_value.get()) * 35.274
        o1.delete("1.0", END)
        o1.insert(END, round(ounces,4))
    except:
        g1.delete("1.0",END)
        g1.insert(END, "error")
        p1.delete("1.0",END)
        p1.insert(END, "error")
        o1.delete("1.0",END)
        o1.insert(END, "error")


window=Tk()
window.option_add('*Font','Roboto 11')
window.title("Convert Kg to Grams, Pounds and Ounces")

t1 = Label(window, text="Input Kg:")
t1.grid(row=0,column=0)
b1 = Button(window,text="Convert", height=1, command = kg_to_other)
b1.grid(row=0,column=2)

kg_value = StringVar()
kg = Entry(window,textvariable = kg_value)
kg.grid(row=0,column=1)

separator = ttk.Separator(window,orient=HORIZONTAL).grid(row=1,column=0, columnspan=3,padx=5,pady=10,sticky=EW)

g1_label = Label(window,text="Grams")
g1_label.grid(row=2,column=0)
g1 = Text(window,height=1, width=20)
g1.insert("1.0","Grams")
g1.grid(row=3,column=0)

p1_label = Label(window, text="Pounds")
p1_label.grid(row=2,column=1)
p1 = Text(window,height=1, width=20)
p1.insert("1.0","Pounds")
p1.grid(row=3,column=1)

o1_label = Label(window, text = "Ounces")
o1_label.grid(row=2,column=2)
o1 = Text(window,height=1, width=20)
o1.insert("1.0","Ounces")
o1.grid(row=3,column=2)

window.mainloop()
