import sys
from itertools import cycle

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

#print(mylist)

mypos = [0,0,"E"]

for instruc in mylist:
	print(mypos)
	print(instruc)
	
	if instruc[0:1]=="N":
		mypos[0]+=int(instruc[1:])
	elif instruc[0:1]=="S":
		mypos[0]-=int(instruc[1:])
	elif instruc[0:1]=="E":
		mypos[1]+=int(instruc[1:])
	elif instruc[0:1]=="W":
		mypos[1]-=int(instruc[1:])
	elif instruc[0:1]=="F":
		if mypos[2]=="N":
			mypos[0]+=int(instruc[1:])
		elif mypos[2]=="S":
			mypos[0]-=int(instruc[1:])
		elif mypos[2]=="E":
			mypos[1]+=int(instruc[1:])
		elif mypos[2]=="W":
			mypos[1]-=int(instruc[1:])
	else:
		steps=int(instruc[1:])/90
		mydirs=["E","S","W","N"]
		if instruc[0:1]=="L":
			mydirs.reverse()
		mydirs=cycle(mydirs) #ugh I accidentally indented this line and it took me forever to debug
		seen=False
		stepdone=0
		for direction in mydirs:
			if direction==mypos[2]:
				seen=True
			if seen==True:
				stepdone+=1
			if stepdone>steps:
				mypos[2]=direction
				break

print(mypos)			
print("Manhattan Distance: ",abs(mypos[0])+abs(mypos[1]))	
sys.exit("Stop!")				
	

