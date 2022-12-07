for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    while c != n and len(s) != 1:
        s = s.replace("11",'0')
        s = s.replace("00","0")
        c += 1
    if len(s) == 1:
        print("yes")
    else:
        print("no")
    