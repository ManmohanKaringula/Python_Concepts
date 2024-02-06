S,K = input("Enter the string and substring length limit: ").split()
S=S.upper()
K=int(K)
ans=[]
n=len(S)
b=1




def initiator(S,K):
    for i, a in zip(S, range(n)):
        ans.append(i)
        cc=[]
        while len(i)<K: