def main():
    
    n=int(input("Enter the input: "))

    for i in range(0,n): 
        print(" "*((n-i)-1) + "*"*(i+1)+"*"*(i))
       
# To print lower half of the triangle.       
    s=n-1
    for i in range(s,0,-1):
        print(" "*(s-(i-1))+"*"*(i)+"*"*(i-1)) 

main()