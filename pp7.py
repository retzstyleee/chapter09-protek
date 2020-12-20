mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print("===========================================================")
print('NIM'.ljust(6, ' '), end='')
print('NAMA MAHASISWA'.ljust(25, ' '), end='')
print('TGL LAHIR'.ljust(15, ' '), end='')
print('TEMPAT LAHIR'.ljust(15, ' '))
print("-----------------------------------------------------------")
for i in mhs:
	x = i.split(":")
	print(x[0].ljust(6, ' '), end='')
	print(x[1].ljust(25, ' '), end='')
	tgl = x[2].split("-")
	c = 0
	for t in reversed(tgl):
		if(c != (len(tgl)-1)):
			print(t, end='/')
		else:
			print(t, end=' ')
		c+=1
	print(''.ljust(3, ' '), end=' ')
	print(x[3].ljust(15, ' '))
print("-----------------------------------------------------------")	