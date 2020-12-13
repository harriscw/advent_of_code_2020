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
#print(mymatrix)

X = mymatrix.shape[0]-1
Y = mymatrix.shape[1]-1

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]

mychanges=1
cnt=0
while mychanges>0:
	cnt+=1
	print(cnt)
	changeind =[]
	for myrow in range(mymatrix.shape[0]):
		for mycol in range(mymatrix.shape[1]):
			#print(mycol,mymatrix[myrow,mycol])
			if mymatrix[myrow,mycol]=="L":
				neighborind=neighbors(myrow,mycol)
				#print(neighborind)
				Lcount=0
				for k in range(len(neighborind)):
					
					#print(mymatrix[neighborind[k][0],neighborind[k][1]])
					Lcount += mymatrix[neighborind[k][0],neighborind[k][1]].count("#")
				#print(Lcount)
				if Lcount==0:
					changeind.append([myrow,mycol])
			if mymatrix[myrow,mycol]=="#":
				neighborind=neighbors(myrow,mycol)
				#print(neighborind)
				hashcount=0
				for k in range(len(neighborind)):
					
					#print(mymatrix[neighborind[k][0],neighborind[k][1]])
					hashcount += mymatrix[neighborind[k][0],neighborind[k][1]].count("#")
				#print(Lcount)
				if hashcount>=4:
					changeind.append([myrow,mycol])
	mychanges=0
	for coord in changeind:
		if mymatrix[coord[0],coord[1]]=="L":
			mymatrix[coord[0],coord[1]]="#"
			mychanges+=1
		elif mymatrix[coord[0],coord[1]]=="#":
			mymatrix[coord[0],coord[1]]="L"
			mychanges+=1
	#print(mymatrix)

unique, counts = np.unique(mymatrix, return_counts=True)
print(dict(zip(unique, counts)))
	
#sys.exit("Stop!")				
	

