for _ in range(int(input())):
    a,b = input().split()

    if(a==b):
                print('=')
    if "M" in a and "M" not in b:
            print(">")

    elif "S" in a and "S" not in b:
            print("<")

    elif "L" in a and "L" not in b:
            print(">")

    elif(a[-1]==b[-1]=='S'):
                if(len(a)>len(b)):
                    print('<')
                else:
                    print('>')
    else:
                if(a[-1]>b[-1]):
                    print('<')
                else:
                    print('>')