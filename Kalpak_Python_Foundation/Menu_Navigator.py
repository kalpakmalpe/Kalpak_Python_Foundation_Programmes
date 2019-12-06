
#Menu driven operation using Tkinter


import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


window=tk.Tk()
window.title("Menu Navigator")
window.geometry("400x400")

menubar=tk.Menu(window)

text=Text(window)
text.grid()


def new_window():

    newwin=tk.Toplevel(window)
    newwin.geometry("300x300")
    menubar = tk.Menu(newwin)

    mnufile = tk.Menu(menubar, tearoff=0)
    mnufile.add_command(label="New", command=new_window)
    mnufile.add_command(label="Open")
    mnufile.add_command(label="Save", command=saveas)
    mnufile.add_separator()
    mnufile.add_command(label="Exit",command=quitApplication)
    menubar.add_cascade(label="File", menu=mnufile)

    mnuedit = tk.Menu(menubar, tearoff=0)
    mnuedit.add_command(label="Undo")
    mnuedit.add_separator()
    mnuedit.add_command(label="Cut ")
    mnuedit.add_command(label="Copy")
    mnuedit.add_command(label="Paste")
    mnuedit.add_command(label="Delete")
    menubar.add_cascade(label="Edit", menu=mnuedit)

    mnuformat = tk.Menu(menubar, tearoff=0)
    mnuformat.add_command(label="Word Wrap")
    mnuformat.add_command(label="Font..")
    menubar.add_cascade(label="Format", menu=mnuformat)

    mnuview = tk.Menu(menubar, tearoff=0)
    mnuview.add_command(label="Zoom")
    mnuview.add_command(label="Status Bar")
    menubar.add_cascade(label="View", menu=mnuview)

    mnuhelp = tk.Menu(menubar, tearoff=0)
    mnuhelp.add_command(label="View Help")
    mnuhelp.add_command(label="Send Feedback")
    mnuhelp.add_separator()
    mnuhelp.add_command(label="About Notepad")
    menubar.add_cascade(label="Help", menu=mnuhelp)

    txt=Text(newwin)
    txt.grid()
    newwin.configure(menu=menubar)
    newwin.mainloop()


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def quitApplication():
    window.destroy()


def openfile():
    global text
    t = text.get("1.0", "end-1c")
    file=filedialog.askopenfilename(initialfile='Untitled.txt',  defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

    if file=="":
        file = None
    else:
        window.title(os.path.basename(file)+"Notepad")
        text.__thisTextArea.delete("1.0", END)

        file = open(file, "r")

        text.__thisTextArea.insert("1.0", file.read())

        file.close()



mnufile=tk.Menu(menubar,tearoff=0)
mnufile.add_command(label="New",command=new_window)
mnufile.add_command(label="Open",command=openfile)
mnufile.add_command(label="Save",command=saveas)
mnufile.add_separator()
mnufile.add_command(label="Exit",command=quitApplication)
menubar.add_cascade(label="File",menu=mnufile)


mnuedit=tk.Menu(menubar,tearoff=0)
mnuedit.add_command(label="Undo")
mnuedit.add_separator()
mnuedit.add_command(label="Cut ")
mnuedit.add_command(label="Copy")
mnuedit.add_command(label="Paste")
mnuedit.add_command(label="Delete")
menubar.add_cascade(label="Edit",menu=mnuedit)


mnuformat=tk.Menu(menubar,tearoff=0)
mnuformat.add_command(label="Word Wrap")
mnuformat.add_command(label="Font..")
menubar.add_cascade(label="Format",menu=mnuformat)


mnuview=tk.Menu(menubar,tearoff=0)
mnuview.add_command(label="Zoom")
mnuview.add_command(label="Status Bar")
menubar.add_cascade(label="View",menu=mnuview)

mnuhelp=tk.Menu(menubar,tearoff=0)
mnuhelp.add_command(label="View Help")
mnuhelp.add_command(label="Send Feedback")
mnuhelp.add_separator()
mnuhelp.add_command(label="About Notepad")
menubar.add_cascade(label="Help",menu=mnuhelp)
















window.configure(menu=menubar)
window.mainloop()
