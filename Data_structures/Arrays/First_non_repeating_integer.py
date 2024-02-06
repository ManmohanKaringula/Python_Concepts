from array import array

def first_non_repeating_Integer(b):
    for i in range(len(b)):
        x, j = b[i],0
        while j<=len(b)-1:
            if b[j]==x and j!=i:
                break
            j+=1
        if j==len(b)-1:
            print(f"The first non repeating integer in the array is: {x}")
        elif i==len(b)-1 and j!=len(b)-1:
            print("There is no non repeating integer")
        
n=int(input("Enter the number of elements: "))
a=[int(input("Enter the element: ")) for i in range(n)]
b=array('i', a)
first_non_repeating_Integer(b)




            
            
        



