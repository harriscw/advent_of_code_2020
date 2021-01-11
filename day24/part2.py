import sys

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

#parse instructions
dirlist=[]
for line in mylist: 
	newline=line.replace("se","se,").replace("sw","sw,").replace("ne","ne,").replace("nw","nw,").replace("ws","w,s").replace("wn","w,n").replace("es","e,s").replace("en","e,n").replace("ee","e,e,").replace("ew","e,w,").replace("ww","w,w,").replace("we","w,e,")#I'm probably a bad person for parsing it this way but here we are
	newline=list(filter(None, newline.split(",")))#split string on , then filter out missing
	dirlist.append(newline)

def newpoint(current,instruction):#function to move in a hexagonal grid
	if instruction=="e":
		outpoint=[current[0]+1,current[1]]
	elif instruction=="w":
		outpoint=[current[0]-1,current[1]]
	elif instruction=="ne":
		outpoint=[current[0]+.5,current[1]+1]
	elif instruction=="se":
		outpoint=[current[0]+.5,current[1]-1]
	elif instruction=="nw":
		outpoint=[current[0]-.5,current[1]+1]
	elif instruction=="sw":
		outpoint=[current[0]-.5,current[1]-1]
	return outpoint

def getneighbors(point):
	return([
	[point[0]+1,point[1]],#east
	[point[0]-1,point[1]],#west
	[point[0]+.5,point[1]+1],#northeast
	[point[0]+.5,point[1]-1],#southeast
	[point[0]-.5,point[1]+1],#northwest
	[point[0]-.5,point[1]-1] #southeast
	])

flipped=[]
for line in dirlist:#execute all instructions
	position=[0,0]
	for dir in line:#do instruction one by one
		position=newpoint(position,dir)
	if position in flipped:#if the tile is already flipped to black remove it from list
		flipped.remove(position)
	else:
		flipped.append(position)#otherwise append it to the list of flipped tiles


i=1
while i<=100:
	neighbordict=dict()
	blacktowhite=[]
	whitetoblack=[]
	allneighbors=[]
	for point in flipped:#iterate over all the black tiles
		blackneighbors=0
		allneighbors=allneighbors+getneighbors(point) #get a list of all the neighbors
		for neighbor in getneighbors(point): #for each neighbor of the black tile see if its also black
			if neighbor in flipped:#if so add 1
				blackneighbors+=1
		if blackneighbors == 0 or blackneighbors > 2:#add to list of all the black tiles that should be flipped to white
			blacktowhite.append(point)
	#now find white tiles that should be flipped
	for point in allneighbors:#for all neighbors of a black tile count how many of its neighbors are black
		blackneighbors=0
		for neighbor in getneighbors(point): 
			if neighbor in flipped:#if so add 1
				blackneighbors+=1
		if blackneighbors == 2:#add to list of all the black tiles that should be flipped to white
			whitetoblack.append(point)
			
	for point in blacktowhite:#remove tiles from flipped
		flipped.remove(point)
	flipped += whitetoblack#add the white to blacks
	flipped=[list(x) for x in set(tuple(x) for x in flipped)]#get unique values
	print("Number of black tiles after day",i,":",len(flipped))
	i+=1









