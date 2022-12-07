num = "III"
sum = 0
k = []
dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

# for i in num:
#     k.append(dict[i])

for i in range (len(num) -1 ):
    if  dict[num[i]]  < dict[num[i+1]] :
        sum = sum - dict[num[i]] 
    else:
        sum = sum + dict[num[i]] 

print(sum + dict[num[-1]] )

#leetcode submission

'''class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        k = []
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        for i in s:
            k.append(dict[i])

        for i in range (len(k) - 1):
            if  k[i]  < k[i+1]:
                sum = sum - k[i]
            else:
                sum = sum + k[i] 

        return (sum + dict[s[-1]])'''