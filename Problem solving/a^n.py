k=18 
b=1
c=int(input("Enter the number: "))
while k!=0:
    if k%2==0:
        k=k/2
        c=c*c
    else:
        k=k-1
        b=b*c

print(c)
        