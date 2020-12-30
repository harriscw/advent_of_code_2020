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

print("Number of tiles:",len(tiles.keys()))#144 so 12x12

# These are obtained from part 1
cornerkeys=[3467, 3169, 1019, 1249]
borderkeys=[3461, 1613, 2137, 1511, 1951, 2081, 1499, 1871, 2689, 1789, 1777, 1129, 1097, 1283, 1229, 3761, 1373, 2707, 2411, 1549, 2459, 2719, 1583, 3413, 1301, 2711, 2161, 1039, 3301, 1801, 2029, 2129, 1171, 2963, 3833, 1399, 3511, 1151, 1453, 1607]

keepgoing=True
lastind=3467 #start with a corner piece
totalrow=np.array(tiles[lastind])
cnt=1
checkthesekeys=borderkeys+cornerkeys

while cnt<12: #check other border pieces for a match against existing piece, append it, iterate until you have 12 pieces across
	foundit=Falses
	rotation=orientation=finalmat=theind=""
	for checkind in checkthesekeys:
	
		if foundit==False:
			#print(np.array(tiles[checkind]))
			outmat=np.array(tiles[checkind])# check normal
			for therotation in [0,1,2,3]:#rotate to check each border matching
				if (totalrow[:,-1]==np.rot90(outmat,k=therotation)[:,0]).all():# 90 degree rotation
					orientation="normal"
					rotation=therotation
					print("Match:",checkind,"orientation:",orientation,"rotation:",rotation)
					#print(totalrow)
					#print(np.rot90(outmat,k=therotation))
					theind=checkind
					foundit=True
					finalmat=np.rot90(outmat,k=therotation)
					
		if foundit==False:	
			outmat=np.flip(np.array(tiles[checkind]),axis=0)# check horizontal flip
			for therotation in [0,1,2,3]:#rotate to check each border matching
				if (totalrow[:,-1]==np.rot90(outmat,k=therotation)[:,0]).all():# 90 degree rotation
					orientation="hflip"
					rotation=therotation
					#sys.exit("Stop!")
					print("Match:",checkind,"orientation:",orientation,"rotation:",rotation)
					#print(totalrow)
					#print(np.rot90(outmat,k=therotation))
					theind=checkind
					foundit=True
					finalmat=np.rot90(outmat,k=therotation)
					
		if foundit==False:	
			outmat=np.flip(np.array(tiles[checkind]),axis=1)# check horizontal flip
			for therotation in [0,1,2,3]:#rotate to check each border matching
				if (totalrow[:,-1]==np.rot90(outmat,k=therotation)[:,0]).all():# 90 degree rotation
					orientation="vflip"
					rotation=therotation
					print("Match:",checkind,"orientation:",orientation,"rotation:",rotation)
					#print(totalrow)
					#print(np.rot90(outmat,k=therotation))
					theind=checkind
					foundit=True
					finalmat=np.rot90(outmat,k=therotation)

	#print(totalrow)
	#print(finalmat)		
	totalrow=np.hstack((totalrow,finalmat)) #append horizontally
	checkthesekeys.remove(theind) #don't check this one in the future
	cnt+=1


outlist=totalrow.tolist() #change from numpy array to list

mylist=[]
for i in range(len(outlist)):
	mylist.append("".join(outlist[i])) #join into a list of single string per row

for i in mylist: #print out for me to manually copy to a text file (yes I know I'm a bad person)
	print(i)
	
sys.exit()


