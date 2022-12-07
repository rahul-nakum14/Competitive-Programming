class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        
    def addfirst(self,data):
        a = node(data)
        if self.head is None:
            self.head = a
            return
        a.next = self.head
        self.head = a

    def addlast(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newnode

    def addpos(self,data,pos):
        newnode = node(data)
        current = self.head
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        for i in range (1,pos-1):
            current = current.next
        newnode.next = current.next
        current.next = newnode
        
    def delfirst(self):
        if self.head == None:
            print("List is empty")
        self.head = self.head.next

    def dellast(self):
        current = self.head.next
        previous = self.head

        while (current.next != None):
            current = current.next
            previous = previous.next
        
        previous.next = None

    def delpos(self,pos):
        current = self.head.next
        previous = self.head

        if pos == 1:
             self.head = self.head.next
        for i in range(1,pos-1):
            current = current.next
            previous = previous.next

        previous.next = current.next


    def printlist(self):
        temp = self.head
        while (temp != None):
                print(temp.data,"-->",end="")
                temp = temp.next
        print("Null")

a = linkedlist()
# a.addfirst(10)
# a.addfirst(20)
# a.addfirst(30)
# a.addfirst(40)
a.addlast(10)
a.addlast(20)
a.addlast(30)
a.addlast(40)
a.dellast()
a.printlist()

