n = 13
if int(n) < 3:
        print(int(n))
else:
        if int(n) % 2 == 1:
            print(int(n) - (int(n) // 2))
        else:
            print((int(n) - (int(n) // 2)) + 1)


# for _ in range(int(input())):
#     n = int(input())
#     hashmap = {}

#     if n%2==0:
#             print("0")
#     else:

#         for i in range(1,n+1):
#             rem = n%i
#             hashmap[i] = rem
#             keys = list(hashmap.keys())
#             val = list(hashmap.values())

#         maxval = val.index(max(val))
#         print(keys[maxval])