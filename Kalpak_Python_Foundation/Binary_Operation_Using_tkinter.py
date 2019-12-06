import tkinter as tk
from tkinter import *
window=tk.Tk()

window.title("binary")
window.geometry("200x100")

def add():
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 + num2
    t3.insert(END, str(result))


lblno1=tk.Label(window,text="NO-1").grid(row=0,column=0)
lblno2=tk.Label(window,text="NO-2").grid(row=1,column=0)

txtno1=tk.Entry(window).grid(row=0,column=1)
txtno2=tk.Entry(window).grid(row=1,column=1)


btnplus=tk.Button(window,text="+",width="5",command=add).grid(row=3,column=0)
btnminus=tk.Button(window,text="-",width="5" ,justify="center").grid(row=3,column=1)
btnmult=tk.Button(window,text="*",width="5").grid(row=3,column=2)
btndiv=tk.Button(window,text="/",width="5").grid(row=3,column=3)

result=tk.Button(window,text="RESULT",width="5").grid(row=4)
#resultminus.bind('<Button-1>', self.sub)


t1 = tk.IntVar()
t2 = tk.IntVar()
t3=Entry()





window.mainloop()