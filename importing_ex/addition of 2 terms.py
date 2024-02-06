x=[]
y=100
ans=[]
for i in range(0, 22):
    x.append(y)
    y+=1

print(x)

for j in range(0, 22, 2):
    c=x[j]+x[j+1]
    ans.append(c)

print(ans)
