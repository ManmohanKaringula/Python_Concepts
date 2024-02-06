
# First  method
list1 = [10, 20, 4, 45, 99]
 
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:       # checking for the maximum number
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and mx != list1[i]:
        secondmax=list1[i]
 
print("Second highest number is : ",\
      str(secondmax))

# Second Method: The second method find the first max and then find second max at the same time....
def findLargest(arr):
    secondLargest = arr[0]
    largest = arr[0]
 
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
 
    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
 
    # Returning second largest element
    return secondLargest
 
# Calling above method over this array set
print(findLargest([10, 20, 4, 45, 99]))


# Third method: Using list comprehension....

def secondmax(arr):
  sublist = [x for x in arr if x < max(arr)]
  return max(sublist)
 
if __name__ == '__main__':
  arr = [10, 20, 4, 45, 99]
  print(secondmax(arr))

  