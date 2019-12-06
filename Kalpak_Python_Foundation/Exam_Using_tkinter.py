#Check the Answers Using tkinter

import tkinter as tk

window=tk.Tk()
window.title("Exam Form")
window.geometry("400x400")


def check_ans():
    a=v.get()






f1= tk.Frame(window)
v=tk.IntVar()

l1=tk.Label(f1,text="1) 2+2=.....",width=10).grid(row=0,columnspan=4)
o1=tk.Radiobutton(f1,text="3",variable=v,value=1).grid(row=1,column=0,ipadx="5",ipady="5")
o2=tk.Radiobutton(f1,text="4",variable=v,value=2).grid(row=1,column=1,ipadx="5",ipady="5")
o3=tk.Radiobutton(f1,text="5",variable=v,value=3).grid(row=2,column=0,ipadx="5",ipady="5")
o4=tk.Radiobutton(f1,text="6",variable=v,value=4).grid(row=2,column=1,ipadx="5",ipady="5")
f1.pack(side="top",fil="x",padx=5,pady=5)

f2= tk.Frame(window)
v=tk.IntVar()
l2=tk.Label(f2,text="2) 2*2=.....",width=10).grid(row=0,columnspan=4)
l21=tk.Radiobutton(f2,text="3",variable=v,value=1).grid(row=1,column=0,ipadx="5",ipady="5")
l22=tk.Radiobutton(f2,text="4",variable=v,value=2).grid(row=1,column=1,ipadx="5",ipady="5")
l33=tk.Radiobutton(f2,text="5",variable=v,value=3).grid(row=2,column=0,ipadx="5",ipady="5")
l44=tk.Radiobutton(f2,text="6",variable=v,value=4).grid(row=2,column=1,ipadx="5",ipady="5")
f2.pack(side="top",fil="x",padx=5,pady=5)

f3= tk.Frame(window)
v=tk.IntVar()
l3=tk.Label(f3,text="3) 3*3=.....",width=10).grid(row=0,columnspan=4)
w1=tk.Radiobutton(f3,text="3",variable=v,value=1).grid(row=1,column=0,ipadx="5",ipady="5")
w2=tk.Radiobutton(f3,text="4",variable=v,value=2).grid(row=1,column=1,ipadx="5",ipady="5")
w3=tk.Radiobutton(f3,text="9",variable=v,value=3).grid(row=2,column=0,ipadx="5",ipady="5")
w4=tk.Radiobutton(f3,text="6",variable=v,value=4).grid(row=2,column=1,ipadx="5",ipady="5")
f3.pack(side="top",fil="x",padx=5,pady=5)

f4= tk.Frame(window)
v=tk.IntVar()
l4=tk.Label(f4,text="4) 5*5=.....",width=10).grid(row=0,columnspan=4)
q1=tk.Radiobutton(f4,text="30",variable=v,value=1).grid(row=1,column=0,ipadx="5",ipady="5")
q2=tk.Radiobutton(f4,text="25",variable=v,value=2).grid(row=1,column=1,ipadx="5",ipady="5")
q3=tk.Radiobutton(f4,text="10",variable=v,value=3).grid(row=2,column=0,ipadx="5",ipady="5")
q4=tk.Radiobutton(f4,text="35",variable=v,value=4).grid(row=2,column=1,ipadx="5",ipady="5")
f4.pack(side="top",fil="x",padx=5,pady=5)








window.mainloop()
