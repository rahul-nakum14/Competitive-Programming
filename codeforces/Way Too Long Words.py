for _ in range(int(input())):
    
    s = input()

    if len(s) > 10:
        # first = (s[0:])
        first,last = s[0],s[-1]
        between = len(s[1:-1])

        print(first+str(between)+last)
    else:
        print(s)