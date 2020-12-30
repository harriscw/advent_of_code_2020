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

cornerkeys=[3467, 3169, 1019, 1249]
borderkeys=[3461, 1613, 2137, 1511, 1951, 2081, 1499, 1871, 2689, 1789, 1777, 1129, 1097, 1283, 1229, 3761, 1373, 2707, 2411, 1549, 2459, 2719, 1583, 3413, 1301, 2711, 2161, 1039, 3301, 1801, 2029, 2129, 1171, 2963, 3833, 1399, 3511, 1151, 1453, 1607]

#Match: 1019 orientation: normal rotation: 2
totalrow=np.rot90(np.array(tiles[1019]),k=2) #I used this for both the left and right borders
#totalrow=np.array(tiles[3467])

cnt=1
checkthesekeys=borderkeys+cornerkeys
while cnt<12:	
	foundit=False
	rotation=orientation=finalmat=theind=""
	
	for checkind in checkthesekeys:
		if foundit==False:
			#print(np.array(tiles[checkind]))
			outmat=np.array(tiles[checkind])# check normal
			for therotation in [0,1,2,3]:#rotate to check each border matching
				if (totalrow[0,:]==np.rot90(outmat,k=therotation)[-1,:]).all():# 90 degree rotation
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
				if (totalrow[0,:]==np.rot90(outmat,k=therotation)[-1,:]).all():# 90 degree rotation
					orientation="hflip"
					rotation=therotation
					print("Match:",checkind,"orientation:",orientation,"rotation:",rotation)
					#print(totalrow)
					#print(np.rot90(outmat,k=therotation))
					theind=checkind
					foundit=True
					finalmat=np.rot90(outmat,k=therotation)
					
		if foundit==False:	
			outmat=np.flip(np.array(tiles[checkind]),axis=1)# check horizontal flip
			for therotation in [0,1,2,3]:#rotate to check each border matching
				if (totalrow[0,:]==np.rot90(outmat,k=therotation)[-1,:]).all():# 90 degree rotation
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
	totalrow=np.vstack((finalmat,totalrow))
	checkthesekeys.remove(theind)
	cnt+=1

outlist=totalrow.tolist()
mylist=[]
for i in range(len(outlist)):
	mylist.append("".join(outlist[i]))

for i in mylist:
	print(i)



