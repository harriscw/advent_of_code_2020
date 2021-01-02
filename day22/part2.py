import sys
import collections
import itertools
from datetime import datetime
import time

startsec = time.time() #start the clock

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()

myplayer1=[]#read in a list of cards for both players
myplayer2=[]
for line in lines:
	thisline=line.strip("\n").strip()
	if thisline=="Player 1:":#once "Player 1:" is seen append numbers to that list
		dop1=True
		continue
	if thisline=="Player 2:":#once "Player 2:" is seen append numbers to that list
		dop1=False
		continue
	if thisline=="":#ignore the line with the space
		continue
	if dop1==True:
		myplayer1.append(int(thisline))
	else:
		myplayer2.append(int(thisline))
		
#print(myplayer1)
#print(myplayer2)

myplayer1=collections.deque(myplayer1) #googled around for tips during debugging and saw lots of suggestions for deque
myplayer2=collections.deque(myplayer2) #so I thought I'd check it out

appendthese=dict() #create a global dictionary to keep the cards that will be appended after subgame resolution
gamecnt=1 #create a global game counter

def part2(player1,player2):
	global winner #make winner flag persistent across recursion
	global gamecnt #same with game count
	winner=""
	knownstrings=[] #known strings is not persistent (this was a little confusing)
	roundcnt=1#round counter
	finaldict=dict()#dictionary for final results
	
	while min(len(player1),len(player2))>0:#play the game until one player has no cards
		
		#print("previous winner:",winner,"Game:",gamecnt)
		if winner=="p1":#append cards if this round was decided by a subgame
			player1.extend(appendthese[gamecnt])
		elif winner=="p2":
			appendthese[gamecnt].reverse()
			player2.extend(appendthese[gamecnt])
		winner="" #reset to missing
		appendthese[gamecnt]=[] #reset to missing
		
		mytime=datetime.now().strftime('%M:%S')#this was for debugging to spit out some results every 10min
		if str(mytime)[-4:]=="1:00":#my code was running for a long time
			print("game:",gamecnt,"round:",roundcnt,mytime,player1[0],"vs.",player2[0])
			print("P1:",player1)#wasnt sure if I just needed to brute force or I was caught in an infinite loop
			print("P2:",player2)#turns out I was prob in an infinite loop
				
		thisstring="p1:"+','.join(str(e) for e in player1) + " p2:"+','.join(str(e) for e in player2) #log prior results	
		appendthese[gamecnt]=[player1[0],player2[0]]
		
		if thisstring not in knownstrings: #if we've never seen this hand before
			knownstrings.append(thisstring)
		
			p1num=player1[0] #define cards being played this hand
			p2num=player2[0]
			
			player1.popleft() #remove the first item in both lists
			player2.popleft()
			
			if not ((len(player1))>=p1num and (len(player2))>=p2num): #if you dont have enough to recurse play head to head
				
				if p1num>p2num:#if player 1 wins add both cards to their list
					player1.extend([p1num,p2num])
					#print("Player 1 wins the round!")
				elif p1num<p2num:#if player 2 wins add both cards to their list
					player2.extend([p2num,p1num])
					#print("Player 2 wins the round!")
			else: #otherwise recurse
				#print("Playing a sub-game to determine the winner...")
				#print("Numbers to append",appendthese[gamecnt])
				gamecnt+=1
				#print("\n=== Game",gamecnt,"===\n")
				newp1=collections.deque(itertools.islice(player1, 0, p1num)) #get the # of cards equal to the value this hand
				newp2=collections.deque(itertools.islice(player2, 0, p2num))
				part2(newp1,newp2)# recurse!
			
		else: #get into this condition if this hand has been seen before in this game
			#print("Player 1 wins by the duplication rule!")
			#player1.extend([player1[0],player2[0]])
			#player1.popleft() #remove the first item in both lists
			#player2.popleft()
			player2=[] #set this to missing so winner will be set as needed in if-else below. 
			break #If you get into this condition hands dont matter just win or lose
			
		roundcnt+=1
	finaldict["Player1"]=player1
	finaldict["Player2"]=player2
	if len(finaldict["Player1"])>0:
		#print("\n=== Player 1 wins! ===\n")
		winner="p1"
	else:
		#print("\n=== Player 2 wins! ===\n")
		winner="p2"
	gamecnt-=1		
	return(finaldict)

runit=part2(myplayer1,myplayer2)
print(runit)


if len(runit["Player1"])>0:
	finaldeck=runit["Player1"]
else:
	finaldeck=runit["Player2"]

weight=len(finaldeck)
points=0
for i in finaldeck:#final score is the sum of the weighted cards
	points+=i*weight
	weight-=1

print("Final Answer:",points)
print("Time Elapsed:",round(time.time()-startsec,3))