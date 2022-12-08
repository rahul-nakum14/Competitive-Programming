# Single level


class a:
    def __init__(self,name):
        self.name = name

    def printdata(self):
        print("name is ",self.name)

class b(a):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def printdata2(self):
        print("Age is ",self.age)

obj = b("helo form child",20)
obj.printdata()
obj.printdata1()

# print(obj.name)
# print(obj.age)
# obj.printdata()
# obj.printdata1()
