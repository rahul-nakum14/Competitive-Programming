totalpass = 0
tmp = []
for _ in range(int(input())):
	exit,enter = map(int,input().split())
	totalpass = (abs(totalpass-exit)+enter)
	tmp.append(totalpass)
print(max(tmp))