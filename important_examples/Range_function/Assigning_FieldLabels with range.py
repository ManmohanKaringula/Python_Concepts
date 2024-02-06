# We can assign field names to the numbers which are used to subscript. The range funciton helps us to do this.....

a=["manmohan", 23432,23]
Name, Pay, Age= range(3)  # We are assigning field names to 0,1,2 to the range funciton 

print(a[Pay])

l=[["vishnu", 15000,21],["kiran", 20000, 20],["ajith", 40000, 23]]

print(l[0][Pay])
print(l[Name][Pay])  # problems with the field names