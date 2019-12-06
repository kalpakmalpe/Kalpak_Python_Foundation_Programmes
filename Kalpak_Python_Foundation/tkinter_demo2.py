import tkinter


window=tkinter.Tk()
window.title("Login")


frame1=tkinter.Frame(window).grid(row=0)
frame2=tkinter.Frame(window).grid(row=1)

lblusername=tkinter.Label(frame1,text="Username").grid(row=0,column=0)
lblpassword=tkinter.Label(frame1,text="Password").grid(row=1,column=0)
txtusename=tkinter.Entry(frame1).grid(row=0,column=1)
txtusename=tkinter.Entry(frame1).grid(row=1,column=1)
btnlogin=tkinter.Button(frame1,text="Login").grid(row=2,column=1)

l1=tkinter.Label(frame2,text="This is for Message").grid(row=3)

window.mainloop()
