for _ in range(int(input())):
    a,b = map(int, input().split())

    total = a+b

    if total%2 ==0:
        print("yes")
    else:
        print("no")
