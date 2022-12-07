class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left= None

        
# # class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if p is None and q is None:
#             return True
#         if p is None or q is None:
#             return False
#         if p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
#             return True
    def addnode(self,data):
        if self.data is None:                                   
            self.data = data
        else:
            if data <self.data:
                if self.left is None:
                        self.left = node(data)
                else:
                        self.left.addnode(data)
            else:
                if self.right  is None:
                    self.right = node(data)
                else:
                    self.right.addnode(data)


    def printing(self):
        print(self.data)
        if self.left:
            self.left.printing()
        if self.right:
            self.right.printing()


root =  node(10)
root.addnode(5)
root.addnode(15)
root.addnode(30)
root.addnode(3)
root.printing()