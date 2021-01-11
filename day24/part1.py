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

flipped=[]
for line in dirlist:#execute all instructions
	position=[0,0]
	for dir in line:#do instruction one by one
		position=newpoint(position,dir)
	if position in flipped:#if the tile is already flipped to black remove it from list
		flipped.remove(position)
	else:
		flipped.append(position)#otherwise append it to the list of flipped tiles

print("Number of black tiles:",len(flipped))
		