def selectionSortRecursive(list1, n=0): #The n parameter is the index in the list that has to be checked the n value always increases and the recursive fjfunction is called.
    minimum=list1[n]
    for i in range(n+1, len(list1)-1):
        if minimum>list1[i]:
            minimum=list1[i]
            list1[i]=list1[n]
            list1[n]=minimum
    n+=1
    if n<=(len(list1)-2):
        selectionSortRecursive(list1, n)
    return list1
    
if __name__=="__main__":
    n=int(input("Enter the number of elements: "))
    list1=[int(input("Enter the number: ")) for i in range(n)]
    print("The unsorted list is: ", list1)  
    # Calling the bubble sort function  
    print("The sorted list is: ", selectionSortRecursive(list1))
