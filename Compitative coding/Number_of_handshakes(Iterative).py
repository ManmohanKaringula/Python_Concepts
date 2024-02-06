def NumOfHS(n):
    HS=0
    for i in range(n-1,0,-1):
        if i==1:
            HS+=1

        else:
            for j in range(i,0,-1):
                HS+=1
    return HS  

N=int(input("Enter the number of people:"))
print(f'The total number of hand shakes are: {NumOfHS(N)}')