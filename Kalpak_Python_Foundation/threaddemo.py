import threading
import time

def Thread_task():
    print("Thread:Starting")
    time.sleep(1)
    print("Thread:Finishing")


if(__name__== "__main__"):
    print("Main:Staring")
    th1=threading.Thread(target=Thread_task())
    print("Main:Waiting for time to Finish Execution")
    th1.start()
    print("main:Thread Execution completed")
    print("All Done")