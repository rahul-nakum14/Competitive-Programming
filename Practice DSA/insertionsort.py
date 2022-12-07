a = [20,10,50,15]

for i in range(len(a)):
    tmp = a[i]
    j = i-1
    while j>=0 and a[j] > tmp:
        a[j+1] = a[j]
        j -=1
    a[j+1] = tmp
print(a)