
def xor(a, b, n):
	ans = ""
	for i in range(n):
		
		if (a[i] == b[i]):
			ans += "0"
		else:
			ans += "1"
	return ans


if __name__ == "__main__":
	a = "10"
	b = "01"
	n = len(a)
	c = xor(a, b, n)
	print(int(c, 2))
