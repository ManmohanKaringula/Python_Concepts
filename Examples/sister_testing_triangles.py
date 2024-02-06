def triangle(n):
    count=1
    t=[]
    for i in range(0, n):
        print(" "*((n-i)-1) + str(count), end='')
        t.append(" "*((n-i)-1) + str(count))
        x=0
        while x!=i:
            count+=1
            print(" "+str(count), end='')
            t.append(" " + str(count))
            x+=1
        count+=1
        print("\n")
        t.append("\n")
    return t, n/2
x=int(input("Enter the number of lines: "))
c,n=triangle(x)
ll=len(c)
print(c, ll)

def calc(c, ll, n):
    j=ll-2
    k=0
    ans, total=[], []
    while n!=0:
        p, q=[], []
        while c[j] != '\n':
            p.append(c[j])
            j-=1
        while c[j-1] != '\n':
            q.append(c[j-1])
            j-=1
        j=j-1
        
        while k<(n*2)-1:
            ans.append(p[k])
            ans.append(q[k])
        ans.append(p[(n*2)-1])
        count=0

        while count<(n*2)+((n*2)-1):
            
            if see==0:
                T=ans[count]+ans[count+1]
                






        


        
        

    
    


