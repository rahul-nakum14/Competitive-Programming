for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    tmp = set(x)
    print(len(tmp))