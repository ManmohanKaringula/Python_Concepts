def fib(n):
    a=0
    b=1
    while(b<n):
        a,b=b,a+b
        printfib(a)

def printfib(a):
    print(a)

if(__name__=="__main__"):
    import sys
    n=int(sys.argv[1])
    fib(n)




