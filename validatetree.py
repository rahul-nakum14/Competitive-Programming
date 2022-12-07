class tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def addnode(self,data):
      if self.data is None:
        self.data = data
      else:
        if data < self.data:
            if self.left is None:
                self.left = tree(data)
            else:
                self.left.addnode(data)
        if data>self.data:
            if self.right is None:
                self.right = tree(data)
            else:
                self.right.addnode(data)

    def printingtree(self): #in order
        if self.left:
            self.left.printingtree()
        print(self.data,end= " ")
        if self.right:
            self.right.printingtree()

    # def preorder(self):
    #     print(self.data,end = " ")
    #     if self.left:
    #         self.left.preorder()
    #     if self.right:
    #         self.right.preorder()


    def searchtree(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return " Not Found"
            return self.left.searchtree(lkpval)

        elif lkpval > self.data:
                if self.right is None:
                    return str(lkpval)+" Not Found"
                return self.right.searchtree(lkpval)
        else:
                print(str(self.data) + ' is found')


    def findingpaent(self,childnode):
        if childnode < self.data:
            if self.left.data is None:
                return "not found"
            else:
                if self.left.data == childnode:
                    print(self.data)
                    return
                self.left.findingpaent(childnode)
           

        if childnode > self.data:
            if self.right.data is None:
                return "not found"
            else:
                if self.right.data == childnode:
                    print(self.data)
                    return
                self.right.findingpaent(childnode)
       

    # def searchtree(self,searchkey):
    #         if self.data == searchkey:
    #             print("found")
    #         elif self.left:
    #             # return(self.searchtree(self.left))
    #             return self.left.searchtree(searchkey)
    #         elif self.right:
    #             # return(self.searchtree(self.right))
    #              return self.right.searchtree(searchkey)
    #         else:
    #             print("not found")


root = tree(10)
root.addnode(5)
root.addnode(15)
root.addnode(2)
root.addnode(8)
# root.printingtree()
# root.preorder()
root.findingpaent(15)