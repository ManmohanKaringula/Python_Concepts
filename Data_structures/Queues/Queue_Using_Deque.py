# Implementing the Queue ADT using Deque from collections, the deque  implementation is efficient than the 
# list implementation since the removal of least recent elements makes the other elements to move by one bit 
# therefore an effecient method is importing deque from collections which is used for same purpose as the list 
# but in an efficient way 

from collections import deque
queue = deque([1,2,3,4,5]) 
print(queue) 
queue.append(6) 
print(queue) 
queue.append(7) 
print(queue) 
#using popleft method instead of pop(0) to retrieve the element that was entered first
print(queue.popleft())                  
print(queue.popleft())                  
print(queue)
