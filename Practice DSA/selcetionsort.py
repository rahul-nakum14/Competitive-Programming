a = [10,20,5,14,8]

for i in range(len(a)):
    min = i

    for j in range(i+1,len(a)):
        if a[j]< a[min]:
            min = j

    # a[i] ,a [min] = a[min],a[i]

    tmp = a[i]
    a[i] = a[min]
    a[min] = tmp
    
print(a)
