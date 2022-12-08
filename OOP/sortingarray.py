import array as arr

a = arr.array('i',[])

size = int(input("Enter Size of array"))

for k in range(size):
    value = int(input("Enter value"))
    a.append(value)


for i in range(size):
    for j in range(i+1,size):
        if a[i] > a[j]:
                 temp = a[i]
                 a[i] = a[j]
                 a[j] = temp
        

print(a)




#for i in range(size):
#     for j in range(size):
#         j=i+1
#         if j == size:
#             break
#         else:
#             a[i] > a[j]
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
#             break 

# print(a)
