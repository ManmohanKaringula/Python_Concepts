
import threading
import time
from datetime import datetime

# This program also shows that the threads are concurrent
# The below code is synchronous 
def thread1():
    now =datetime.now().time()
    for i in range(0,2):
        print(f"\nThis is first thread {now} {time.time_ns()} \n")
        print(i*i)
        time.sleep(1)
        
def thread2():
    now =datetime.now().time()
    for j in range(0,2):
        print(f"\nThis is second thread {now} {time.time_ns()}\n")
        print(j*j)
        time.sleep(1)

x=threading.Thread(target=thread1)
y=threading.Thread(target=thread2)

start= time.time()
x.start()
x.join()   #ImpNote: Put this line between two thread when you want to make the threads synchronous which will definitely 
y.start()  # not be as performant as the asynchronous multithreading...
y.join()

print(f"The threads completed both the executions in {round(time.time()-start, 2)}")


# The below code is asynchronous

def Thread1():
    now =datetime.now().time()
    for i in range(0,2):
        print(f"\nThis is first thread {now} {time.time_ns()} \n")
        print(i*i)
        time.sleep(1)
        

def Thread2():
    now =datetime.now().time()
    for j in range(0,2):
        print(f"\nThis is second thread {now} {time.time_ns()}\n")
        print(j*j)
        time.sleep(1)

a=threading.Thread(target=Thread1)
b=threading.Thread(target=Thread2)

start1= time.time()
a.start()
# Here the important note is that since the join() is not mentioned the thread act in asynchronous way there is interruption 
b.start()  

a.join() # including join() method after the start() methods are called for every thread inorder to avoid synchronous thread. 
b.join()

print(f"The threads completed both the executions in {round(time.time()-start1, 2)}")
# ImpNote: Since this is asynchronous the speed of execution is faster than the synchronous, but as you can see there are race
# of conditions hence locks are introduced in multithreading...
