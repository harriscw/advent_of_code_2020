import sys
from itertools import cycle

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

#print(mylist)

mypos = [0,0,"E"]

for instruc in mylist:
	if instruc[0:1]=="L" or instruc[0:1]=="R":
		print(instruc)


