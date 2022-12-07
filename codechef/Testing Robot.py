n = 6 
x = 10
tmp = []
s = "RRLLLL"

for i in s:
    if i == "R":
        tmp.append(x)
        x = x+1
        if x not in tmp:
            tmp.append(x)
    else:
        tmp.append(x)
        x = x- 1
        if x not in tmp:
            tmp.append(x)

print(len(set(tmp)))