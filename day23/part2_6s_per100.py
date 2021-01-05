import sys
import itertools
from collections import deque
import time




input="389125467" #test case
#input="538914762" #puzzle input

inlist=[int(x) for x in list(input)] #convert to a list of integers
print(inlist)
inlist=inlist + list(range(max(inlist),1000000+1))
inlist=deque(inlist)
#print(inlist)
moves=1 #keep track of moves
i=0 #iterator
startsec = time.time() #start the clock
#while moves<=10:
#while moves<=100:
while moves<=10000000:
	
	if moves % 100==0:
		print("\n-- Move:",moves,"Iterator:",i,"---")
		print("Time Elapsed:",round(time.time()-startsec,3))
		#print("cups",inlist)
	
	thenum=inlist[i]
	inlist.rotate(-inlist.index(thenum)-1) #rotate so pickup is first 3 cards
	pickup=(list(itertools.islice(inlist, 0, 3)))
	#print("pick up:",pickup)
	
	inlist.popleft()
	inlist.popleft()
	inlist.popleft()
	
	destinationval=thenum-1 #get the destination value
	
	if destinationval<min(inlist):#deal with destination value when it gets too small
		destinationval=max(inlist)
	elif destinationval in pickup: #deal with destination value when its in the pickups
		while destinationval in pickup:
			destinationval-=1
			if destinationval<min(inlist):
				destinationval=max(inlist)
				break
	
	#print("Destination Value:",destinationval)
	destinationind=inlist.index(destinationval) #get index of destination
	#print("Destination Index:",destinationind)
	inlist.rotate(-inlist.index(destinationval)-1)#rotate so insertion destination is at the front

	pickup.reverse()
	inlist.extendleft(deque(pickup))#insert pickup at destination

	#print("Current number new index:",inlist.index(thenum))
	inlist.rotate(-inlist.index(thenum)+i)

	i+=1 #increment
	if i==len(inlist): #go back to the begining once you hit the end
		i=0
	moves+=1 #increment


inlist.rotate(-inlist.index(1)-1)
print("\nOut Rotated:",inlist)
first2=list(itertools.islice(inlist, 0, 2))
print("Final Answer:",first2[0]*first2[1])
print("Total Time Elapsed:",round(time.time()-startsec,3))
#for the final answer I just eyeballed it instead of programming it