import threading
import time
import os

global lst
lst=[]

def read():
    print("creating the list.")
    for i in range(10):
        lst.append(i)

    print("list is completed")

def display():
    print("Display the list")
    #for i in range(10):
    print(lst)



if(__name__== "__main__"):
    print("Main:Staring")
    th1=threading.Thread(target=read())
    th2=threading.Thread(target=display())

    th1.start()
    th2.start()

    th1.join()
    th2.join()