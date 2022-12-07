# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true

a = ["a", "cb"]
b = ["ab", "c"]
# b = ["a", "bc"]

tmp = []

# for i in range (len(a)):
   
# tmp.append(join(a[i]))
tmp1 = ''.join(a)
tmp2 = ''.join(b)

if tmp1==tmp2:
    print("true")
else:
    print("false")