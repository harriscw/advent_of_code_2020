import sys
import pandas as pd
import time
import math

# I did a lot of manual work here.
# I made bus*char manual based on the number necessary for the problem instead of a generalized porgramming solution
# Also I checked jumps by hand.  I checked the first time when DD is seen noting the time and the difference between occurences
# Then I increased the start point of the iterator to that time and increaed the iterator by the difference.
# the logic is that the final DDDDDDDD can only be seen if you first have DD*******.  So you can limit to check all the DD*******s.
# Similarly you can limit to check only the DDD******s then DDDD*****s.  I did this part manually instead of programatically.


#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

bus_string=mylist[1].split(",") #raw string with x's

# count each offset positions
offsets=[0]
xcnt=1
for i in range(1,len(bus_string)):
	if bus_string[i]=='x':
		xcnt+=1
	else:
		offsets.append(offsets[-1]+xcnt)
		xcnt=1
print(bus_string)		
print(offsets)

# create ongoing cycles for each bus
cyclelist=[]
for i in range(0,len(bus_string)):
	if bus_string[i] != 'x':
		cyclelist.append(['D'] + ['x']*(int(bus_string[i])-1))
print(cyclelist)
	
start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()

seen=False
mystart=26670649704
i=mystart
outlist=[]
while seen == False:
	print(i)
	bus0char=cyclelist[0][(i+offsets[0]) % len(cyclelist[0])]
	bus1char=cyclelist[1][(i+offsets[1]) % len(cyclelist[1])]
	bus2char=cyclelist[2][(i+offsets[2]) % len(cyclelist[2])]
	bus3char=cyclelist[3][(i+offsets[3]) % len(cyclelist[3])]
	bus4char=cyclelist[4][(i+offsets[4]) % len(cyclelist[4])]
	bus5char=cyclelist[5][(i+offsets[5]) % len(cyclelist[5])]
	bus6char=cyclelist[6][(i+offsets[6]) % len(cyclelist[6])]
	bus7char=cyclelist[7][(i+offsets[7]) % len(cyclelist[7])]
	bus8char=cyclelist[8][(i+offsets[8]) % len(cyclelist[8])]
		
	if i!=mystart and bus0char=="D" and bus1char=="D" and bus2char=="D" and bus3char=="D" and bus4char=="D" and bus5char=="D" and bus6char=="D" and bus7char=="D" and bus8char=="D": #last after 4
		#outlist.append(i)
		print("got it: ", i)
		print(bus0char,bus1char,bus2char,bus3char,bus4char,bus5char,bus6char,bus7char,bus8char)
		seen=True
	
	#if len(outlist)>2:	
	#	seen=True
	#	#print(outlist)
	#	print("New Start: ",outlist[0])
	#	print("New Increment: ",outlist[1]-outlist[0])
	i+=48393865507

#100000000000000
#690123192779524

print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
sys.exit("Stop!")


	




