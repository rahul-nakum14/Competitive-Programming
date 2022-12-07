class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def addnode(self,data):
        if self.data is None:                                   
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.addnode(data)
                
            elif data > self.data:
                if self.right is None:
                    self.right= Node(data)
                else:
                    self.right.addnode(data)

    # def searchNode(self,root,value):  
    #     #Check whether tree is empty  
    #     if(self.data == None):  
    #         print("Tree is empty");  
          
    #     else: 
    #         if root:
    #             if root.data == value:
    #                 return root
    #         if value > root.data:
    #                 return (self.searchNode(root.left,value))
    #         if value < root.data:
    #                 return (self.searchNode(root.right,value))
    #         else:
    #                 print("not found")
            # if root.left.data and root.right.data ==None:
            #     print("child node")
            #     exit()

            # if(root.data == value):  
            #         print(root.left.data)
            #         print(root.right.data)
            #         return;  

            # if(root.left != None):  
            #     if (root.left == None):
            #         print("child node")
            #         exit()
            #     else:
            #         self.searchNode(root.left, value);  
              
            # #Search in right subtree  
            # elif(root.right != None): 
            #     if (root.right == None):
            #         print("child node")
            #         exit()
            #     else:
            #         self.searchNode(root.right, value);  
            # else:
            #     print("not found")

    def searchtree(self,searchkey):
            if self.data == searchkey:
                print("found")
            elif self.left:
                # return(self.searchtree(self.left))
                return self.left.searchtree(searchkey)
            elif self.right:
                # return(self.searchtree(self.right))
                 return self.right.searchtree(searchkey)
            else:
                print("not found")
            
            # elif searchkey < self.data:
            #     if self.left == searchkey:
            #         return (self.left.searchtree(searchkey))
            # elif searchkey > self.data:
            #     if self.right == searchkey:
            #         return(self.right.searchtree(searchkey))
            # else:
            #     print("key not found")

    # def inorder(self):
    #         if self.left:
    #             self.left.inorder()
    #             searchkey = 2
    #             if self.data == searchkey:
    #                 # print(self.data,end=" ")
    #                 print(self.data)
    #                 print(searchkey.left)
    #                 exit()
    #             else:
    #                 print("Not found")
    #                 exit()
    #         if self.right:
    #             self.right.inorder()



        
# '''  def addnode(self,data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.addnode(data)

#             elif data > self.data:
#                     if self.right is None:
#                         self.right = Node(data)
#                     else:
#                         self.right.addnode(data)
#         else:
#                 self.data = data
# '''
    # def inorder(self):
    #     if self.left:
    #         self.left.inorder()
    #     print(self.data,end=" ")
    #     if self.right:
    #         self.right.inorder()


    # def preorder(self):
    #     print(self.data,end=" ")
    #     if self.left:
    #         self.left.preorder()
    #     if self.right:
    #         self.right.preorder()

    
    # def postorder(self):
    #     if self.left:
    #         self.left.postorder()
    #     if self.right:
    #         self.right.postorder()
    #     print(self.data,end=" ")

    # def PrintTree(self):
    #   if self.left:
    #      self.left.PrintTree()
    #   print( self.data)
    #   if self.right:
    #      self.right.PrintTree()
    #  # print("found")
#                 if root.left.data and root.right.data != None:
#                     # print(root.left.data)
#                     # print(root.right.data)
#                     print("Found")
#                     return;  
#                 if root.left.data and root.right.data == None:
#                     print("Child node")
#                     return


# '''def searchNode(self,root,value):  
#         #Check whether tree is empty  
#         if(self.data == None):  
#             print("Tree is empty");  
          
#         else: 
            
#             if root.left.data and root.right.data ==None:
#                 print("child node")
#                 exit()

#             if(root.data == value):  
#                     print(root.left.data)
#                     print(root.right.data)
#                     return;  

#             if(root.left != None):  
#                 if (root.left == None):
#                     print("child node")
#                     exit()
#                 else:
#                     self.searchNode(root.left, value);  
              
#             #Search in right subtree  
#             elif(root.right != None): 
#                 if (root.right == None):
#                     print("child node")
#                     exit()
#                 else:
#                     self.searchNode(root.right, value);  
#             else:
#                 print("not found")'''

root = Node(4)
root.addnode(2)
root.addnode(7)
root.addnode(1)
root.addnode(3)
root.searchtree(1)
# root.searchtree(2)


# root.PrintTree()
# print("----------------Pre order---------------------------")
# root.preorder()
# print("----------------In order-------------------")
# root.inorder()
# print("----------------Post ordet--------------------")
# root.postorder()
# print("-------------------------------------------")

# root.PrintTree()
# root = Node(10)
# root.left = Node(34)
# root.right = Node(89)
# root.left.left = Node(45)
# root.left.right = Node(50)
# root.PrintTree()