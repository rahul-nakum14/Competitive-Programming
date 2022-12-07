row = int(input())
cols = int(input())

'''one liner'''
matrix = [[int(input()) for i in range(cols)] for i in range(row)]
# matrix = [[0]*cols for i in range(row)]

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

# matrix = []
# for i in range(rows):
#   row = []
#   for j in range(cols):
#     row.append(int(input()))
#   matrix.append(row)

# print(matrix)

