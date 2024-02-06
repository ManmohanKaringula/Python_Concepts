import time 
import threading

start=time.perf_counter()
def do_something():
    print("start sleeping")
    time.sleep(1)
    print("Done sleeping!")

threads=[]
for _ in range(10):
    thread= threading.Thread(target=do_something )
    thread.start()
    threads.append(thread)

for i in threads:
    i.join()

end=time.perf_counter()

print(f"It took {round(start-end)} seconds")



