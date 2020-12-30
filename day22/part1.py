import sys

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()

player1=[]#read in a list of cards for both players
player2=[]
for line in lines:
	thisline=line.strip("\n")
	if thisline=="Player 1:":#once "Player 1:" is seen append numbers to that list
		dop1=True
		continue
	elif thisline=="Player 2:":#once "Player 2:" is seen append numbers to that list
		dop1=False
		continue
	elif thisline=="":#ignore the line with the space
		continue
	elif dop1==True:
		player1.append(int(thisline))
	else:
		player2.append(int(thisline))
		
print(player1)
print(player2)

cnt=1#round counter
while min(len(player1),len(player1))>0:#play the game until one player has no cards
	print("round",cnt,player1[0],"vs.",player2[0])
	player1.pop(0) #remove the first item in both lists
	player2.pop(0)
	if player1[0]>player2[0]:#if player 1 wins add both cards to their list
		player1=player1+[player1[0],player2[0]]
	elif player1[0]<player2[0]:#if player 2 wins add both cards to their list
		player2=player2+[player2[0],player1[0]]
	cnt+=1
	
if len(player1)>0:
	print("Player 1 wins!",player1)
	finaldeck=player1#save the dinal deck to a new object so you can calculate the final score
else:
	print("Player 2 wins!",player2)
	finaldeck=player2

weight=len(finaldeck)
points=0
for i in finaldeck:#final score is the sum of the weighted cards
	points+=i*weight
	weight-=1

print("Final Answer:",points)