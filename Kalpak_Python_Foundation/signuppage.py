import mysql.connector
import tkinter as tk
from tkinter import messagebox


db=mysql.connector.connect(host="localhost",user="root",password="",database="sample")

window=tk.Tk()
window.title("Login")

strno=tk.StringVar()
stname=tk.StringVar()
stemail=tk.StringVar()
stmobile=tk.StringVar()
stpass=tk.StringVar()



def add():
    qry="INSERT INTO student(sroll,sname,semail,number,password) VALUES(%s,%s,%s,%s,%s)"
    values=(strno.get(),stname.get(),stemail.get(),stmobile.get(),stpass.get())
    dbcursor=db.cursor()
    dbcursor.execute(qry,values)
    db.commit()
    messagebox.showinfo("Success","Successfully Added......")

def edit():
    qry="UPDATE student SET sname=%s,semail=%s,number=%s,password=%s  WHERE  sroll=%s"

    values = (stname.get(), stemail.get(), stmobile.get(), stpass.get(),strno.get())
    dbcursor = db.cursor()
    dbcursor.execute(qry, values)
    db.commit()
    messagebox.showinfo("Success","Successfully Updated......")

def delete():

    try:
        qry="DELETE FROM student WHERE  sroll="+strno.get()

        dbcursor = db.cursor()
        dbcursor.execute(qry)
        db.commit()
        messagebox.showinfo("Success","Successfully Deleted......")
    except Exception as e:
        messagebox.showerror("Error","Error while deleting..."+str(e))

def fetch():

    try:

        val=int(strno.get())
        qry="SELECT * FROM student WHERE sroll=%s"
        values = [val]
        dbcursor = db.cursor()
        dbcursor.execute(qry,values)
        student=dbcursor.fetchall()
        for std in student:
            print(std)

        messagebox.showinfo("Success","Successfully Fetched......")

    except Exception as e:
        messagebox.showerror("Error","Error while Fetching..."+str(e))





f1= tk.Frame(window)
l1=tk.Label(f1,text="Roll No",width=10).pack(side="left")
t1=tk.Entry(f1,textvariable=strno).pack(side="right",fill="x",expand=True)
f1.pack(side="top",fil="x",padx=5,pady=5)

f2= tk.Frame(window)
l2=tk.Label(f2,text="Name",width=10).pack(side="left")
t2=tk.Entry(f2,textvariable=stname).pack(side="right",fill="x",expand=True)
f2.pack(side="top",fil="x",padx=5,pady=5)


f3= tk.Frame(window)
l3=tk.Label(f3,text="Email",width=10).pack(side="left")
t3=tk.Entry(f3,textvariable=stemail).pack(side="right",fill="x",expand=True)
f3.pack(side="top",fil="x",padx=5,pady=5)

f4= tk.Frame(window)
l4=tk.Label(f4,text="mobile",width=10).pack(side="left")
t4=tk.Entry(f4,textvariable=stmobile).pack(side="right",fill="x",expand=True)
f4.pack(side="top",fil="x",padx=5,pady=5)

f5= tk.Frame(window)
l5=tk.Label(f5,text="Password",width=10).pack(side="left")
t5=tk.Entry(f5,textvariable=stpass).pack(side="right",fill="x",expand=True)
f5.pack(side="top",fil="x",padx=5,pady=5)

f6=tk.Frame(window)
b1=tk.Button(f6,text="ADD",width=15,command=add).pack(side="left",padx=2,ipady=5)
b2=tk.Button(f6,text="EDIT",width=15,command=edit).pack(side="left",padx=2,ipady=5)
b3=tk.Button(f6,text="DELETE",width=15,command=delete).pack(side="left",padx=2,ipady=5)
b4=tk.Button(f6,text="FETCH",width=15,command=fetch).pack(side="left",padx=2,ipady=5)

f6.pack(side="top",fil="x",padx=5,pady=5)

window.mainloop()