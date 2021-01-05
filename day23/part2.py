#the big idea here is to consider each cup's neighbor
#for each iteration only 3 cups actually change neighbors:
#-the current cup
#-the destination cup
#-the last cup in the pickup set
#So updating 3 values in a dictionary is faster than updating each index in a list or deque
#I definitely didn't arrive at this solution on my own, I googled around for tips

import sys
import time

#input="389125467" #test case
input="538914762" #puzzle input

inlist=[int(x) for x in list(input)] #convert to a list of integers
inlist=inlist + list(range(max(inlist)+1,1000000+1)) #add numbers to a million

indict=dict()#dictionary storing the next number
for i in range(len(inlist)):
	if i < len(inlist)-1:
		indict[inlist[i]]=inlist[i+1]
	else:
		indict[inlist[i]]=inlist[0]

listlen=len(inlist)#get this outside of loop
moves=1 #keep track of moves
thenum=inlist[0]#initial value of current number per iteration
startsec = time.time() #start the clock

#while moves<=10:
#while moves<=100:
while moves<=10000000:
	if moves % 2000000==0:#print out info periodically
		print("\n-- Move:",moves,"---")
		print("Time Elapsed:",round(time.time()-startsec,3))
		print("Current number:",thenum)
	#print("Cups:",thenum,indict[thenum],indict[indict[thenum]],indict[indict[indict[thenum]]],indict[indict[indict[indict[thenum]]]],indict[indict[indict[indict[indict[thenum]]]]],indict[indict[indict[indict[indict[indict[thenum]]]]]],indict[indict[indict[indict[indict[indict[indict[thenum]]]]]]],indict[indict[indict[indict[indict[indict[indict[indict[thenum]]]]]]]])
	
	pickup=[indict[thenum],indict[indict[thenum]],indict[indict[indict[thenum]]]] #the three cup next to the current number
	#print("Pickup:",pickup)

	#for val in pickup:#remove these values
	#	inlist.remove(val)

	if listlen not in pickup: #rigamarole to find max and min without pickup cup
		themax=listlen
	elif listlen-1 not in pickup:
		themax=listlen-1
	elif listlen-2 not in pickup:
		themax=listlen-2
	else:
		themax=listlen-3
		
	if 1 not in pickup:
		themin=1
	elif 2 not in pickup:
		themin=2
	elif 3 not in pickup:
		themin=3
	else:
		themin=4

	destinationval=thenum-1 #get the destination value, initially set to current number -1
	if destinationval in pickup: #deal with destination value when its in the pickups
		while destinationval in pickup:
			destinationval-=1
	if destinationval<themin:#deal with destination value when it gets too small
		destinationval=themax
	#print("Destination Value:",destinationval)

	#update dictionary - only 3 keys have a new clockwise neighbor every turn
	indict[thenum]=indict[indict[indict[indict[thenum]]]] #set clockwise neighbor for the current cup
	indict[pickup[-1]]=indict[destinationval] #set clockwise neighbor for the last cup in the pickups
	indict[destinationval]=pickup[0] #set clockwise neighbor for the destination cup

	thenum=indict[thenum] #iterate to the next number
	moves+=1 #increment

print("\nCups:",thenum,indict[thenum],indict[indict[thenum]],indict[indict[indict[thenum]]],indict[indict[indict[indict[thenum]]]],indict[indict[indict[indict[indict[thenum]]]]],indict[indict[indict[indict[indict[indict[thenum]]]]]],indict[indict[indict[indict[indict[indict[indict[thenum]]]]]]],indict[indict[indict[indict[indict[indict[indict[indict[thenum]]]]]]]])
print(indict[1],indict[indict[1]])
print("Final Answer:",indict[1]*indict[indict[1]])
print("Total Time Elapsed:",round(time.time()-startsec,3))
