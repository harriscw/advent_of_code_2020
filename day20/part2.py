import sys
import numpy as np
import re

filename="fullstring.txt"
text_file = open(filename, "r") #read in the puzzle I previously assembled
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	thisline=lines[i].strip("\n")
	mylist.append(list(thisline))
	
mymat=np.array(mylist)
print(mymat.shape)

if filename =="fullstring.txt":#don't need to drop these in the sample input
	dropthese=[0,9,10,19,20,29,30,39,40,49,50,59,60,69,70,79,80,89,90,99,100,109,110,119] #drop the borders
	mymat=np.delete(mymat,dropthese,axis=0) #delete rows
	mymat=np.delete(mymat,dropthese,axis=1) #delete cols

print(mymat.shape)
print(len(mymat.tolist()))

###try transformations to find right orientation to actually find the sea dragons
#mymat=np.rot90(mymat,k=-1)
#mymat=np.flip(mymat,axis=0) #hflip
#mymat=np.rot90(mymat,k=3)
mymat=np.flip(mymat,axis=1) #vflip
#mymat=np.rot90(mymat,k=3)

mylist=mymat.tolist()#convert from numpy array to a list of strings
newlist=[]
cnt=0
for myrow in mylist:
	newlist.append("".join(myrow))
	print(cnt,":","".join(myrow))
	cnt+=1
	
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
	
string1 ="(?=(..................#.))"#define regular expressions for sea monster strings
string2 ="(?=(#....##....##....###))"#?= is a look ahead that I think is needed to find overlapping matches, not just the first.
string3 ="(?=(.#..#..#..#..#..#...))"


cnt=0
match1=dict()#create 3 different dictionaries, one for each string I need to match.
match2=dict()
match3=dict()
for line in newlist:
	mymatch1=[(m.start(0)) for m in re.finditer(string1, line)] #for a given line find all starting indicies of a regex match
	mymatch2=[(m.start(0)) for m in re.finditer(string2, line)]
	mymatch3=[(m.start(0)) for m in re.finditer(string3, line)]
	if len(mymatch1)>0:
		match1[cnt]=mymatch1#store the match in the appropriate dictionary where the key is the line number from the image
	if len(mymatch2)>0:
		match2[cnt]=mymatch2
	if len(mymatch3)>0:
		match3[cnt]=mymatch3		
	cnt+=1

print(match1.keys())
print(match2.keys())
print(match3.keys())

cnt=0 #this code now counts sea dragons for the given orientation
for key in match2.keys():#iterating over the keys in the match2 dictionary because there are the fewest
	if key-1 in match1 and key in match2 and key+1 in match3:#if 3 consecutive keys match string1,2,and 3
		print(key-1,":",match1[key-1])
		print(key,":",match2[key])
		print(key+1,":",match3[key+1])
		print()
		for match2key in match2[key]:#for each index of string start in match 2 
			if match2key in match1[key-1] and match2key in match3[key+1]: #see if that index is also in the line above and below
				cnt+=1 #if so add 1 to the count

print("Number of sea monsters:",cnt)
		
#get count of # symbols
cntlist=[]
for line in newlist:
	cntlist.append(line.count("#"))

print("Final Answer:",sum(cntlist)-(15*cnt)) #there are 15 # in the sea monster



