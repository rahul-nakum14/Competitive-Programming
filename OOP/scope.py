class a:
    def __init__(self,name):
        self.name = name

    def printdata(self):
        print("name is ",self.name)

class b:
    def __init__(self,no):
        self.no = no

    def printdata1(self):
        print("No is ",self.no)

class c(a,b):
    def __init__(self,age):
        a.__init__(self,"helo")
        b.__init__(self,"988188818")
        self.age = age

    def printdata2(self):
        print("Age is ",self.age)

obj = c(19)
obj.printdata()
obj.printdata1()
obj.printdata2()


