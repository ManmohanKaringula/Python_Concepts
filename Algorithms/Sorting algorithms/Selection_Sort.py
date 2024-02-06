def Selection_sort(lst):
    for i in range(len(lst)-2):
        minimum=lst[i] # Setting a variable as a minimum number in the list.
        for j in range(i+1, len(lst)):
            if minimum>lst[j]: # Checking the condition whether the minimum number is greater than the consequent number
                minimum=lst[j]
                lst[j]=lst[i]
                lst[i]=minimum
            else:
                continue
    return lst
if __name__=="__main__":
    n=int(input("enter the number of elements you want to sort: "))
    lst=[int(input("Enter the number: "))for i in range(n)]
    print(Selection_sort(lst))
