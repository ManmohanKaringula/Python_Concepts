A=[3, 7, 8,  5,   9,  4, 2,  6 ]
low=0
high=7
def func1(A, low, high):
    i=-1
    x=A[high]
    for j in range(low, high):
        if A[j]<=x:
            i=+1
            A[i],A[j]=A[j], A[i]
            A[i+1], A[high]=A[high], A[i+1]
    return i+1

print(func1(A,low, high))