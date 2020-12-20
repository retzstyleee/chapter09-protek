import random
def shuffleString(x, n):
	string = x
	listString = []
	i = 0
	while i < n:
		hasil = ''.join(random.sample(string, len(string)))
		if hasil not in listString:
			listString.append(hasil)
			i += 1
		else:
			continue
	return listString

print(shuffleString('aku', 3))