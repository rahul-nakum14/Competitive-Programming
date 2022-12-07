def mergesort(a):
    if len(a) <= 1:
        return a
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        mergesort(left)
        mergesort(right)

    i,j,= 0,0
    k = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            k.append(left[i])
            i += 1
        else:
            k.append(right[j])
            j +=1
    k.extend(left[i:])
    k.extend(right[j:])
    return k

a = [90,123,13,567,11,49,36]
print(mergesort(a))

