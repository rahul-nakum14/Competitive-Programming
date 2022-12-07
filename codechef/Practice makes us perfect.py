a = []
count = 0
for _ in range(1):
    a = [int(item) for item in input().split()]
# for i in range(int(input())):
#     a.append(i)
for index,value in enumerate (a,1):
# for index in a:
    if value >= 10:
        count += 1
    else:
        pass
print(count)