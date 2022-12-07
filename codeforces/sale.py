n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
x=[i for i in l if i<0]
tmp =(sorted(x)[:m])
sumii = abs(sum(tmp))
print(sumii)


