for _ in range(int(input())):
	n=int(input())
	a=list(input())
	ans=0
	for j in a:
		if j=='Q':
			ans+=1
		else:
			if ans>0:
				ans-=1

	if ans>0:
		print('NO')
	else:
		print('YES')