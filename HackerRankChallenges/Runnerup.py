import copy
if __name__ == '__main__':
    n = int(input())   
    arr = map(int, input().split())    
    ls=list(arr)   
    a=2
    for i in range(a):
        max=ls[0]
        for j in range(1,len(ls)):       
            if ls[j]>max:
                max=ls[j]
        if i==0:
            b=copy.copy(ls)
            for k in range(len(ls)):
                if ls[k]==max:
                    b.remove(max)
            ls=b
        else:
            print(max)
                    
