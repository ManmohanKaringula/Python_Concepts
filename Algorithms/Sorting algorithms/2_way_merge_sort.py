def merging(X):
    Y=[]
    A,B=[],[]
    if len(X)%2==0:
        for i in range(0, (len(X)), 2):
            while len(X)>1:
                A.append(X[i])
                B.append(X[i+1])
                two_way_merging(A, B, len(A))
        
            

    else:
        for i in range(0, (len(X)), 2):


    


    return Y

def two_way_merging(A, B, n):
    i,j =0, 0
    C=[]
    while i<n and j<n:
        if A[i]<=B[j]:
                C.append(A[i])
                i+=1 
                continue
        elif A[i]>B[j]:
                C.append(B[j])
                j+=1
    if i==n:
        while j<n:
            C.append(B[j])
            j+=1
    elif j==n:
        while i<n:
            C.append(A[i])
            i+=1
    return C


