class a:
    def __init__(self):
        self.name = "outer"
        self.age = 55
        # self.innefr = self.inner() Used to create Object inside class

    def show(self):
        print(self.name,self.age)
        
    class inner:
        def __init__(self):
            self.name = "inner"
            self.age = 19

        def show(self):
            print(self.name,self.age)

        class inner1:
            def __init__(self):
                self.name = "inner1"
                self.age = 66

            def show(self):
                print(self.name,self.age)


obj = a()
obj.show()

obj1 = a.inner()
obj1.show()

obj2 = a.inner.inner1()
obj2.show()
'''Outer Class object'''
# s1 = a("abc",20)
# s1.show()

'''Creating object outside class'''
# obj = a.inner()
# obj.show()

'''Accessing Object inside'''
# obj = s1.innefr
# obj.disp()