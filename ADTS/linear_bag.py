class bag:

    def __init__(self, bag_list):
        self.bgl=bag_list

    def check_item(self, item):
        self.item = item
        if(self.item in self.bgl):
            print(f"{item} is present in the bgl")

        else:
            print(f"{item} is not present in the bgl")
          

n= int(input("Enter the number of input: "))
baglist=[int(input("Enter the number: ")) for i in range(n)]

MYbag=bag(baglist)

item=input("Enter the item to be searched: ")

MYbag.check_item(item)

