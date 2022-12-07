a= [1,1,1,0,0,0]

b = []


b.append(a[0])

for i in range(len(a)-1):
    if a[i] == a[i+1] and int(0) in a:
        b.extend(a[i],0)
        a.remove(0)
        
# first = 0
# last = len(a)-1

# print(first)
# print(last)
# for i in range(len(a)-1):
#     if a[i] == a[i+1]:
#         a[first],a[last] = a[last],a[first]

#         first +=1
#         last -=1

# print(a)