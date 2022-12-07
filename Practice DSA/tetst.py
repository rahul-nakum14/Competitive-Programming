class node:
    def __init__(self,data) :
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self) :
        self.head = None

    def addlast(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = newnode
    
    def print(self):
        current = self.head
        while(current):
            print(current.data, "-->",end="")
            current = current.next
        print("NUll")

    def merge(self,obj,obj1):
        current = obj.head
        current2 = obj1.head
        newnode = node(None)        
        while current and current2 != None:
            if current.data <= current2.data:
                newnode.next = current
                current = current.next
                newnode = newnode.next
            else:
                newnode.next = current2
                current2 = current2.next
                newnode = newnode.next

        if current:
                newnode.next = current
                newnode = newnode.next

        if current2:
                newnode.next = current2
                newnode = newnode.next
                
        # newnode.next = current or current2  # out of the loop
        self.head = newnode.next


obj = linkedlist()
obj.addlast(10)
obj.addlast(20)
obj.addlast(30)
obj.addlast(40)

obj1 = linkedlist()
obj1.addlast(50)
obj1.addlast(60)
obj1.addlast(70)
obj1.addlast(80)

obj3 = linkedlist()
obj3.merge(obj,obj1)
obj.print()

