# for _ in range(int(input())):
#     n= int(input())

#     for i in range(n, 0,-1):
#             print(i)

import math
import itertools


n = int(input())

per = itertools.permutations(set(a for a in range([n])))

print(per)
# number = int(input("Enter the Number"))

# root = math.sqrt(number)
# if int(root + 0.5) ** 2 == number:
#     print(number, "is a perfect square")
# else:
#     print(number, "is not a perfect square")