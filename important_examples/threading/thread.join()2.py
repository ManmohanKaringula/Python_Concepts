# Daemon thread: A daemon thread is a low priority thread which executes in the background the main thread doesn't wait
# for the daemon thread to execute completely it, the main thread just leaves the thread once it gets completed..
 

import time
import threading


def func1():
    print("The thread starts sleeping now")
    time.sleep(10)
    print("The thread is done sleeping")

thread1= threading.Thread(target=func1)
thread1.setDaemon(True) # Syntax to create a daemon thread in python
thread1.start()
thread1.join() 

# the join() method is used so the daemon thread is not left inbetween of execution my the main thread 
# In simple words the .join() method takes care of completion of the daemon threads...  
