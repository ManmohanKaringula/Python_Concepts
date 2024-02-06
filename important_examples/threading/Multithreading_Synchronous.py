# since this is a synchronous program it will take more time to execute than the asynchonous program....

from concurrent.futures import thread
import threading
import time

def does_something(x, i):
    print(f"The {i} thread is about to sleep")
    time.sleep(x)
    print("Done sleeping")


start = time.time()
for i in range(10):
    thread=threading.Thread(target=does_something, args=[2, i])
    thread.start()
    thread.join()  # this line makes the threads to act in a synchronous way

end= time.time()

print(f"All in all the total time taken by the threads to complete the task is {round(end-start,2)} since they are synchronous")
# It will take around 20 seconds for the threads to execute since they are synchronous the next 
