for _ in range(int(input())):
    n,district,state = map(int,input().split())
    s = input()

    while n:
        total1 = int(s.count("1"))
        total0 = int(s.count("0"))
        n -=1
    print(total1*state+total0*district)
