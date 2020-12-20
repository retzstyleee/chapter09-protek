nilai =	[{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
       	 {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
       	 {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('=' * 60)
print('NIM'.ljust(8, ' '), end='')
print('NAMA'.ljust(16, ' '), end='')
print('N.MID'.ljust(10, ' '), end='')
print('N.UAS'.ljust(10, ' '), end='')
print('N.AKHIR'.ljust(10, ' '), end='')
print('STATUS'.ljust(12, ' '))
print('-' * 60)

for i in nilai:
	nilaiAkhir = round((i.get('mid')+i.get('uas')*2)/3, 2)
	if nilaiAkhir >=60:
		status = 'LULUS'
	else:
		status = 'TIDAK LULUS'
	print(i.get('nim').ljust(8, ' '), end='')
	print(i.get('nama').ljust(16, ' '), end='')
	print(str(i.get('mid')).ljust(10, ' '), end='')
	print(str(i.get('uas')).ljust(10, ' '), end='')
	print(str(nilaiAkhir).ljust(10, ' '), end='')
	print(status.ljust(12, ' '))

print('=' * 60)
