class node:
    def __init__(self,data):
        self.data = data
        self.next= None

class linkedlist:
    def __init__(self):
        self.head= None

    def addlast(self,data):
        newnode = node(data)
        if self.head is None:
            self.head =  newnode 
            return
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newnode

    def l1(self):
        objforl1 = linkedlist()

        def __init__(self):
            objforl1.head = None

        def addlast(self,data):
            newnode = node(data)
            if objforl1.head is None:
                objforl1.head =  newnode 
                return
            current = objforl1.head
            while(current.next != None):
                current = current.next
            current.next = newnode

            objforl1.addlast(99)
            objforl1.addlast(88)
            objforl1.addlast(77)
            objforl1.addlast(66)
            objforl1.print()

        def print(self):
            current = objforl1.head
            while current:
                print(current.data,"-->",end="")
                current = current.next
            print("NULL")

    def print(self):
        current = self.head
        while current:
            print(current.data,"-->",end="")
            current = current.next
        print("NULL")

obj = linkedlist()
obj.addlast(10)
obj.addlast(20)
obj.addlast(30)
obj.l1()
obj.print()