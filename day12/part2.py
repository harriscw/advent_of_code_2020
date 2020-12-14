import sys
from itertools import cycle
import numpy as np

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

#Function to rotate coordinates that I stole from stackoverflow
def rotate(p, origin=(0, 0), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T-o.T) + o.T).T)

mypos = [0,0] #initial ship position
wppos = [1,10] #initial waypoint position

for instruc in mylist:
	print("Ship: ",mypos)
	print("Waypoint: ",wppos)
	print(instruc)

#general instructions	
	if instruc[0:1]=="F":
		mypos[0]+=int(instruc[1:])*wppos[0] #North/South
		mypos[1]+=int(instruc[1:])*wppos[1] #East/West
	elif instruc[0:1]=="N":
		wppos[0]+=int(instruc[1:])
	elif instruc[0:1]=="S":
		wppos[0]-=int(instruc[1:])
	elif instruc[0:1]=="E":
		wppos[1]+=int(instruc[1:])
	elif instruc[0:1]=="W":
		wppos[1]-=int(instruc[1:])	

	#rotate the waypoint
	elif instruc[0:1]=="R":
		wppos = rotate(p=wppos,degrees=int(instruc[1:]))
	elif instruc[0:1]=="L":
		wppos = rotate(p=wppos,degrees=-int(instruc[1:]))
		
print(mypos)			
print("Manhattan Distance: ",abs(mypos[0])+abs(mypos[1]))	
	
sys.exit("Stop!")

