for _ in range(int(input())):
    data = map(int,input().split())
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s = input()
    tmp = []
    pos = 0
    for i in range(26):
        pos+=1
        if a[i] not in s:
            tmp.append(pos)
    print(sum(tmp))