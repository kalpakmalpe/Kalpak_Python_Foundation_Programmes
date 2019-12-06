import tkinter
from tkinter import *

window=tkinter.Tk()
window.title("Calculator")
#window.resizable(500,500)

#frame1=tkinter.Frame(window).grid(row=0)
#frame2=tkinter.Frame(window).grid(row=1)
expression=""

def btn_click(item):
    global expression

    expression=expression + str(item)
    input_txt.set(expression)


def btn_clear():
    global expression
    expression=""
    input_txt.set("")

def btn_equal():
    global expression
    result=str(eval(expression))
    input_txt.set(result)
    expression=""




input_txt= StringVar()

txtno=tkinter.Entry(bg="grey",textvariable=input_txt).grid(columnspan=4,sticky="n,s,e,w",ipadx="5",ipady="5")


seven=tkinter.Button(text=" 7",bg="black",fg="white",width='5',command=lambda:btn_click(7)).grid(row=1,column=0)
eight=tkinter.Button(text="8",bg="black",fg="white",width='5',command=lambda:btn_click(8)).grid(row=1,column=1)
nine=tkinter.Button(text="9",bg="black",fg="white",width='5',command=lambda:btn_click(9)).grid(row=1,column=2)
plus=tkinter.Button(text="+",bg="black",fg="white",width='5',command=lambda:btn_click("+")).grid(row=1,column=3)

four=tkinter.Button(text="4",bg="black",fg="white",width='5',command=lambda:btn_click(4)).grid(row=2,column=0)
five=tkinter.Button(text="5",bg="black",fg="white",width='5',command=lambda:btn_click(5)).grid(row=2,column=1)
six=tkinter.Button(text="6",bg="black",fg="white",width='5',command=lambda:btn_click(6)).grid(row=2,column=2)
minus=tkinter.Button(text="-",bg="black",fg="white",width='5',command=lambda:btn_click("-")).grid(row=2,column=3)


one=tkinter.Button(text="1",bg="black",fg="white",width='5',command=lambda:btn_click(1)).grid(row=3,column=0)
two=tkinter.Button(text="2",bg="black",fg="white",width='5',command=lambda:btn_click(2)).grid(row=3,column=1)
three=tkinter.Button(text="3",bg="black",fg="white",width='5',command=lambda:btn_click(3)).grid(row=3,column=2)
mult=tkinter.Button(text="*",bg="black",fg="white",width='5',command=lambda:btn_click("*")).grid(row=3,column=3)

zero=tkinter.Button(text="0",bg="black",fg="white",width='5',command=lambda:btn_click(0)).grid(row=4,column=0)
dot=tkinter.Button(text="C",bg="black",fg="white",width='5',command=lambda:btn_clear()).grid(row=4,column=1)
blank=tkinter.Button(text="=",bg="black",fg="white",width='5',command=lambda:btn_equal()).grid(row=4,column=2)
divide=tkinter.Button(text="/",bg="black",fg="white",width='5',command=lambda:btn_click("/")).grid(row=4,column=3)





window.mainloop()
