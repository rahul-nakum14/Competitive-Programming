for _ in range(int(input())):
        n = int(input())
        if n>2:
                if(n%2==0):
                         print(int((n-2)/2))
                else:
                         print(n//2)
        else:
                print(int(0))


# https://codeforces.com/contest/1335/submission/178786638
# https://codeforces.com/contest/1335/submission/178671075


# t = 6
# if(t>2):
#     if(t%2==0):
#             print(int((t-2)/2))
#     else:
#             print(int(t//2))
# else:
#         print(0)

# ujju = 7
# spr=2000000000
# tmp = spr-1
# final = tmp//2

# print(final)






    # for _ in range(int(input())):
#     target = int(input())
#     count = 0
#     hashmap = {}
#     for i in range (target):
#                 com = target - i
#                 if com in hashmap:
#                     # print([hashmap.get(com),i])
#                     count +=1
#                 else:
#                     hashmap[i] = i
#     print(count)
