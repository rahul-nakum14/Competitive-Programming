for tc in range(int(input())):
    size,addi = map(int,input().split())
    ele = [int(x) for x in input().split()]
    x = max(ele)
    for i in range(addi):
        ele.append(x+i+1)
    
    ele.sort()
    print(ele[(size+addi)//2])
# if len(a)%2==0:
#         tmp = a[-1]
#         a.append(tmp+2)
#         sor1 = sorted(a)
#         total = sum(a)
#         div = math.ceil(total/len(a))
#         print(div)
# else:
#     tmp = a[-1]
#     for i in range (3):
#         a.append(tmp+2)
#     sor1 = sorted(a)
#     total = sum(a)
#     div = math.ceil(total/len(a))
#     print(div)
