#Multi_Threading

import threading
import time
import os

def Thread_task():
    print("Thread:",threading.current_thread().name ,"Starting")
    print("Process id:",os.getppid())
    time.sleep(1)
    print("Thread:",threading.current_thread().name ,"Finishing...")


if(__name__== "__main__"):
    print("Main:Staring")
    th1=threading.Thread(target=Thread_task(),name="Thread one")
    th2=threading.Thread(target=Thread_task(),name="Thread Two")

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("Main thread:Finishing...")
    
