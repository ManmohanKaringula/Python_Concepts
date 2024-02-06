# the iterative recursion is faster than the recursive fibonacci
def recur_iter(n, first, second):
    print(f"{first}\n{second}")
    for i in range(0, n-2):
        c=first+second
        print(c)
        first, second=second, c  

if __name__=="__main__":
    first=0
    second=1
    n=int(input("Enter the limit: "))
    recur_iter(n, first, second)