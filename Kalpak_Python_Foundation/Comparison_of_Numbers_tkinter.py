#Comparision of Numbers


import tkinter as tk

window=tk.Tk()
window.title("Compare numbers")
window.geometry("300x300")


def btn_largest():
    num1=txtno1.get()
    num2=txtno2.get()
    num3=txtno3.get()

    if (num1 > num2) and (num1 > num3):
        answer.configure(text=num1)

    elif (num2 > num3) and (num2 > num3):
        answer.configure(text=num2)
    else:
        answer.configure(text=num3)


def btn_smallest():
    num1 = txtno1.get()
    num2 = txtno2.get()
    num3 = txtno3.get()
    if (num1 < num2) and (num2 < num3):
        answer.configure(text=num1)

    elif (num2 < num3)and (num2 < num3):
        answer.configure(text=num2)
    else:
        answer.configure(text=num3)


lblno1 = tk.Label(text="NO1",width="6")
lblno1.grid(columnspan=2,ipadx="5",ipady="5")

lblno2 = tk.Label(text="NO2",width="6")
lblno2.grid(columnspan=2,ipadx="5",ipady="5")

lblno3 = tk.Label(text="NO3",width="6")
lblno3.grid(columnspan=2,ipadx="5",ipady="5")

txtno1 = tk.Entry(window,width="6")
txtno1.grid(row=0,column=2,columnspan=2,ipadx="5",ipady="5")

txtno2 = tk.Entry(window,width="6")
txtno2.grid(row=1,column=2,columnspan=2,ipadx="5",ipady="5")


txtno3 = tk.Entry(window,width="6")
txtno3.grid(row=2,column=2,columnspan=2,ipadx="5",ipady="5")

btnlarge = tk.Button(window,text=" LARGEST",width="3",command=btn_largest)
btnlarge.grid(row=3,column=0,ipadx="5",ipady="5")

btnsmall = tk.Button(text="SMALLEST",width="3",command=btn_smallest)
btnsmall.grid(row=3,column=1,ipadx="5",ipady="5")

answer = tk.Label(window,text="-------",width="6")
answer.grid(row=4,column=1,columnspan=2,ipadx="5",ipady="5")









window.mainloop()
