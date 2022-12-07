class test:

    name = 'rahul'
    age = 22

e1 = test()
e2 = test()

# print("name is ",e1.__class__.name)
# print(getattr(e1,"name"))
# setattr(e1,'new',222)
# print(getattr(e1,"new"))
# delattr(e1,"new")

print("name is ",e2.__class__.name)
setattr(e2,"neeeee","new atttr")
print(getattr(e2,"neeeee"))
delattr(e2,"neeeee")
print(getattr(e2,"neeeee"))