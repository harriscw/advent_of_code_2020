import sys
import time



input="389125467" #test case
input="538914762" #puzzle input

inlist=[int(x) for x in list(input)] #convert to a list of integers

inlist=inlist + list(range(max(inlist),1000000+1))
moves=1 #keep track of moves
i=0 #iterator

startsec = time.time() #start the clock
while moves<=10000001:#go to 10000001 so it displays the final value
	
	if i % 100 ==0:
		print("\n-- Move:",moves,"Iterator:",i,"---")
		print("Time Elapsed:",round(time.time()-startsec,3))
	#print("cups:",inlist)
	#print("this number:",inlist[i])
	
	#concatenate numbers before current iteration to numbers after current iteration
	#have the string start with numbers right after current iteration
	before=inlist[0:i]
	after=inlist[i+1:]
	splicelist=after+before
	#print("Spliced",splicelist)
	
	pickup=splicelist[0:3] #the cards you pick up
	#print("pick up:",pickup)
	
	for val in pickup:#remove these values
		splicelist.remove(val)
		
	destinationval=inlist[i]-1 #get the deistination value
	
	if destinationval<min(splicelist):#deal with destination value when it gets too small
		destinationval=max(splicelist)
	elif destinationval in pickup: #deal with destination value when its in the pickups
		while destinationval in pickup:
			destinationval-=1
			if destinationval<min(splicelist):
				destinationval=max(splicelist)
				break
	
	#print("Destination Value:",destinationval)
	destinationind=splicelist.index(destinationval)+1 #get index of destination
	#print("Destination Index:",destinationind)
	
	splicelist=splicelist[:destinationind] + pickup + splicelist[destinationind:] #insert the pickup cards
	inlist=splicelist[len(inlist)-i-1:]+[inlist[i]]+splicelist[0:len(inlist)-i-1] #now wrap to create the new list

	i+=1 #increment
	if i==len(inlist): #go back to the begining once you hit the end
		i=0
	moves+=1 #increment
	
#for the final answer I just eyeballed it instead of programming it