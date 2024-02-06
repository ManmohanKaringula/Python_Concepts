n=int(input("Enter the number: "))
middle=n/2
if (n%2==0):
    a=n+1
    print(f"The pattern is possibe {a}")
    for i in range(a):
        for j in range(a):
            if i==0 or i==a-1:
                print("*", end=" ")
            if j==n:
                print("\n")
                
            elif 0<i<5:
                if j==0 or j==n or i==j or j==middle-i or j==middle+i or j==middle or i+j==10:
                    print("*", end=" ")
                    if j==n:
                        print("\n")
                     
                else:
                    print("", end=" ")   
                    continue 
                
            elif i==5:
                print("*", end=" ")
            
            elif 5<i<a-1:
                if j==0 or j==n or i==j or j==middle-(i-middle) or j==middle+(i-middle) or j==middle or i+j==10:
                    print("*", end=" ")
                    if j==n:
                        print("\n")
                else:
                    print("", end=" ")   
                    continue
else:
    print("The pattern is not possible")
