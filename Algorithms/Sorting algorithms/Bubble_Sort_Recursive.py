def bubbleSortRecursive(list1, iterpass=0):
    swap=False
    for i in range(0, len(list1)-iterpass-1):
        if list1[i]>list1[i+1]:
            list1[i], list1[i+1]=list1[i+1], list1[i]
            swap=True
    if swap==True:
        iterpass+=1
        bubbleSortRecursive(list1, iterpass)
    return list1

if __name__=="__main__":
    n=int(input("Enter the number of elements: "))
    list1=[int(input("Enter the number: ")) for i in range(n)]
    print("The unsorted list is: ", list1)  
    # Calling the bubble sort function  
    a=bubbleSortRecursive(list1)
    print(f"The sorted list is {a} ")