import sys
from itertools import product

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

#initialize a known keys list 
knowndict = dict()
for key in sorted(list(rulesraw.keys())):
	if rulesraw[key]=='a' or rulesraw[key]=='b':
		knowndict[key]=rulesraw[key]

###Define a function to iterate over a list and make the relevant strings
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
		mydot=[''.join(sub_list) for sub_list in list(product(*sublist))]
		#print(mydot)
		outerlist += mydot
	#print("outer",outerlist,"length",len(outerlist))
	return(outerlist)
	
	
## Test cases

#print(stringmaker(['4 4 ', ' 5 5']))
#print(stringmaker(['4 5 ', ' 5 4']))
#knowndict={'4': 'a', '5': 'b', '2': ['aa', 'bb'], '3': ['ab', 'ba']}
#print(stringmaker(['2 3 ', ' 3 2']))
#knowndict={'4': 'a', '5': 'b', '2': ['aa', 'bb'], '3': ['ab', 'ba'], '1': ['aaab', 'aaba', 'bbab', 'bbba', 'abaa', 'abbb', 'baaa', 'babb']}
#print(stringmaker(['4 1 5']))

## Now iteratively go through all the rules and resolves the ones you can

cnt=1
alldone=False
while alldone==False:
	print("Step:",cnt,"Known Keys:",len(knowndict.keys()),"Total Keys:",len(rulesraw.keys()))
	unknownkeys=list(filter(lambda a: a not in knowndict.keys(), sorted(list(rulesraw.keys()))))
	#find only keys that depend on known keys
	for key in unknownkeys: #iterate over unknown keys 
		allkeys=list(set(rulesraw[key].replace("| ","").split(" ")))#get all rule dependencies for this rule
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

print("Number of strings matching rule 0",len(knowndict['0']))
goodones=[x for x in messages if x in knowndict['0']] #Get the matches in messages
print("Final Answer:",len(goodones)) 

sys.exit("stop!")