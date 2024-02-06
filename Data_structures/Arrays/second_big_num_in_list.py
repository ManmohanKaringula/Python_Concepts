def lent(lst):
    a=0
    while a<2:
        max=lst[0]
        for i in range(1, len(lst)):
            if lst[i]>max:
                max =lst[i]
        lst.remove(max)
        a+=1
    return max
if __name__=="__main__":
    n=int(input("Enter the size of the list:  "))
    lst=[int(input("Enter the elements: ")) for i in range(n)]
    print('\n')
    print(f"The second largest element in the list is: {lent(lst)}")



    

