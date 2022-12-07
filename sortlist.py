class node:
    def __init__(self,data):
        self.data= data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head= None

    def addlast(self,data):
        current = self.head
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return

        while current.next != None:
            current = current.next
        current.next = newnode

    def getMid(self, head):

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

    def sorting(self):

        if self.head == None or self.head.next == None:
                return self.head

            mid = self.getMid(self.head)
            mid1 = mid.next
            mid.next = None

            l = self.sortList(self.head)
            r = self.sortList(mid1)

            res = self.mergeSortList(l, r)

            return res

    def mergesort(self,list1,list2):

        dummy = newnode = node(None)

        while list1 and list2:
            if list1.data < list2.data:
                newnode.next = list1
                list1 = list1.next
                newnode =newnode.next

            else:
                newnode.next = list2
                list2 = list2.next
                newnode = newnode.next

            while list1:
                newnode.next = list1
                list1=list1.next
                newnode = newnode.next

            while list2:
                newnode.next = list2
                list2=list2.next
                newnode = newnode.next

        self.head = dummy.next

    def print(self):
        current = self.head
        while current:
            print(current.data,"-->",end = "")
            current = current.next
        print("NULL")

    # def bubblesort(self):
    #     if self.head != None:
    #         while 1:
    #             swap = 0
    #             c1 = self.head
    #             c2 = self.head.next

    #             while(c1.next != None):
    #                     if c1.data > c2.data:
    #                             swap += 1
    #                             p = c2.next
    #                             c2.next = c1
    #                             c1.next = p
    #                     else:
    #                             c1 = c1.next
    #                             c2= c2.next
    #                     c1 = c1.next
    #                     c2= c2.next
    #             if swap == 0:
    #                 break
    #             else:
    #                 continue

    # def sorting(self, data):
    #     new_node = node(data)
    #     if self.head is None:
    #         self.head = new_node
    #         return

    #     temp = self.head
    #     if temp.data > data:
    #         new_node.next = temp
    #         self.head = new_node
    #         return

    #     while temp.next:
    #         if temp.next.data > data:
    #             break
    #         temp = temp.next

    #     new_node.next = temp.next
    #     temp.next = new_node

        

        # while current :

        #     if current.data < current1.data:
        #         newnode.next = current
        #         current = current.next
        #         newnode = newnode.next
        #     else:
        #         newnode.next = current
        #         newnode = newnode.next

        #     # current1= current1.next
        #     current = current.next
        #     current1 = current1.next

        # if current:
        #             newnode.next = current
        #             newnode = newnode.next



        # c1 = self.head
        # c2 = self.head.next

        # while c1 and c2:

        #     if c1.data > c2.data:
        #      tmp = c2.next
        #      c2.next = c1
        #      c1.next = tmp
        #      c1 = c1.next
        #      c2 = c2.next
        #     else:
        #         c1 = c1.next
        #         c2 = c2.next

        # self.head = c1

obj = linkedlist()
obj.addlast(70)
obj.addlast(20)
obj.addlast(80)
obj.addlast(10)
obj.addlast(220)
obj.middle()
obj.print()
