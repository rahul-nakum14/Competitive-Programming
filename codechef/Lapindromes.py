for _ in range(int(input())):
    s = input()
    hashmap = {}
    hashmap1 = {}

    # if len(s) %2 == 1:
    #     middle = len(s)//2
    #     s1 = s[:middle]
    #     s2 = s[middle+1:]
    #     s = s1+s2

    middle = len(s)//2

    left = s[:middle]
    right = s[(len(s)-middle):len(s)]

    for i in left:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for j in right:
        if j not in hashmap1:
            hashmap1[j] = 1
        else:
            hashmap1[j] += 1

    if hashmap == hashmap1:
        print("yes")
    else:
        print("no")