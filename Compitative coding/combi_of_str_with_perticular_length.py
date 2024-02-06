S, K=input().split()
S=str.upper(S)
K=int(K)
ans=[]

def conti(i,a):
    for j in range(a, len(S)):
        P=i+S[j]
        if len(P)==K:
            ans.append(P)
            break
        elif len(P)<=K-1:
            conti(P, j)
    print(ans)  
    return ans

def sort_and_Print(ans):
    ans1=["".join(sorted(u)) for u in ans]
    x=sorted(ans1)
    for i in range(len(x)):
        print(x[i])

def initiator(S, K):
    if K==1:
        for i in S:
            ans.append(i)
    else:
        for i,a in zip(S, range(len(S))):
            conti(i, a)
    sort_and_Print(ans)      
              
initiator(S, K)