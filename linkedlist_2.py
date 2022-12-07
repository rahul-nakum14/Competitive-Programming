
class node:

    def __init__ (self,data):
        self.data = data
        self.next = None
    
class linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def addlast(self,data):
        a = node(data)
        if self.head == None:
             self.head = a
             self.tail = a
        else:
            self.tail.next = a
            self.tail = a

    def printlist(self):
        current = self.head
        while(current):
            print(current.data , "-->",end = "")
            current = current.next
        print("Null")

    def rotatelist(self):
        # k = 2
        # while k:
            current = self.head
            while(current):
                current = current.next

                if current.next == None:
                    current.next = self.head
                    print(current.next)
                    break

    def detectcycle(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next != None:
              slow = slow.next
              fast = fast.next.next
             
              if slow.data == fast.data:
                    print("cycle")
                    return
               
        print("not cycle")
                




obj = linkedlist()
obj.addlast(10)
obj.addlast(20)
obj.addlast(30)
# obj.printlist()
obj.rotatelist()
obj.detectcycle()