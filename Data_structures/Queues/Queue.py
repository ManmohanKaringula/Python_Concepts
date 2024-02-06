"""Queue works on the principle of “First-in, first-out”. Below is list implementation of queue. We use pop(0) 
    to remove the first item from a list.
"""
# Note: The queue ADT has one end for insertion and other end for removel in our case the list is used therefore
# the index 0 is used for pop and index (size_of) last is used for insertion. 
queue=[1,2,3,4,5,6]
queue.append(7)
print(queue)
queue.append(8)
print(queue)
# The append function inserts the element at the end 
# The queue ADT pops the element at starting  of the list since the element at the begining are added first
# (First-In First-out) therefore we added the 0 index in pop function we get the value that is first added
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)