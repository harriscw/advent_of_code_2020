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

#I generated rows manually like a bad person starting with each left border piece 
#I pasted the results into a text file again like a bad person
#But it was helpful for ensuring that things matched

#totalrow=np.rot90(np.flip(np.array(tiles[1951]),axis=0),k=1)
#totalrow=np.rot90(np.array(tiles[1171]),k=3)
#totalrow=np.rot90(np.array(tiles[1511]),k=3)
#totalrow=np.rot90(np.array(tiles[1151]),k=3)
#totalrow=np.rot90(np.array(tiles[3461]),k=3)
#totalrow=np.rot90(np.flip(np.array(tiles[1613]),axis=0),k=3)
#totalrow=np.flip(np.array(tiles[1789]),axis=0)
#totalrow=np.rot90(np.array(tiles[2707]),k=1)
#totalrow=np.rot90(np.array(tiles[2963]),k=2)
#totalrow=np.rot90(np.array(tiles[1607]),k=3)
totalrow=np.rot90(np.array(tiles[1249]),k=1)

#Match: 1951 orientation: hflip rotation: 1
#Match: 1171 orientation: normal rotation: 3
#Match: 1511 orientation: normal rotation: 3
#Match: 1151 orientation: normal rotation: 3
#Match: 3461 orientation: normal rotation: 3
#Match: 1613 orientation: hflip rotation: 3
#Match: 1789 orientation: hflip rotation: 0
#Match: 2707 orientation: normal rotation: 1
#Match: 2963 orientation: normal rotation: 2
#Match: 1607 orientation: normal rotation: 3
#Match: 1249 orientation: normal rotation: 1


cnt=1
checkthesekeys=borderkeys
#checkthesekeys=np.setdiff1d(list(tiles.keys()),cornerkeys+borderkeys).tolist()
print(totalrow)
print(len(checkthesekeys))

while cnt<11:	
	foundit=False
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
	totalrow=np.hstack((totalrow,finalmat))
	checkthesekeys.remove(theind)
	cnt+=1


outlist=totalrow.tolist()

mylist=[]
for i in range(len(outlist)):
	mylist.append("".join(outlist[i]))

for i in mylist:
	print(i)
	
sys.exit()
