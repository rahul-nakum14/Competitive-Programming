for _ in range(int(input())):

    a,b = map(int,input().split())

    if a*2 > b*5:
        print("chocalte")
    elif a*2 < b*5:
        print("candy")
    else:
        print("either")