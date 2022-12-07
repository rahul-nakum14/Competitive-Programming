'''There are two types of variable 
    Instance Variable and
    Class (Static Variable)

    Instance variable are seprated for each object obj,obj1
    Class Variable have same value across all object 

    namespace is a place where create and store object/variable
'''

class a:

    comman = "gtu"  #class namespace

    def __init__(self):
        self.name="rahul"  # instance namespace
        self.age=22

c1 = a()
c2 = a()

a.comman="c2name"

print(c1.age,c1.name,c1.comman)
print(c2.age,c2.name,c2.comman)

