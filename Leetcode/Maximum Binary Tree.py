nums = [3,2,1,6,0,5]
max = 3
for i in nums:
    if i >=max:
        max = i

class node:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def addnode (self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.addnode(data)
            else:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.addnode(data)
    
    def printinf(self):
        print(self.data ,end="")
        if self.left:
            self.left.printinf()
        if self.right:
            self.right.printinf()

root = node(max)
root.addnode(3)
root.addnode(2)
root.addnode(1)
root.addnode(0)
root.addnode(5)
root.printinf()