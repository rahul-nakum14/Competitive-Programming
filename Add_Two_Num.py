from urllib.parse import non_hierarchical


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self) -> None:
        self.head = None

    def addlast(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            return
        else:
            current = self.head
            while(current.next != None):
                 current = current.next
            current.next = newnode

    def printlist(self):
        current = self.head
        while current != None:
            print(current.data,"-->",end="")
            current = current.next
        print("Null")

    def sorting(self):
        current = self.head
        current1 = self.head.next

        while current and current1:
            if current.data > current1.data:
                tmp =current1.data
                current1.data = current.data
                current.data = tmp
            current1 = current1.next   
            
obj = linkedlist()
obj.addlast(20)
obj.addlast(10)
obj.addlast(5)
obj.sorting()
obj.printlist()

