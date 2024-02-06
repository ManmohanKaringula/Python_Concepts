import threading
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
thread2.start()



print(amount)

# The above condition will enter race off condition at any time and that can give eronous output
# hence locks are introduced to have synchronous threads below is the example code.

lock1= threading.Lock()

amount1=100

def deposit1():
    global amount1
    lock1.acquire()
    for i in range(100000):
        amount1+=10
    lock1.release()
def paybill1():
    global amount1
    lock1.acquire()
    for i in range(100000):
        amount1-=10
    lock1.release()    

thread3= threading.Thread(target=deposit1, args= ())
thread4= threading.Thread(target=paybill1, args= ())

thread3.start()
thread3.join()
thread4.start()
thread4.join()

print(amount1)