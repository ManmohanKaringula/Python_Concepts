import threading
import time

def does_something(x, i):
    print(f"The thread {i} is about to sleep")
    time.sleep(2)
    print(f"The thread {i} is done sleeping")


threads=[]
start= time.time()
for i in range(10):
    thread= threading.Thread(target=does_something, args=[2, i])
    thread.start()
    threads.append(thread)

for j in threads:
    j.join()
end=time.time()

print(f"All in all the threads took {round(end-start, 2)} seconds to complete the execution")


