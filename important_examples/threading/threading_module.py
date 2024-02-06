import time
import threading
lock=threading.Lock()
class threadtester(threading.Thread):
    def __init__(self, id, name, i):
        threading.Thread.__init__(self)
        self.id=id
        self.name=name
        self.i=i

    def run(self):
        lock.acquire()
        thread_test(self.name, self.i, 5)
        print(f"{self.name} has finished execution")
        lock.release()

def thread_test(name, wait, i):
    while i:
        time.sleep(wait)
        print(f"Running {name} \n")
        i=i-1

if __name__=="__main__":
    thread1= threadtester(1, "First Thread", 1)
    thread2= threadtester(2, "second Thread", 2)
    thread3= threadtester(3, "Third Thread", 3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("hello this is manmohan in the main thread tyring to run the main thread before the sub threads are completed")
    print("this  some bullshit code just for the purose of testing")

    i=5
    while i>=0:
        print("manmohan never give up man")
        i-=1


