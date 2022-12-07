for _ in range(int(input)):
    c=[]
    n,k,v=map(int,input().split())
    c = list(map(int,input().split()))
    d = sum(c)
    ans=(((n+k)*v)-d)/k
    if ans>0 and ans%1==0:
        print(int(ans))
    else:
        print(-1)
# for i in range (a[1]):
#     b.append(1)

# avg = 4

# maxel = max(b)

# for i in range(maxel):
    
#     for j in b:
#         if j==1:
#             b[j] = i

#             avf = sum(b) // len(b)

#             if avf == avg:
#                 print(i)
#                 break

