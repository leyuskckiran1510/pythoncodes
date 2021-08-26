'''
with open('ascii.txt','rb') as opn:
	a=opn.readlines()
mapper={}
cut=100
for i in a:
	cut+=1
	mapper[i.decode().split('=')[1].strip()]=cut
print(mapper)
with open('mapper.py','w') as opn:
	opn.write(f'chart={mapper}')
'''
'''
from mapper import chart,chartrev


with open('file.txt','r') as opn:
	data=opn.read()


def decomp():
	for i in range(0,len(nume),+3):
		print(chartrev[int(nume[i:i+3])],end='')

nume=''
print('here')
for i in data:
	nume+=str(chart[i])
print('now compressing')
'''
from mapper import chart,chartrev


with open('file.txt','r') as opn:
	data=opn.readlines()


def decomp():
	for i in range(0,len(nume),+3):
		print(chartrev[int(nume[i:i+3])],end='')

nume=''
print('here')
for i in data:
	pseudo=''
	for j in i:
		pseudo+=str(chart[j])
	ak=str(int(pseudo)//2**56)+":"+str(int(pseudo)%2**56)
	nume+=ak+'\n'
print('now compressing')
print(nume)



