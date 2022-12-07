n=int(input())
print(n//2-n%2*n)

n = int(input())
tmp = []
i = 1

while i<n+1:
    if i%2==0:
        tmp.append(i)
        i+=1
    else:
        tmp.append(-i)
        i+=1
print(sum(tmp))
