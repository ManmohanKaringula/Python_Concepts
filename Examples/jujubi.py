
n=input("Enter the name: ")
s=[]
for i in n:
    j=ord(i)-64
    print(f"The alphabet {i} is at position: {j}")
    s.append(j)

print(f'The total sum for the alphabet position is : {sum(s)}')

