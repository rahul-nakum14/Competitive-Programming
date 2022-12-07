#https://leetcode.com/discuss/general-discussion/603729/singly-linked-list-data-structure-python

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkelist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addlast(self,data):
        newnode  = node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newnode

    def reverselist(self):
        current = self.head
        previous = None
        while (current != None):
            newnode = current.next
            current.next =  previous
            previous = current
            current = newnode
        self.head = previous
 
        
    def circularlist(self):
        current = self.head
        while(current.next):
            current = current.next
        current.next = self.head
 
    def printlist(self):
        current = self.head
        while (current != None):
            print(current.data,"-->",end="")
            current = current.next
        print("NUll")

    def circularprintlist(self):
        current = self.head
        while (current != None):
            print(current.data,"-->",end="")
            current = current.next
            if current == self.head:
                exit()
        print("NUll")
 

a  = linkelist()
a.addlast(10)
a.addlast(20)
a.addlast(30)
a.addlast(40)
a.circularlist()
a.printlist()
# a.circularlist()
# a.circularprintlist()
# a.detectcycle()
