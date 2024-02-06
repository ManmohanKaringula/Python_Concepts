def insertionSort(list1):
    for i in range(1,len(list1)):
        while i-1>=0:
            if list1[i]<list1[i-1]:
                list1[i], list1[i-1]=list1[i-1], list1[i]  
                i-=1
            else:
                break    # This break is very important in the insertion sort program as reduces the extra iteration
            
    return list1

if __name__=="__main__":
    n=int(input("Enter the number of elements: "))
    list1=[int(input("Enter the number: ")) for i in range(n)]  
     # The input function only takes string datatype by default hence it should be converted to int in the above list comprehension....
    print("The unsorted list is: ", list1)  
    # Calling the insertion sort function  
    print("The sorted list is: ", insertionSort(list1))
