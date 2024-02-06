import time
import threading

start=time.perf_counter()
def does_something(x):
    print("Let the thread sleep\n")
    time.sleep(x)
    print("The thread is done sleeping\n")

thread1=threading.Thread(target=does_something, args=(3,))
thread2=threading.Thread(target=does_something, args=(2,))

thread1.start()

thread2.start() # Since there is no .join() method the main thread will not wait for the threads completion and start to 
# execute print statement...


end=time.perf_counter()
print(f'The threads are executed in {round(end-start, 2)}')
print("\n")

# Example:

start2=time.perf_counter()
def does_something(x):
    print("Let the thread sleep \n")
    time.sleep(x)
    print("The thread is done sleeping \n")

thread3=threading.Thread(target=does_something, args=(3,))
thread4=threading.Thread(target=does_something, args=(2,))

thread3.start()
thread4.start() 

thread3.join()
thread4.join()

end2=time.perf_counter()
print(f'The threads are executed in {round(end2-start2, 2)}') # The print() statement is not executed until the threads are
# executed completely since the join() function is called for each thread...

