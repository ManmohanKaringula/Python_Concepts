import math
A=[4,5,6,7,8,9,2,1]
B=[]
def AlgorithmA( A, n=len(A)):
    for i in range(1, n):
        B[i] = A[i] 
    for h in range(1, math.log2(n)):
        for i in range(1, n/2^h):
            if(B[2*i - 1] >= B[2*i]):
                B[i] = B[2*i-1]
            else:
                B[i] = B[2*i-1]

    return B[1]
AlgorithmA(A)
