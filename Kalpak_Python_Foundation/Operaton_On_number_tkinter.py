import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("plus,minus,multi,div")
window.geometry("200x200")


def plus():
    num1 = float(txtnum1.get())
    num2 = float(txtnum2.get())
    c = num1 + num2
    answer.configure(text=c)

def minus():
    num1 = float(txtnum1.get())
    num2 = float(txtnum2.get())
    c = num1 - num2
    answer.configure(text=c)

def div():
    num1 = float(txtnum1.get())
    num2 = float(txtnum2.get())
    c = num1 / num2
    answer.configure(text=c)

def mult():
    num1 = float(txtnum1.get())
    num2 = float(txtnum2.get())
    c = num1 * num2
    answer.configure(text=c)



lblnum1 = tk.Label(text="number 1",width="6")
lblnum1.grid(columnspan=2,ipadx="5",ipady="5")

txtnum1 = tk.Entry(window,width="6")
txtnum1.grid(row=0,column=2,columnspan=2,ipadx="5",ipady="5")

lblnum2 = tk.Label(text="number 2",width="6")
lblnum2.grid(columnspan=2,ipadx="5",ipady="5")

txtnum2 = tk.Entry(window,width="6")
txtnum2.grid(row=1,column=2,columnspan=2,ipadx="5",ipady="5")

answer = tk.Label(window,text="-------",width="6")
answer.grid(row=3,column=1,columnspan=2,ipadx="5",ipady="5")



btnplus = tk.Button(window,text=" + ",width="3",command=plus)
btnplus.grid(row=2,column=0,ipadx="5",ipady="5")


btnminus = tk.Button(text=" - ",width="3",command=minus)
btnminus.grid(row=2,column=1,ipadx="5",ipady="5")

btnmulti = tk.Button(text=" * ",width="3",command=mult)
btnmulti.grid(row=2,column=2,ipadx="5",ipady="5")

btndiv = tk.Button(text=" / ",width="3",command=div)
btndiv.grid(row=2,column=3,ipadx="5",ipady="5")

btnresult = tk.Button(text="Result",width="3")
btnresult.grid(row=3,ipadx="5",ipady="5")




window.mainloop()