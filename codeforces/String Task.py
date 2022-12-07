vowels = ['a','e','i','o','u','y']

s = input().lower()

for i in s:
    if i in vowels:
         s = s.replace(i,'')
for i in s:
    print("."+i,end= "")

