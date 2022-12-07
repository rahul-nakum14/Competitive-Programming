#https://leetcode.com/discuss/general-discussion/603729/singly-linked-list-data-structure-python

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkelist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addfirst(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            return
        newnode.next = self.head
        self.head = newnode

    def addlast(self,data):
        newnode  = node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newnode
 
        
    def circularlist(self):
        current = self.head
        while(current.next):
            current = current.next
        current.next = self.head
    
    def circularprintlist(self):
        current = self.head
        if self.head is not None:
            while (True):
                print(current.data,"-->",end="")
                current = current.next
                if current == self.head:
                    break
            print("NUll")
 
    def addlasttail(self,data):
        obj = node(data)
        if self.head == None:
           self.head = obj
           self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj

    def detectcycle(self):
        current = self.head
        a = []
        while(current):
            if current in a:
                print("True")
                exit()
            a.append(current)
            current = current.next
        print("False")

    # def detectcyclefailed(self):
    #     current = self.head
    #     while(current):
    #        current = current.next
    #        if current != None:
    #             print("True")
    #             exit()
    #     print("False")
    
    def printlist(self):
        current = self.head
        while (current != None):
            print(current.data,"-->",end="")
            current = current.next
        print("NUll")
 

a  = linkelist()
a.addlast(10)
a.addlast(20)
a.addlast(30)
a.circularlist()
a.circularprintlist()
# a.addlasttail(10)
# a.addlasttail(20)
# a.detectcycle()

