import threading
import time
amount=100

def deposit():
    global amount

    for i in range(100000):
        amount+=10

def paybill():
    global amount
    for i in range(100000):
        amount-=10

thread1= threading.Thread(target=deposit, args= ())
thread2= threading.Thread(target=paybill, args= ())

thread1.start()
thread1.join()
thread2.start()


print(amount)

# The above condition will enter race off condition at any time and that can give eronous output
# hence locks are introduced to have synchronous threads below is the example code.

lock= threading.Lock()

amount=100

def deposit():
    global amount
    lock.acquire()
    for i in range(100000):
        amount+=10
    lock.release()
def paybill():
    global amount
    lock.acquire()
    for i in range(100000):
        amount-=10
    lock.release()    

thread3= threading.Thread(target=deposit, args= ())
thread4= threading.Thread(target=paybill, args= ())

thread3.start()
thread4.start()

print(amount)