def insertionSortRecursion(list1, p=1):
    if p<= (len(list1)-1):
        q=p
        while  q-1>=0:
            if list1[q]<list1[q-1]:
                list1[q], list1[q-1]=list1[q-1], list1[q]
                q-=1
            else:
                break
        p+=1
        insertionSortRecursion(list1, p)
    return list1

if __name__=="__main__":
    n=int(input("enter the number of elements you want to sort: "))
    list1=[int(input("Enter the number: "))for i in range(n)]
    print("The unsorted list is: ", list1)
    print("The sorted list is: ", insertionSortRecursion(list1))

