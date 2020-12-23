import sys
from itertools import product
import numpy as np

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
rulesraw=dict()
messages=[]
seen=False
for i in range(len(lines)):
	thisline=lines[i].strip("\n")
	if thisline=='':
		seen=True
	if seen==False:
		rulesraw[thisline.split(": ")[0]]=thisline.split(": ")[1].strip('"')
	if seen==True and thisline != '':
		messages.append(thisline)

#print(rulesraw)

#initialize a known keys list 
knowndict = dict()
for key in sorted(list(rulesraw.keys())):
	#print(key,rulesraw[key])
	if rulesraw[key]=='a' or rulesraw[key]=='b':
		knowndict[key]=rulesraw[key]

#print("Known",knowndict)

###Define a function to iterate over a list and mae the relevant strings

def stringmaker(thelist):
	#print(thelist)
	newlist=[]
	outerlist=[]
	for myitem in thelist:#each element of the list
		newlist = myitem.strip().split()
		#print("Newlist",newlist)
		sublist=[]
		for myval in newlist:
			sublist.append(knowndict[myval])
		#print("Sublist",sublist)
		#print("dot",list(product(*sublist)))
		#mydot=[i[0]+i[1] for i in list(product(*sublist))]
		mydot=[''.join(sub_list) for sub_list in list(product(*sublist))]
		#mydot = [ x for y in list(product(*sublist)) for x in y]
		#print(mydot)
		outerlist += mydot
	#print("outer",outerlist,"length",len(outerlist))

	return(outerlist)
	
	

#print(stringmaker(['4 4 ', ' 5 5']))
#print(stringmaker(['4 5 ', ' 5 4']))

#knowndict={'4': 'a', '5': 'b', '2': ['aa', 'bb'], '3': ['ab', 'ba']}
#print(stringmaker(['2 3 ', ' 3 2']))
#
#knowndict={'4': 'a', '5': 'b', '2': ['aa', 'bb'], '3': ['ab', 'ba'], '1': ['aaab', 'aaba', 'bbab', 'bbba', 'abaa', 'abbb', 'baaa', 'babb']}
#print(stringmaker(['4 1 5']))
#sys.exit("stop!")





#print(knowndict)

cnt=1
alldone=False
while alldone==False:
#while cnt<10:
	print("Step:",cnt,"Known Keys:",len(knowndict.keys()),"Total Keys:",len(rulesraw.keys()))
	unknownkeys=list(filter(lambda a: a not in knowndict.keys(), sorted(list(rulesraw.keys()))))
	#print(unknownkeys)
	#find only keys that depend on known keys
	for key in unknownkeys: #iterate over unknown keys
		#allkeys=list(filter(lambda a: a != ' ' and a != '|' and a != "\"", set(rulesraw[key]))) #get all rule dependencies for this rule
		allkeys=list(set(rulesraw[key].replace("| ","").split(" ")))
		#print("attempt",list(set(rulesraw[key].replace("| ","").split(" "))))
		#print("key",key,"dependencies",allkeys,"Raw",rulesraw[key])
		if all(x in knowndict.keys() for x in allkeys): #if this rule consists of only known rules
			ruleaslist=rulesraw[key].split('|')
			#print("Key",key)
			#print("Rule",ruleaslist)
			#print("Resolved",stringmaker(ruleaslist))
			knowndict[key]=stringmaker(ruleaslist)
	cnt+=1
	print(len(knowndict.keys()))
	if len(knowndict.keys())==len(rulesraw.keys()):
		alldone=True

print("it ended")
print("Final Dictionary",len(knowndict['0']))

goodones=[x for x in messages if x in knowndict['0']]
print(len(goodones))

sys.exit("stop!")