# an enumerate() function return the enumerate object

list1=[1,2,3,3,4,6,7,9]
e=enumerate(list1)
print(e) # it will print the object type and its location 

a=list(e)
print(a)

list2=[200,300,400, 500, 600, 700, 800, 900]
b=enumerate(list1) # we can also set user defined start index...
print(list(b))
