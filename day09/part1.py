import csv
import sys
import itertools

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
    mylist.append(int(lines[i].strip("\n")))
print(mylist)

#print(mylist)

preamblength=25

for i in range(len(mylist)-preamblength):
	preamble=mylist[i:preamblength+i]
	restoflist=mylist[preamblength+i:]
	#print(preamble)
	#print(restoflist)
	#print(restoflist[0])
	mypairs=list(itertools.combinations(preamble, 2))
	#print(mypairs)
	mysums=set(map(sum,mypairs))
	#print(mysums)
	
	if restoflist[0] not in mysums:
		sys.exit("Stop! " + str(restoflist[0]))
	else:
		print("Sum exists")
	