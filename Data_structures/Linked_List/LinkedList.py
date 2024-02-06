class linkedListNode:
    def __init__(self, data=None, nextNode=None):
        self.data=data
        self.nextNode=nextNode

class linkedList:
    def __init__(self):
        self.head=None

    def insert(self, data): # This method is generally used to insert at the end of the list...
        node= linkedListNode(data)
        if self.head==None:
            self.head=node
        else:
            currentNode=self.head
            while True:
                if currentNode.nextNode==None:
                    currentNode.nextNode=node
                    break
                else:
                    currentNode=currentNode.nextNode

    def insertAtPosition(self, data, position):
        insertnode=linkedListNode(data)
        if self.head==None:
            self.head=insertnode

        elif position==1:
            a=self.head
            self.head=insertnode
            insertnode.nextNode=a

        elif position==2:
            currentnode=self.head
            a=currentnode
            for i in range(position-1):
                currentnode=currentnode.nextNode
            a.nextNode=insertnode
            insertnode.nextNode=currentnode

        else:
            currentnode=self.head
            for i in range(1,position):
                currentnode=currentnode.nextNode
                if i==position-2:
                    a=currentnode
                if i==position-1:
                    b=currentnode
            a.nextNode=insertnode # Important concept 
            insertnode.nextNode=b

# Method to print linked list
    def printLinkedList(self):
        currentnode=self.head     
        while currentnode!=None: # MOST IMPORTANT POINT: whenever an object of a class is assigned to variable and if we print the variable, the interpreter 
                                 # returns the memory location of the object say <__main__.linkedListNode object at 0x000000B2AE381220> in this linked list 
                                 # data_structure the class linkedListNode has self.nextNode instance variable with a default value None in the above code 
                                 # but when we insert a node the value of nextNode= linkedListNode object hence not None but for the last insertion the 
                                 # the default value is None.
            print(currentnode.data, "-->>", end="")
            print("\t", currentnode.nextNode)
            currentnode=currentnode.nextNode
            

ll=linkedList()
ll.insert(99)
ll.insert(22)
ll.insert(45)
ll.insert(32)
ll.printLinkedList()
print('\n')
ll.insertAtPosition(100,3)
ll.printLinkedList()
print('\n')
ll.insertAtPosition(2000,2)
ll.printLinkedList()
print('\n')
ll.insertAtPosition(155,1)
ll.printLinkedList()

