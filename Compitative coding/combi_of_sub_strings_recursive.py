S,K=input("Enter the string and substring length limit: ").split()
S=S.upper()
K=int(K)
ans=[]
n=len(S)

def conti(i, a): # this is where the substrings are formed and a recursion is made with every substring till the limit k-1
    for b in range(a+1, n):
        aux=i+S[b]
        ans.append(aux)
        if len(aux)<=K-1:
            conti(aux, b)
    return ans

# This method is used to print the final substrings is a alphabetic order ex:["BA", "QH", "CBA"]==["AB", "HQ", "ABC"]
def Sort_and_print(ans):
    ans1=["".join(sorted(u)) for u in ans]
    x=sorted(ans1)
    for b in range(1, K+1):
        for cc in x:
            if len(cc)==b:
                print(cc)

def initiator(S,K):    # To understand this program first look at this function....
    for i,a in zip(S, range(n)):
        ans.append(i)
        if K>1:
            conti(i, a)  # The method conti is called for every corresponding i and a values           
        else:
            continue
    Sort_and_print(ans) # used for sorting the ans alphabetically and in length order.

initiator(S, K) 



