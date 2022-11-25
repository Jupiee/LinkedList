class Node:

    def __init__(self, data, next= None):

        self.data= data
        self.next= next

class LinkedList:

    def __init__(self):

        self.head= None
        self.curr= None
        self.tail= None

    def prepend(self, data):

        newNode= Node(data)
        newNode.next= self.head
        self.head= newNode
        del newNode

    def append(self, data):

        self.curr= self.head
        newNode= Node(data)
        
        while self.curr != None:
            
            self.tail= self.curr
            self.curr= self.curr.next
        
        self.tail.next= newNode
        self.tail= newNode
        self.curr= None

mylist= LinkedList()

mylist.prepend(15)
mylist.prepend(69)
mylist.append(56)
mylist.append(123)

print(mylist.tail.data)
print(mylist.head.data)