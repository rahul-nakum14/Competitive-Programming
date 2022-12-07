# a = []
# # ch = int(input())
# for _ in range(1):
#      a = [int(item) for item in input().split()]
# grade = " "
# for i in range(len(a) -1):
#     sum = a[i] + a[i+1]
#     if sum %2 == 1:
#         grade = "yes"
#         break
#     else:
#         grade = "no"
# print(grade)
 

# # a = 12
# # if a %3 == 1:
# #     print("even")
# # else:
# #     print("oodd")


# import itertools

# numbers = [3,3,9]

# result = [seq for i in range(len(numbers), 0, -1)
#           for seq in itertools.combinations(numbers, i)
#           if sum(seq) == target]

# print(result)

import itertools

numbers = []

for _ in range(1):
    numbers = [int(item) for item in input().split()]
combinations1 = []

combinations = itertools.combinations(numbers,2)
for i in combinations:
    combinations1.append(i)

for j in combinations1:
   if (j[0]+j[1]) %2 == 1:
    grade = "yes"
    break
   else:
    grade = "no"

print(grade)