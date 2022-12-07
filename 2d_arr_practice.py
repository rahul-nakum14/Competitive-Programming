# row = int(input())
# cols = int(input())
row = 3
cols = 3
'''one liner'''
# matrix = [[int(input()) for i in range(cols)] for i in range(row)]
# matrix = [[0]*cols for i in range(row)]
'''
1 2 3
4 5 6
7 8 9
'''
# if input format like this then use following
# mat = [list(map(int,input().split())) for i in range(row)] 

'''printing'''

# print(matrix)

'''manual printing'''
# for i in range(row):
#     print()
#     for j in range(cols):
#         print(matrix[i][j],end=" ")


'''manual code'''
# rows = int(input())
# cols = int(input())

# rows = 3
# cols = 3

# matrix = []
# for i in range(rows):
#   row = []
#   for j in range(cols):
#     # row.append(int(input()))
#     row.append(0)
#   matrix.append(row)

# for i in range(rows):
#     print()
#     for j in range(cols):
#         print(matrix[i][j],end=" ")


