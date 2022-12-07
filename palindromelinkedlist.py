class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    a1 = []
    class node:
        a1 = []
        b1 = []
        def __init__(self,data) :
            self.data = data
            self.next = None

    def addlast(self,data):
        a = linkedlist.node(data)
        if self.head == None:
            self.head = a
            self.tail = a
        self.tail.next = a
        self.tail = a

    def traversefirst(self):
        first = self.head
        while(first):
            linkedlist.node.a1.append(first.data)
            first = first.next
        print(linkedlist.node.a1)

    def travesrlast(self):
        current = self.head
        previous = None
        while(current):
            tmp = current.next
            current.next = previous
            previous  = current
            current = tmp
        self.head = previous
  
    def callreverse(self):   #same as printlist
        current  = self.head
        while(current):        
            linkedlist.node.b1.append(current.data)
            current = current.next
        print(linkedlist.node.b1)

    def palindrome(self):
        if linkedlist.node.a1 == linkedlist.node.b1:
            print("True")
        print("False")

obj = linkedlist()
obj.addlast(10)
obj.addlast(20)
# obj.addlast(30)
# obj.addlast(10)
obj.traversefirst()
obj.travesrlast()
obj.callreverse()
obj.palindrome()

'''class linkedlist:
    def __init__(self):
        self.head = None

    class node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def addlast(self,data):
        a = linkedlist.node(data)
        if self.head == None:
            self.head = a
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = a

    def reverse(self,head):
        current = self.head
        previous = None
        while(current):
            tmp = current.next
            current.next = previous
            previous = current
            current  = tmp
        self.head = previous
        return self.head

    def palindrome(self):
        firstpoint = self.head
        lastpointer = self.reverse(self.head)
        while firstpoint and lastpointer:
            if firstpoint.data != lastpointer.data:
               print("False")
               exit()
            else:
                firstpoint,lastpointer = firstpoint.next,lastpointer.next
        print("True")


    def print(self):
        current = self.head
        while(current):
            print(current.data,"-->",end="")
            current = current.next
        print("Null")

obj = linkedlist()
obj.addlast(10)
obj.addlast(20)
obj.addlast(5550)
obj.addlast(10)
obj.palindrome()
obj.print()'''