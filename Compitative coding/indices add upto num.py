# The below code is used to check whether the given target number can be obtained from adding any two numbers in the 
# list, if two number add upto the target number then the indices are returned. 

nums=[2,7,11,15]
target=9
x=[]
length=len(nums)
count=0
a=True
while a:
    for i in range(0, length-1):
        if i<=(length-1)-2:
            k=i+1
            for j in range(k,length):
                b=nums[i]+nums[j]
                if b>target:
                    break
                elif b==target:
                    x.append(i)
                    x.append(j)
                    print(x)
                    count+=1
                    x.clear()
                    
        else:
            l=i+1
            if nums[i]+nums[l]==target:
                x.append(i)
                x.append(l)
                print(x)
                x.clear()
            elif count==0:
                print(f"There exist no two numbers that add up to {target}")
    a=False
