for _ in range(int(input())):
	n = int(input())
	p = n//2
	i = p
	while i > 0:
		j = i
		while j <= n:
			print(j, end=" ")
			j += p
		i -=1
		
	print()