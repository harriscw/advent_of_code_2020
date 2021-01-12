import sys

def findloops(num):
	value=1
	loops=0
	while value != num:
		value=(value*7)%20201227
		loops+=1
	print("Loop size for",value,"is:",loops)

#findloops(5764801) #card
#findloops(17807724) #door
findloops(8458505)
findloops(16050997)

# Transform
def getencryption(loops,key):
	value=1
	for i in range(loops):
		value=(value*key)%20201227
	print("Encryption key is:", value)
	
#getencryption(8,17807724)#use card loop size with door key
#getencryption(11,5764801)#use door loop size with card key
getencryption(15260454,16050997)#use card loop size with door key
getencryption(10476062,8458505)#use door loop size with card key