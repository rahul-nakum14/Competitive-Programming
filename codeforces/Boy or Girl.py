# distint chr == odd male

a = input()
tmp = []
count = 0

for i in a:
    if i not in tmp:
        tmp.append(i)
        count += 1

if count %2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")