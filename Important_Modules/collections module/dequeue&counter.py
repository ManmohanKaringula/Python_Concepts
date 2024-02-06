# The dequeue is double ended queue that is allows us to insert and remove elements at both ends
from collections import deque, Counter

list1=[1,2,3,4,5,6,7,8,9]
list1=deque(list1)
print(list1)
print(list1.pop()) 
print(list1.popleft())
print(list1)
print(list1.append(9))
print(list1.appendleft(9))
print(list1)

# The counter is used to count the number of similar elements and return the value
# Example:
a=[1,2,3,4,5,6,6]
print(Counter(a))
c=Counter(A=4, B=10, C=2 )
D=Counter(A=10, B=10, C=5 )
c.subtract(D)
print(c) # This is to show that counter can hava negative values....