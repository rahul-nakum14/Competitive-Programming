for _ in range(int(input())):

    testcase = int(input())
    s= input()

    vowels = ['a','e','i','o','u']
    test = []
    constant = 0

    for i in range(65,91):
        if chr(i).lower() not in vowels:
            test.append(chr(i).lower())


    for i in range(testcase):
        for j in s:
            if j in test:
                constant += 1
            else:
                constant = 0

        if constant >= 4:
                print("NO")
    else:
                print("YES")


# for i in range(int(input())):

#     n= int(input())

#     s = input()

#     v = ['a','e','i','o','u']
    
#     count=0
#     for i in range(n):
#         if s[i] not in v:
#             count+=1
#         else:
#             count=0
#         if count==4:
#             print("no")
#             break
#     else:
#         print("yes")
            