# the _thread module is depricated with the release of python 3, now we use threading module
# here in this example we use _thread module


import _thread
import time

def thread_test(name, wait):
    i=0
    while(i<=3):
        time.sleep(wait)
        print(f"This {name} thread running currently")
        i=i+1
    print(f"The {name} thead completed its execution")

if __name__=="__main__":
    _thread.start_new_thread(thread_test, ("first thread", 1))
    _thread.start_new_thread(thread_test, ("second thread", 2))
    _thread.start_new_thread(thread_test, ("third thread", 3))

