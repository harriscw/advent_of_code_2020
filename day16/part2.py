import sys
import re
import numpy as np
import sympy

#####
#Read data 
#####

text_file = open("input.txt", "r")
lines = text_file.readlines()

#####
# get my ticket
#####

myticket=[]
seen=False
for i in range(len(lines)):
	if lines[i].strip("\n")=="your ticket:": #stop when this is observed
		seen=True
	else:
		if lines[i].strip("\n") != "" and seen==True:
			myticket = list(map(int,lines[i].strip("\n").split(",")))
	if len(myticket)>0:
		break
print("My ticket: ", myticket)


#####
#get valid numbers
#####

combinedRegex = re.compile("[0-9]+-[0-9]+")#regular expression for range of numbers
myranges0=[]
rowids=[]
for i in range(len(lines)):
	if lines[i].strip("\n")=="your ticket:": #stop when this is observed
		break
	else:
		if lines[i].strip("\n") != "":
			myranges0.append(combinedRegex.findall(lines[i].strip("\n"))) #get the ranges
			rowids.append(lines[i].strip("\n").split(": ")[0]) #get the rownames
			
###
#combined all valid numbers into a single list
###

validnums = []
for therange in myranges0:
	l1start=int(therange[0].split("-")[0])
	l1end=int(therange[0].split("-")[1])+1
	l2start=int(therange[1].split("-")[0])
	l2end=int(therange[1].split("-")[1])+1
	validnums.append(list(range(l1start,l1end))+list(range(l2start,l2end)))
myranges=validnums #save this for later
validnums=list(set([inner for outer in validnums for inner in outer])) #get unique values
validnums.sort()

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

nearbytix=[list(map(int, x)) for x in nearbytix]

###
# Find invalid numbers and remove those tickets
###

notthere=[]#find rows with invalid numbers
for i in range(len(nearbytix)): #iterate rows in nearbytix (distinct tickets)
	therow=nearbytix[i]
	for j in therow: #iterate over values in that row
		if j not in validnums: #compare each value to the valid numbers
			notthere.append(i)#find rows with invalid numbers
#print("rows with invalid numbers: ",notthere)

for index in sorted(notthere, reverse=True):
    del nearbytix[index]


########
# Get a matrix of 0s and 1s
# checking if all the numbers in a given column of nearby tickets are in ranges specified
# output matrix will be square
########

nearbytix=np.array(nearbytix)

outlist=[]
for i in range(len(nearbytix[0,:])):#iterate over columns
	rowlist=[]
	for j in myranges:#iterate over the ranges for each type
		if(len(set(nearbytix[:,i]).intersection(j))==len(set(nearbytix[:,i]))):
			rowlist.append(1)
		else:
			rowlist.append(0)
	outlist.append(rowlist)

print(rowids)
mymat=np.array(outlist).T######ugggggh it took me forever to figure out I needed to transpose here

######
# RREF the matrix by hand because I couldn't find an RREF function that keeps track of column names
######

cnt=0
seen = []
mydict=dict()
while cnt<=mymat.shape[1]:
	for col in range(mymat.shape[1]):#iterate over columns
		if(list(mymat[:,col]).count(1)==1 and list(mymat[:,col]).count(0)==mymat.shape[1]-1) and col not in seen:#if you find a reduced column you haven't seen before
			seen.append(col)
			theindex=list(mymat[:,col]).index(1)
			#print("column:",col,"is",rowids[theindex])
			mydict[rowids[theindex]]=col
			for col2 in range(mymat.shape[1]):
				if(list(mymat[:,col2]).count(1)==1 and list(mymat[:,col2]).count(0)==mymat.shape[1]-1):#if you find a reduced row skip it
					continue
				else:
					mymat[:,col2]-=mymat[:,col]
	cnt+=1		

print(mydict)	
print(myticket[mydict['departure station']]*myticket[mydict['departure track']]*myticket[mydict['departure location']]*myticket[mydict['departure date']]*myticket[mydict['departure platform']]*myticket[mydict['departure time']])



				
	

