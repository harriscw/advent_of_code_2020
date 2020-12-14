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

#general instructions	
	if instruc[0:1]=="N":
		mypos[0]+=int(instruc[1:])
	elif instruc[0:1]=="S":
		mypos[0]-=int(instruc[1:])
	elif instruc[0:1]=="E":
		mypos[1]+=int(instruc[1:])
	elif instruc[0:1]=="W":
		mypos[1]-=int(instruc[1:])
		
#instructions are dependent on which way the boat is facing
	elif instruc[0:1]=="F":
		if mypos[2]=="N":
			mypos[0]+=int(instruc[1:])
		elif mypos[2]=="S":
			mypos[0]-=int(instruc[1:])
		elif mypos[2]=="E":
			mypos[1]+=int(instruc[1:])
		elif mypos[2]=="W":
			mypos[1]-=int(instruc[1:])
			
#instructions to change the direction of the boat
	else:
		steps=int(instruc[1:])/90 #number of steps for iterator
		mydirs=["E","S","W","N"] #set directions in order
		if instruc[0:1]=="L": #reverse as needed
			mydirs.reverse()
		mydirs=cycle(mydirs) #use a cyclical iteraotr.  ugh I accidentally indented this line and it took me forever to debug
		seen=False
		stepdone=0
		for direction in mydirs:
			if direction==mypos[2]: #start keeping track after the current direction is seen
				seen=True
			if seen==True:
				stepdone+=1
			if stepdone>steps:# stop after the number of steps is done
				mypos[2]=direction
				break

print(mypos)			
print("Manhattan Distance: ",abs(mypos[0])+abs(mypos[1]))	
sys.exit("Stop!")				
	

