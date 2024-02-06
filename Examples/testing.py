import threading
import time
# global variable x
x = 0
lock=threading.Lock()
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
  
def thread_task():
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()
  
def main_task():
    global x
    # setting global variable x as 0
    x = 0
  
    # creating threads
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)
  
    # start threads
    t1.start()

    t2.start()

  
    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    start= time.time()
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))
    end=time.time()
    print(f"The whole execution is done with in {round(end-start,2 )}")