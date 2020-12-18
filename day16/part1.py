import sys
import re

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()

###
#get valid numbers
###

combinedRegex = re.compile("[0-9]+-[0-9]+")#regular expression for range of numbers

myranges0=[]
for i in range(len(lines)):
	if lines[i].strip("\n")=="your ticket:": #stop when this is observed
		break
	else:
		if lines[i].strip("\n") != "":
			myranges0.append(combinedRegex.findall(lines[i].strip("\n")))

#combined all valid numbers into a single list
validnums = []
for therange in myranges0:
	l1start=int(therange[0].split("-")[0])
	l1end=int(therange[0].split("-")[1])+1
	l2start=int(therange[1].split("-")[0])
	l2end=int(therange[1].split("-")[1])+1
	validnums.append(list(range(l1start,l1end))+list(range(l2start,l2end)))

validnums=list(set([inner for outer in validnums for inner in outer])) #get unique values
validnums.sort()
#print(validnums)

###
#get nearby tickets
###
seen=False
nearbytix=[]
for i in range(len(lines)):
	if lines[i].strip("\n")=="nearby tickets:": #only start appending after you see this
		seen=True
	elif seen==True:
		nearbytix.append(lines[i].strip("\n").split(","))
#print(nearbytix)


###
# Find invalid numbers
###

notthere=[]
for i in range(len(nearbytix)): #iterate rows in nearbytix (distinct tickets)
	therow=nearbytix[i]
	for j in therow: #iterate over values in that row
		if int(j) not in validnums: #compare each value to the valid numbers
			notthere.append(int(j))
#print(notthere)		
print("the sum:", sum(notthere))	



				
	

