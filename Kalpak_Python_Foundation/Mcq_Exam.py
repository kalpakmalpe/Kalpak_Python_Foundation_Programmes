import mysql.connector
import tkinter as tk
from tkinter import messagebox


window=tk.Tk()
window.title("EXAM")

db= mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database ="sample")
print(db)

#def question():
dbcursor=db.cursor()
qry="SELECT * FROM questions"
dbcursor.execute(qry)
records = dbcursor.fetchall()

answers={}

def getResult():

    for i in range(1, len(answers)+1):
        print(i, " ", answers[i].get())


def result():
    pass



#dbcursor = db.cursor()
#qry = "SELECT * FROM questions WHERE qst_ans="
#dbcursor.execute(qry)
#ans = dbcursor.fetchall()



for row in records:

    frame = tk.Frame(window)

    answers[row[0]] = tk.StringVar()

    lbl = tk.Label(frame, text=str(row[0])+" : "+str(row[1])).pack(side="top",  fill="x", expand=True)

    op1 = tk.Radiobutton(frame, text=str(row[2]), variable=answers[row[0]], value=1).pack(side="left")
    op2 = tk.Radiobutton(frame, text=str(row[3]), variable=answers[row[0]], value=2).pack(side="left")
    op3 = tk.Radiobutton(frame, text=str(row[4]), variable=answers[row[0]], value=3).pack(side="left")
    op4 = tk.Radiobutton(frame, text=str(row[5]), variable=answers[row[0]], value=4).pack(side="left")

    frame.pack(side='top', fill="x", padx=5, pady=5)

btnSubmit = tk.Button(window, text="Submit", command=getResult).pack(side="bottom")
btnResult = tk.Button(window, text="Result", command=result).pack(side="bottom")





window.mainloop()