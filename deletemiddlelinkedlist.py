class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def addlast(self,data):
        newnode  = node(data)

        if self.head is None:
                self.head = newnode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode
           
    def addfirst(self,data):
        newnode = node(data)
        if self.head is None:
                self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def printlist(self):
        current = self.head
        while current:
            print(current.data,"-->",end=" ")
            current = current.next
        print("NUll")


    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next != None:
            previous = slow
            slow = slow.next
            fast = fast.next.next
            
        previous.next = previous.next
        self.printlist()

        # print(slow.data)

    # def deletemiddle(self):
    #     current = self.head
    #     previous = None

    #     middle = self.middle()

    #     while current != None:
    #         tmp = current.next
    #         if current.data == middle:
    #             previous.next = tmp
    #             break
    #         else:
    #             current = current.next
    #             previous = previous.next
            
    #             self.printlist()



obj = linkedlist()
obj.addlast(1)
obj.addlast(2)
obj.addlast(3)
obj.addlast(4)
# obj.deletemiddle()
# obj.printlist()