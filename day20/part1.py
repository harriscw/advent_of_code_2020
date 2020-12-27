import sys
import numpy as np

text_file = open("input.txt", "r") #read data
lines = text_file.readlines()
tiles=dict()
for i in range(len(lines)):
	thisline=lines[i].strip("\n")
	if thisline[0:4]=="Tile":#capture key
		thekey=int(thisline.strip(":").strip("Tile "))
		tiles[thekey]=[]
	elif thisline != '':#write picture to dictionary
		tiles[thekey].append(list(thisline))	

#General approach: lets find the 4 tiles that have the least amount of shared borders with other pieces and call them the corners

def getborders(mykey):#function for getting normal borders
	myarray=np.array(mykey)
	top=''.join(myarray[0,:])
	bottom=''.join(myarray[len(myarray)-1,:])
	lside=''.join(myarray[:,0])
	rside=''.join(myarray[:,len(myarray)-1])
	return([top,rside,bottom,lside])
	
def hflip(myborders): #borders horizontally flipped
	return([myborders[0][::-1],myborders[3],myborders[2][::-1],myborders[1]])

def vflip(myborders): #borders vertically flipped
	return([myborders[2],myborders[1][::-1],myborders[0],myborders[3][::-1]])
	
#Now iterate over each piece and count number of shared borders
thekeys=list(tiles.keys())
countdict=dict()
for primarykey in thekeys:#iterate over pieces
	print("Checking Key:",primarykey)
	matchlist=[]
	for checkkey in thekeys:#compare to all other pieces
		if primarykey != checkkey: #dont check a piece's borders with itself
			normalnormal=len(set(getborders(tiles[primarykey])) & set(getborders(tiles[checkkey])))
			normalhflip=len(set(getborders(tiles[primarykey])) & set(hflip(getborders(tiles[checkkey]))))
			normalvflip=len(set(getborders(tiles[primarykey])) & set(vflip(getborders(tiles[checkkey]))))
			
			hflipnormal=len(set(hflip(getborders(tiles[primarykey]))) & set(getborders(tiles[checkkey])))
			hfliphflip=len(set(hflip(getborders(tiles[primarykey]))) & set(hflip(getborders(tiles[checkkey]))))
			hflipvflip=len(set(hflip(getborders(tiles[primarykey]))) & set(vflip(getborders(tiles[checkkey]))))
			
			vflipnormal=len(set(vflip(getborders(tiles[primarykey]))) & set(getborders(tiles[checkkey])))
			vfliphflip= len(set(vflip(getborders(tiles[primarykey]))) & set(hflip(getborders(tiles[checkkey]))))
			vflipvflip= len(set(vflip(getborders(tiles[primarykey]))) & set(vflip(getborders(tiles[checkkey]))))
			
			#sum all the shared borders
			matchlist.append(normalnormal+normalhflip+normalvflip+hflipnormal+hfliphflip+hflipvflip+vflipnormal+vfliphflip+vflipvflip)
	
	countdict[primarykey]=(len(thekeys)-1)-matchlist.count(0)#add shared border count to dictionary

#Now lets find the pieces with the lowest number of shared borders
min_val = min(countdict.values())
min_keys=[k for k, v in countdict.items() if v == min_val]
print("Corner Keys:",min_keys)

myproduct = 1#multiply these corners together.  Is there a better way to get a list product without importing a module??
for item in min_keys:
	myproduct = myproduct * item
print("Final Answer:",myproduct)

sys.exit("stop!")