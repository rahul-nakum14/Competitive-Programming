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
    def __init__(self,name,no,age):
        super().__init__(name,no)
        self.age = age

    def printdata2(self):
        print("Age is ",self.age)

obj = c("helo",98745856,20)
obj.printdata()
obj.printdata1()
obj.printdata2()




