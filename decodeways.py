# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).


dict = {}
j=1
s = "06"
count = 0

for i in range(65,91):   
    if i <=91:
        dict[chr(i)] = j
        j +=1

if int(s) in dict.values():
        count += 1
for k in s:
    if int(k) in dict.values():
        count += 1

print(count)












# if  int(s) in dict.values():
#     # print(list(dict.keys())[list(dict.values()).index(int(s))])
#    for key , values in dict.items():  
#         if int(s) == values:
#             print(key,values)
 

