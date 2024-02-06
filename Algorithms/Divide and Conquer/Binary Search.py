# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x) 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
 
# Test array
"""arr=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    arr.append(int(input("Enter the number: ")))

print(arr)
x=int(input("Enter the number to be searched: "))
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")"""

# changes done to hack exam
A=[29,30,31,32,33] 
B=[9,10,11,12,13]

def func1(A,B,n):
    c=[]
    for i in range(1, 6):
        j=binary_search(B,0, len(B)-1, A[i])
        k=binary_search(A,0, len(A)-1, B[i])
        c[i+j]=A[i]
        c[i+k]=B[i]
    return c

print(func1(A,B,5))