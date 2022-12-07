# # Each test case consists of three integers N,X,, and Y, 
# # the number of problems, the maximum score for each problem, and the score Chef wants.


# prob  = No of prob.
# x = max score
# y = chef wants


# 1 8 4
# 3 6 12

for _ in range(int(input())):

    n,x,y=map(int,input().split())

    if y%x==0:
        print("yes")
    else:
        print("no")