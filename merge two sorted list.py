a = [1,2,4]
b = [1,3,4]
k = a+b

for i in range(len(k)):
    min =i
    for j in range(i+1,len(k)):
        if k[j] < k[min]:
            min = j
    tmp = k[i]
    k[i] = k[min]
    k[min]  = tmp

print(k)