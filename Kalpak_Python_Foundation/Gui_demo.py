#Operation On tkinter

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("My First Window")
window.geometry("200x200")

def on_btn_click():
    #print("Button Clicked")
    messagebox.showwarning("Info", "Button Clicked")

def change_text():
    lbl.config(text="Text Changed")

def get_radio_value():
    messagebox.showwarning("Info", "You have selected : "+str(v.get()))

def get_checked_value():
    messagebox.showinfo("Info", "Male : "+str(v1.get()) + " , Female : " + str(v2.get()))

'''
l1 = tkinter.Label(window,text="This is Label Top", bg="red")
l1.pack(fill="x")

l2 = tkinter.Label(window,text="This is Left", bg="yellow")
l2.pack(side="left", fill="y")

l3 = tkinter.Label(window,text="This is Right", bg="green")
l3.pack(side="right", fill="y")

l4 = tkinter.Label(window,text="This is Bottom", bg="blue", fg="white")
l4.pack(side="bottom", fill="x")
'''
v1 = tk.IntVar()
v2 = tk.IntVar()
rd1 = tk.Checkbutton(window, text="Male", variable=v1).pack()
rd2 = tk.Checkbutton(window, text="Female", variable=v2).pack()
btnCheck = tk.Button(window, text="Get Checked Value", command=get_checked_value).pack()

v = tk.IntVar()
v.set(1)
cd1 = tk.Radiobutton(window, text="Option 1", variable=v, value=1).pack()
cd2 = tk.Radiobutton(window, text="Option 2", variable=v, value=2).pack()
btnRadio = tk.Button(window, text="Get Selected Radio Value", command=get_radio_value).pack()

lbl = tk.Message(window, text="This is message widget. Its is a advanced Lable which can show rich text!")
lbl.config(bg="lightgreen", font=('Times new Roman',14,'italic'))
lbl.pack();


btn1 = tk.Button(window, text="Show", command=on_btn_click).pack()
btn2 = tk.Button(window, text="Change", command=change_text).pack()


window.mainloop()
