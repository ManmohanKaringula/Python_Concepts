def two_way_merging(A, B, n, C, i=0, j=0):
    if i<n and j<n:
        if A[i]<=B[j]:
            C.append(A[i])
            i+=1
            if i==n:
                while j<n:
                    C.append(B[j])
                    j+=1
            else:
                two_way_merging(A, B, n, C, i, j)
        elif A[i]>B[j]:
            C.append(B[j])
            j+=1
            if j==n:
                while i<n:
                    C.append(A[i])
                    i+=1
            else:
                two_way_merging(A, B, n, C, i, j)           
    return C

if __name__=='__main__':
    A=[2,5,9,12,16,19]
    B=[4,10,18,21,25,29]
    C=[]
    ans=two_way_merging(A, B, 6, C)
    print(ans)