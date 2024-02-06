#Implementing stack ADT using list datatype
"""Stack ADT follows the "Last-In First-out" paradigm where the element entered last will pop first, the
   element entered first will pop last
"""
stack=[1,2,3,6,12,14]
# the append method adds the element at last index 
stack.append(27)
print(stack)
stack.append(455)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)



