n, t = list(map(int, input().split()))

s= input()
list1 = list(s)
for k in range(t):
    count = 0
    for yy in range(n):
        while count<len(list1)-1:
                if list1[count] == "B" and list1[count+1] == "G":
                    list1[count] = "G"
                    list1[count+1] = "B"
                    count+=2
                else:
                    count += 1
list1 = ''.join(list1)
print(list1)


# for count in range(count,len(list1)-1):

# j=0
# while j<=len(s)-1:
#         if (j+1)<=(len(s)-1) and s[j]=="B" and s[j+1]=="G":
#             s=s[:j]+"G"+"B"+s[j+2:]
#             j=j+2
#         else:
#             j=j+1
# print(s)