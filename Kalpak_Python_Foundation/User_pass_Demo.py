import mysql.connector
import tkinter as tk
from tkinter import messagebox


db=mysql.connector.connect(host="localhost",user="root",password="",database="sample")


window=tk.Tk()
window.title("Login")

tuser=tk.StringVar()
tpass=tk.StringVar()

def getloggedinuser(uname,passw):
    qry="SELECT * FROM student WHERE semail=%s  AND password=%s"
    value=(uname,passw)
    dbcursor=db.cursor()
    dbcursor.execute(qry,value)
    stud=dbcursor.fetchone()
    return stud





def check_login():

    stud=getloggedinuser(tuser.get(),tpass.get())
    if(stud):
        messagebox.showinfo("Login :","Login Successful")

    else:
        messagebox.showerror("L`ogin-Error","Invalid Input")


def check_text():
    tuser.set("")
    tpass.set("")

f1= tk.Frame(window)
l1=tk.Label(f1,text="Username",width=10).pack(side="left")
t1=tk.Entry(f1,textvariable=tuser).pack(side="right",fill="x",expand=True)
f1.pack(side="top",fil="x",padx=5,pady=5)

f2= tk.Frame(window)
l2=tk.Label(f2,text="Password",width=10).pack(side="left")
t2=tk.Entry(f2,textvariable=tpass).pack(side="right",fill="x",expand=True)
f2.pack(side="top",fil="x",padx=5,pady=5)

f3=tk.Frame(window)
b1=tk.Button(f3,text="Login",width=15,command=check_login).pack(side="left",padx=2,ipady=5)
b2=tk.Button(f3,text="Reset",width=15,command=check_text).pack(side="left",padx=2,ipady=5)
f3.pack(side="top",fil="x",padx=5,pady=5)






window.mainloop()