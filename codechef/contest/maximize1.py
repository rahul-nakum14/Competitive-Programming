import itertools

s="111"
tmp = []
for i in range(len(s)):
    if s[i] == "1":
        tmp.append(i)

print(tmp)
perm = list(itertools.combinations(tmp,2))

print(perm)