def bintang(n):
	if(n % 2 == 0):
		print("Bukan bilangan ganjil")
	else:
		n1 = n
		n2 = n
		for i in range(0, n1, 2):
			i += 1
			string = '*' * i
			print(string.center(n1 , ' '))
		for j in range(n2, 1, -2):
			j -= 2
			string = '*' * j
			print(string.center(n2, ' '))

bintang(7)