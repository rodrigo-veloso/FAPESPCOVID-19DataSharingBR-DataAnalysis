
fileName = 'HSL_Exames_2.csv'

with open(fileName, "r") as myFile:
		make = myFile.readlines();

#for i,line in enumerate(make):
#	if line[-2] == '|':
		#print(True)
		#make[i] = make[i].replace('||','')
#		make[i] = make[i][:-2] + make[i][-1]

for i,line in enumerate(make):
#	if line[-2] == '|':
#		print(True)
	make[i] = make[i].replace('"','')
		#make[i] = make[i] + make[-1]


#print(make[-1])#.replace('||',''))

#for line in make:
#	print(line[-2])

with open(fileName, "w") as myFile:
		myFile.writelines(make)




