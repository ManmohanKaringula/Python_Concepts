def bubble_sort(list1):      
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)):  
        for j in range(0, len(list1)-1-i):  # this loop is for the passes to occur
            if(list1[j]>list1[j+1]):                  
                list1[j],list1[j+1] = list1[j+1], list1[j]         
            else:
                continue
    return list1, 
  
if __name__=="__main__":
    n=int(input("Enter the number of elements: "))
    list1=[int(input("Enter the number: ")) for i in range(n)]
    print("The unsorted list is: ", list1)  
    # Calling the bubble sort function  
    a=bubble_sort(list1)
    print(f"The sorted list is {a}" )
