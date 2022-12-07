class linkedlist:
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

    def middle(self):
        fast = self.head.next
        slow = self.head
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next     
        return slow.data
    
    def reverse(self,first):
        current = first
        previous = None
        while(current):
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        return previous

    def palindrome(self):
        first = self.middle()
        secondpass = self.reverse(first)
        



'''    def palindrome(self):
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = none ,
        curr = slow.next
        slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        head2 = prev

        currM=prev
        currB=self.head
        while currM and currB:
            if currM.data !=currB.data:
                print("False")
                exit()
            currM=currM.next
            currB=currB.next
        print("True")'''


'''https://leetcode.com/problems/palindrome-linked-list/discuss/1695170/Python-Very-Easy-Approach'''

'''https://leetcode.com/problems/palindrome-linked-list/discuss/2468307/Yet-another-two-fast-Python-solutions-O(N)'''

'''https://leetcode.com/problems/palindrome-linked-list/discuss/2467211/Python-Simple-Python-Solution-using-Slow-Fast-Faster-and-Reverse-Linked-list'''

'''https://leetcode.com/problems/palindrome-linked-list/discuss/2467076/Daily-Leetcode-Challenge-23th-August-Python3-solution'''

obj = linkedlist()
obj.addlast(10)
obj.addlast(20)
obj.addlast(270)
obj.addlast(10)
obj.palindrome()