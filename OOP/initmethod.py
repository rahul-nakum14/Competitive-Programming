class a:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age= age

    def config(self):
        print("name is ",self.name,"age is",self.age)

obj = a("rahul",19)
obj1 = a("abc",22)
obj.config()
obj1.config()

'''Types the way to create Object'''
# a.config(obj)
# obj.config()

'''Getting value from user'''

'''class a:
    def __init__(self,name):
        self.name=name
    def printdata(self):
        print("name is",self.name)

data = input("Enter name")
obj = a(data)
obj.printdata()'''