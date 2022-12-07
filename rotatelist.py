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

    # def printlist(self):
    #     current = self.head
    #     if self.head is not None:
    #         while (True):
    #             print(current.data,"-->",end="")
    #             current = current.next
    #             if current == self.head:
    #                 break
    #         print("NUll")

    def printlist(self):
        current = self.head
        while (current != None):
            print(current.data,"-->",end="")
            current = current.next
        print("NUll")

    # def rotatelist(self):
    #     k = 3 
    #     while k >=2:
    #         current = self.head.next    
    #         previous = self.head
            
    #         while(current.next):
    #             current = current.next
    #             previous = previous.next

    #         current.next = self.head
    #         self.head= current
    #         previous = None
            
    def rotatelist(self, k):  # k should be parameter
        if self.head == self.tail:  # Fewer than 2 elements
            return
        for _ in range(k):  # Determine the number of iterations
            current = self.head.next
            previous = self.head
            
            while current.next:
                current = current.next
                previous = previous.next
    
            current.next = self.head
            self.head= current
            previous.next = None  # Correction
            # self.tail = previous  # Update tail

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
obj.addlast(1)
obj.addlast(2)
obj.addlast(3)
obj.addlast(4)
obj.addlast(5)
obj.rotatelist(6)
obj.printlist()
# obj.detectcycle()
