
import threading

x=[1,2,3,4,5]

def first():
    for i in range(5):
        a=x[i]
        b=a*a    
        x[i]=b
        

first()
print(x)