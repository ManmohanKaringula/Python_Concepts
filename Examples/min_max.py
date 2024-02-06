
def max(x, n):
    maxn=x[0]
    for i in range(1, n):
        if(maxn < x[i]):
            maxn=x[i]
    return maxn 

def min(x, n):
    minn=x[0]
    for i in range(1, n):
        if(minn > x[i]):
            minn=x[i]
    return minn

x=[]
n=int(input("Enter the number of elements: "))
print("Enter the numbers: ")
for i in range(n):
    z=int(input())
    x.append(z)

p= min(x, n)
q= max(x, n)
print(f"The smallest number is: {p}")
print(f"The largest number is: {q}")