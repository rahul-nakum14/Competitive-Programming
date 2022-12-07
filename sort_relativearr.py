# arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# arr2 = [2,1,4,3,9,6]

# Output: [2,2,2,1,4,3,3,9,6,7,19]

arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]


#  [2,42,38,0,43,21
# ,5,7,12,12,13,23,24,24,27,29,30,31,33,48]'''

# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
k = []

for j in range(len(arr2)):
    for i in range(len(arr1)):
        search = arr2[j]
        if search == arr1[i]:
            k.append(arr1[i])

q = []
for i in arr1:
    if i not in arr2:
        q.append(i)
        # arr1.remove(i)
q.sort()

for i in q:
    k.append(i)
print(k)
# for q in arr1:
#     k.append(q)
# print(k)
# y = set(arr1)
# x = set(arr2)

# for i in y.copy():
#     if i in x:
#         y.remove(i)
#         x.remove(i)

# q = list(y)
# q.sort()
# for u in q:
#     k.append(u)
# print(k)
# x = list(y)
# print(k.append(x))
# print(k)


# z = set(y)-set(x)
# print(z)

# res = list(set(y)^set(x))
# print(res)
# print(set(y).difference(x))
