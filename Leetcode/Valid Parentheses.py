s = "()["

closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
stack = []

for char in s:
    
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    print(closeToOpen[char])
                    stack.pop()
                else:
                    print("False")
            else:
                stack.append(char)

print("True" if not stack else "False")

# if len(s)==1:
#         print("false")
# for i in range(len(s)-1):

#     if s[i+1] in hashmap.values():
#         print("true")
#     else:
#         print("false")

# print(hashmap)