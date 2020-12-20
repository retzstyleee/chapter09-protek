def bintang(n):
	n = n * 2
	for i in range(0, n, 2):
		i += 1
		string = '*' * i
		print(string.center(n, ' '))

bintang(4)