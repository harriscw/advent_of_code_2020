import csv
import sys
import numpy as np

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(list(lines[i].strip("\n")))
	
#print(mylist)

mymatrix=np.array([np.array(xi) for xi in mylist])
print(mymatrix)

X = mymatrix.shape[0]#rows
Y = mymatrix.shape[1]#columns




#Define a function to get all the seats (either L or #) that can be seen from a given seats
#ie get indicies of Ls and #s a given seat can see in 8 directions

def cansee(therow,thecol):
	canseeinds=[]
	
		# vertically down
	for rowiter in range(therow+1,X):
		if mymatrix[rowiter,thecol]=="L" or mymatrix[rowiter,thecol]=="#":
			canseeinds.append((rowiter,thecol))
			break	
			
		# vertically up
	if therow>0:
		for rowiter in range(therow-1, -1, -1):
			if mymatrix[rowiter,thecol]=="L" or mymatrix[rowiter,thecol]=="#":
				canseeinds.append((rowiter,thecol))
				break
	
		# horizontally right
	for coliter in range(thecol+1,Y):
		if mymatrix[therow,coliter]=="L" or mymatrix[therow,coliter]=="#":
			canseeinds.append((therow,coliter))
			break
	
		# horizontally left
	if thecol>0:
		for coliter in range(thecol-1, -1, -1):
			if mymatrix[therow,coliter]=="L" or mymatrix[therow,coliter]=="#":
				canseeinds.append((therow,coliter))
				break
	
	###
	#diag down right
	###
	# get indicies to check
	myinds=[]
	xpos=therow
	ypos=thecol
	for myiter in range(therow,X):
		xpos+=1
		ypos+=1
		if xpos>X-1 or xpos<0 or ypos>Y-1 or ypos<0:
			break
		else:
			myinds.append([xpos,ypos])
	# find the first L or # in that direction
	for myind in myinds:
		if mymatrix[myind[0],myind[1]]=="L" or mymatrix[myind[0],myind[1]]=="#":
			canseeinds.append((myind[0],myind[1]))
			break
			
	###
	#diag up right
	###
	# get indicies to check
	myinds=[]
	xpos=therow
	ypos=thecol
	for myiter in range(therow,0,-1):
		xpos-=1
		ypos+=1
		if xpos>X-1 or xpos<0 or ypos>Y-1 or ypos<0:
			break
		else:
			myinds.append([xpos,ypos])
	# find the first L or # in that direction
	for myind in myinds:
		if mymatrix[myind[0],myind[1]]=="L" or mymatrix[myind[0],myind[1]]=="#":
			canseeinds.append((myind[0],myind[1]))
			break
	
	###
	#diag down left
	###
	#get indicies to check
	myinds=[]
	xpos=therow
	ypos=thecol
	for myiter in range(therow,X,1):
		xpos+=1
		ypos-=1
		if xpos>X-1 or xpos<0 or ypos>Y-1 or ypos<0:
			break
		else:
			myinds.append([xpos,ypos])
	# find the first L or # in that direction
	for myind in myinds:
		if mymatrix[myind[0],myind[1]]=="L" or mymatrix[myind[0],myind[1]]=="#":
			canseeinds.append((myind[0],myind[1]))
			break
	
	###
	#diag up left
	###
	
	##get indicies to check
	myinds=[]
	xpos=therow
	ypos=thecol
	for myiter in range(therow,0,-1):
		xpos-=1
		ypos-=1
		if xpos>X-1 or xpos<0 or ypos>Y-1 or ypos<0:
			break
		else:
			myinds.append([xpos,ypos])
	# find the first L or # in that direction
	for myind in myinds:
		if mymatrix[myind[0],myind[1]]=="L" or mymatrix[myind[0],myind[1]]=="#":
			canseeinds.append((myind[0],myind[1]))
			break
			
	return canseeinds

# test a point
#print(cansee(1,9))


## Now rerun prior code from part 1.
## For a given point check if its a # or an Lcount
## get a count of #s and Ls for a given point
## apply the change rules accordingly

mychanges=1
cnt=0
while mychanges>0:
	cnt+=1
	print(cnt)
	changeind =[]
	for myrow in range(mymatrix.shape[0]):#iterate over each row
		for mycol in range(mymatrix.shape[1]):#iterate over each column
			neighborind=cansee(myrow,mycol) #get all the indicies that point can see using prior function
			if mymatrix[myrow,mycol]=="L": # if the seat is empty...
				Lcount=0
				for k in range(len(neighborind)): #...then count the empty seats of those they can see
					Lcount += mymatrix[neighborind[k][0],neighborind[k][1]]=="#"
				if Lcount==0: #if no #s can be seen then add to list of seats that will change
					changeind.append([myrow,mycol])
			elif mymatrix[myrow,mycol]=="#": #if the seat is full...
				hashcount=0
				for k in range(len(neighborind)):
					hashcount += mymatrix[neighborind[k][0],neighborind[k][1]]=="#"
				if hashcount>=5:#if 5 or more occupied seats can be seen then add to list of seats that will change
					changeind.append([myrow,mycol])
	mychanges=len(changeind)#number of changes to feed back to while loop				
	for coord in changeind: #make the changes
		if mymatrix[coord[0],coord[1]]=="L":
			mymatrix[coord[0],coord[1]]="#"
		elif mymatrix[coord[0],coord[1]]=="#":
			mymatrix[coord[0],coord[1]]="L"

unique, counts = np.unique(mymatrix, return_counts=True)
print(dict(zip(unique, counts)))
	
#sys.exit("Stop!")				
	

