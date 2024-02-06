
import threading
import time

def thread1():
    for i in range(1, 10):
        print(i)
def thread2():
    for j in range(1, 13):
        print(j)

x=threading.Thread(target=thread1)
y=threading.Thread(target=thread2)
x.start()

y.start()