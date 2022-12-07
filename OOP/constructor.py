class a:
    def __init__(self) -> None:
        self.name= "rahul"
        self.age = 22

    def update(self):
        self.age = 66

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

        
obj = a()
obj1 = a()

# obj1.name="new namw" #changing value
#print(obj.name) #rahul
# print(obj1.name) # new name Every objcet has different value
# obj1.update()
# print(obj.age)

if obj.compare(obj1): #obj1.age == obj.age
    print("same")
else:
    print("different")