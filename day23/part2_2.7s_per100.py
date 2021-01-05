import sys
import itertools
from collections import deque
import time




input="389125467" #test case
#input="538914762" #puzzle input

inlist=[int(x) for x in list(input)] #convert to a list of integers
#print(inlist)
inlist=inlist + list(range(max(inlist),1000000+1))

indict=dict()#dictionary storing the next number
for i in range(len(inlist)):
	#print(i)
	if i < len(inlist)-1:
		indict[inlist[i]]=inlist[i+1]
	else:
		indict[inlist[i]]=inlist[0]
#print(indict)
listlen=len(inlist)
inlist=deque(inlist)





#print(inlist)
moves=1 #keep track of moves
i=0 #iterator

#while moves<=10:
#while moves<=100:

startsec = time.time() #start the clock
#while moves<=10:
#while moves<=100:
while moves<=10000000:
	
	if moves % 100==0:
		print("\n-- Move:",moves,"Iterator:",i,"---")
		print("Time Elapsed:",round(time.time()-startsec,3))
		#print("cups",inlist)
	thenum=inlist[i]
	
	pickup=[indict[thenum],indict[indict[thenum]],indict[indict[indict[thenum]]]]


	for val in pickup:#remove these values
		inlist.remove(val)
	
	destinationval=thenum-1 #get the destination value
	mininlist=min(inlist)
	if destinationval<mininlist:#deal with destination value when it gets too small
		destinationval=max(inlist)
	elif destinationval in pickup: #deal with destination value when its in the pickups
		while destinationval in pickup:
			destinationval-=1
			if destinationval<mininlist:
				destinationval=max(inlist)
				break
	
	
	#print("Destination Value:",destinationval)
	destinationind=inlist.index(destinationval)+1 #get index of destination
	#print("Destination Index:",destinationind)
	
	#update dictionary
	indict[thenum]=indict[indict[indict[indict[thenum]]]]
	indict[pickup[-1]]=indict[destinationval]
	indict[destinationval]=pickup[0]

	pickup.reverse()
	for num in pickup:
		inlist.insert(destinationind,num) #insert the pickup cards
	

	#print("Current number new index:",inlist.index(thenum))
	inlist.rotate(i-inlist.index(thenum))
	
	i+=1 #increment
	if i==listlen: #go back to the begining once you hit the end
		i=0
	moves+=1 #increment


inlist.rotate(-inlist.index(1)-1)
print("\nOut Rotated:",inlist)
first2=list(itertools.islice(inlist, 0, 2))
print("Final Answer:",first2[0]*first2[1])
print("Total Time Elapsed:",round(time.time()-startsec,3))
#for the final answer I just eyeballed it instead of programming it
