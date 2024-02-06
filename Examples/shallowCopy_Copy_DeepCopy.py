""" In shallow copy the variable which copies the value from the variable can change both the value of itself and the
value of the variable from which it is copied """
import copy
a=12
b=a
b=234
print(a) # 12
print(b) # 234, 
"""Hence this is not a shallow copy of the variable and it is the deep copy where the variables has their own reference"""

# lets look at an array object

arr1=[[1,1,1], [2,2,2], [3,3,3]]
arr2=arr1

arr2.append([4,4,4])
print(arr2) # Output: [[1,1,1], [2,2,2], [3,3,3], [4,4,4]]
print(arr1) # Output: [[1,1,1], [2,2,2], [3,3,3], [4,4,4]]
"""Hence from the above output it can be said that arr2 and arr1 are in shallow copy"""

# In order to make a perfect copy like variables "a" and "b" we can use the copy moduels copy and deepcopy methods...

arr3=copy.copy(arr1)
arr3.append([5,5,5])
print(arr1) # Output: [[1,1,1], [2,2,2], [3,3,3], [4,4,4]]
print(arr3) # Output: [[1,1,1], [2,2,2], [3,3,3], [4,4,4], [5,5,5]]
"""Hence from the above output we can say that the variable arr3 is the copy of the varible of the arr1 """

# deep copy for the nested elements where the copy method does'nt work...

arr3[2][1]="Apple"
print(arr3) # Output: [[1,1,1], [2,2,2], [3, 'Apple', 3], [4,4,4], [5,5,5]]
print(arr1) # Output: [[1,1,1], [2,2,2], [3, 'Apple', 3], [4,4,4]]
"""Hence from the above output the copy() method doesn't work with nested(in position) methods....."""

# Using the deepcopy method for creting copies with nested elments.....
arr4=copy.deepcopy(arr1)
arr4[0][0]="Pineapple"
print(arr4) # Output: [['pineapple', 1, 1], [2, 2, 2], [3, 'Apple', 3], [4, 4, 4]]
print(arr1) # Output: [[1, 1, 1], [2, 2, 2], [3, 'Apple', 3], [4, 4, 4]]
"""Hence from the above change in nested element in arr4 we can say that it is not effected in the arr1 by using the 
deepcopy() method.... """




