for _ in range(int(input())):
    tmp = []
    k = []
    count = 0
    
    n,budget= map(int,input().split())

    for _ in range (n):
        tmp.append(list(map(int,input().split())))
   

    for i in (tmp):
        if budget>=i[2]:
            k.append(i[0]*i[1])
            count = 1

    if count==0:
        print("no tab")
    else:
        print(max(k))


# for _ in range (u):
#     tmp.append(list(map(int,input().split())))
