'''Instance Methods  --> types are accessor ,mutator 
   Class Methods --> works with class variable
   Static Methods  -- > seprate independatent method
   '''

class a:

    all = "abcxyz"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    # def avg(self):
    #     total = (self.m1+self.m2+self.m3)//3
    #     print(total)

    def getvalue(self):
        print(self.m1,self.m2,self.m3)
    
    def setvalue(self):
        self.m1 = 555
        print(self.m1,self.m2,self.m3)

    @classmethod  #decorators
    def info(cls):
        print(cls.all)

    @staticmethod
    def staticm1(val1,val2):
        sum = val1+val2
        print(sum)

    
# s1 = a(34,67,32)
# s2 = a(89,32,182)

s3 = a(35,66,44)
s3.staticm1(10,20)

# s1.getvalue()
# s1.setvalue()

# a.info()  calling class method

#s2.avg()

'''
class hello:
    def __init__(self, m, n): #this needs m and n
      self.g = m
      self.h = n

    def hi(self, x, y):
      a = x + self.g
      b = x + self.h #use self to access other class members
      return a, b
  
m = 100
n = 200
obj = hello(m, n) #pass m and n to the constructor
c = obj.hi(10, 11)
print(c)
'''