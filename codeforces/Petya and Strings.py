first = input()
second = input()

f1 =first.lower()
f2 = second.lower()

if f1 == f2:
    print(0)
elif f1<f2:
    print(-1)
else:
    print(1)