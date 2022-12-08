import array as arr

a = arr.array('i',[])

n = int(input("Enter The Size OF array"))

for i in range(n):
    value = int(input("Enter Value To append"))
    a.append(value)

for k in range (n):
    tmp = n-1
    print(a[tmp])
    n = n-1
