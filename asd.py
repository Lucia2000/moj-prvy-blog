def ahoj():	
	print('Ahoj')
	print('AKo sa mas')
ahoj()
def cau(meno):
	if meno=='Lucia':
		print('Ahoj Lucia')
	elif meno== 'Maria':
		print('Ahoj Maria')
	else:
		print('Ahoj cudzinec')
cau('Lucia')
def cauko(meno):
	print('Ahoj'+ meno)
cauko('Maria')

def diev(meno):
	print('Ahoj'+ meno)
dievcata= ['Maria','Lucia', 'Betka', 'Anna']
for meno in dievcata: 
	diev(meno)
	print('Dalsie dievca')
for z in range(1,8):
	print(z)