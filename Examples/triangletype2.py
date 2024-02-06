def triangle(n):
    for i in range(0, n):
        print(" "*((n-i)-1) + "5"  +" 5"*(i))

n=int(input("Enter the number of lines: "))
triangle(n)



