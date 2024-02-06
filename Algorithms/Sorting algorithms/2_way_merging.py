
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

if __name__=="__main__":
    A=[2,4,9,12,16,19]
    B=[4,10,18,21,25,29]
    ans=two_way_merging(A, B, 6)
    print(ans)
    
    
