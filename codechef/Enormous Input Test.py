n , k = map(int ,input("").split())
count = 0

for _i in range(n):
    datainput = int(input())
    if datainput % k  == 0:
        count += 1
    else:
        count = 0 
print(count)
# print(1%3)