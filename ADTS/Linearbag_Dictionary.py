class Linear_bag:

    def __init__(self, bag):
        self.bag=bag

    def add(self, item):
        self.item=item
        if self.item not in self.bag.keys():
            self.bag[self.item]=1
        else:
            self.bag[self.item]+=1 

    def Print_bag(self):
        print(self.bag)

    def remove(self, remove_item):
        self.remove_item=remove_item
        if self.remove_item in self.bag.keys():
            if self.bag[self.remove_item]>1:
                self.bag[self.remove_item]-=1
            else:
                del self.bag[self.remove_item]
        else:
            print(f"There is no {self.remove_item} in the bag")

    def baglen(self):
        return len(self.bag)


my_dict={}
n=int(input("Enter the number of items to be entered into the bag: "))
My_bag=Linear_bag(my_dict)
for i in range(n):

    My_bag.add(input("Enter the item name: "))

My_bag.remove(input("Enter the element to be removed: "))
My_bag.Print_bag()
print(My_bag.baglen())


