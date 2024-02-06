from math import *
List=[]
a=int(input("Enter any number:  "))
b=2
c=floor(a/b)

for i in range(1,c+1):
    if a%i==0:
        
        List.append(i)

print(List)



