nums = [1,2,4,7,10]

tmp = []
t1 = []
final = 0
for i in nums:
    if i%2==0 and i%3==0:
        tmp.append(i)
    
total = sum(tmp)
try:
    final = total//len(tmp)
    print(final)
except Exception:
    print("0")


