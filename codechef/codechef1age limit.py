# def main(x,y,age):

#     if not y and age:
#         output = "YES"

#     # x = 21
#     # y = 
#     # age = 
#     # output = None

#     if age >= x and age<y:
#        output = "YES"
#     else:
#         output = "NO"
#     return output

    
# if __name__=="__main__":
#     print(main(21))

# (int(x,y,age)) = ((""),(""),(""))
# x,y,age = [int(i) for i in (input("").split())]
n = 3
while n:
    x,y,age = map(int,input().split())
    if age >= x and age<y:
        print("Yes")
    else:
        print("NO")
    n -= 1