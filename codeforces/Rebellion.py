for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sorted(l)
    c = 0
    for i in range(n):
        if l[i] != s[i]:
            c += 1
    print(c//2)


n=int(input())
i=0
while i<n:
    x=int(input())
    t=input().split()
    print(t[:t.count("0")].count("1"))
    i+=1

    # a = [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]

# count = 0

# # def sorting(a):
# #     if a == sorted(a):
# #         print(count)
# #         exit
# #     else:
# #         return "no"


#     # for i,val in enumerate(a,1):
#     #         a[j] + val
# for i in range(len(a)):
#     if a == sorted(a):
#                 break
#     else:
#             # a[j]  = a[j]+a[i]
#             j = len(a)-1
#             tmp = a[j]
#             tmp1 = a[j]
#             tmp2 = a[i]
#             tmp = tmp1+tmp2
           
#             a.pop(i)
            
#             count +=1
#             if a == sorted(a):
#                 break
            
# print(count)


