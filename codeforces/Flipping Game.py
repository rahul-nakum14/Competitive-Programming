for _ in range(int(input())):
    
    count = 0
    n = int(input())

    s = list(map(int,input().strip().split()))

    for i in s:
        if s[i] and s[i+1] == 0:
            s[i] = 1
            s[i+1] = 1
for i in s:
        if i==1:
            count +=1

print(count)