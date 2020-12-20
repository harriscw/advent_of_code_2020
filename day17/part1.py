import sys
import numpy as np
from collections import Counter


###
# Data wrangling
###

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(list(lines[i].strip("\n")))
	
print(np.array(mylist)) #print as array for formatting

#get coords into a dict
hashes=[]
for i in range(len(mylist)):
	for j in range(len(mylist[i])):
		if mylist[i][j]=="#":
			hashes.append((0,i,j))

#initialize dictionary of coordinates with count 0
mycoords=dict()
for i in hashes:
	mycoords[i]=0
	
###
# Define necessary functions
###

#define a function to get all 27 [(3^3)-1] 3D neighbors
def getneighbors(pt):
	first=[pt[0]-1,pt[0],pt[0]+1]
	second=[pt[1]-1,pt[1],pt[1]+1]
	third=[pt[2]-1,pt[2],pt[2]+1]
	
	allneighbors=[]
	for i in first:
		for j in second:
			for k in third:
				if (i,j,k) != pt:#dont append the point itself
					allneighbors.append((i,j,k))
	return(allneighbors)

def hashstayhash(coords):#define a function to do what happens for existing hash marks
	for key in coords.keys():
		#generate all neighbors
		neighbors=getneighbors(key)

		for i in neighbors:#iterating over all neighbors add +1 to count if it sees an existing hash mark
			if i in coords.keys():
				coords[key]+=1
	newcoords=dict()
	for k,v in coords.items():#append that point to outlist only if count is 2 or 3 according to rules
		if v == 2 or v == 3:
			newcoords[k]=0
	return(newcoords)
	
def blankturnhash(coords):#define a function to do what happens for empty points
	neighborcount=[]
	for key in coords.keys():
		#generate all neighbors
		neighbors=getneighbors(key)

		for i in neighbors:#iterating over all neighbors add to list whenever a given point is a space with a hash mark
			if i not in coords.keys():#ignore existing hashes
				neighborcount.append(i)
	newhahses0=Counter(neighborcount)#now count how many times a hash mark was a neighbor to a point
	newhashes=dict()
	for k,v in newhahses0.items():#if the amount of time is exactly 3 then output
		if v == 3:
			newhashes[k]=0
	return(newhashes)		

###
# Run it
###

cnt=1
while cnt<=6:##Run everything for 6 cycles
	mycoords={**hashstayhash(mycoords),**blankturnhash(mycoords)} #create a single dictionary of only hash marks
	print(len(mycoords.keys()))
	cnt+=1

