l = list(map(int,input().split()))

l1=l[:2]
l2=l[2:4]
l3=l[4:len(l)]
    
if l1[0] in l2 and l1[1] in l2:
        print("1")
elif l1[0] in l3 and l1[1] in l3:
        print("2")
else:
        print("0")
# t,t1 = a[0],a[1]

# count = 0

# for i,val in enumerate(a[2:]):
#     if t == i:
#         continue
#     if t1 == i:

