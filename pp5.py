nilai =	[{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
       	 {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
       	 {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('=' * 40)
print('NIM'.ljust(10, ' '), end='')
print('NAMA'.ljust(15, ' '), end='')
print('N.MID'.ljust(10, ' '), end='')
print('N.UAS'.ljust(10, ' '))
print('-' * 40)

for i in nilai:
	print(i.get('nim').ljust(10, ' '), end='')
	print(i.get('nama').ljust(15, ' '), end='')
	print(str(i.get('mid')).ljust(10, ' '), end='')
	print(str(i.get('uas')).ljust(10, ' '))

print('=' * 40)
