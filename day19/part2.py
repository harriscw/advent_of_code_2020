import sys
from itertools import product
import re
import time

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
print("Start time:",start)
startsec = time.time()
#Read data 
text_file = open("input1_updt.txt", "r")
text_file = open("input_updt.txt", "r")
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
maxmsglen=len(max(messages, key=len)) #this is maximum length of all message strings, we dont need to go beyond this

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
	
	
#print(knowndict)

cnt=1
alldone=False
while alldone==False:
#while cnt<10:
	print("Step:",cnt,"Known Keys:",len(knowndict.keys()),"Total Keys:",len(rulesraw.keys()))
	oldlength = len(knowndict.keys())
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
	#print(len(knowndict.keys()))
	#if oldlength == len(knowndict.keys()):#not updating
	#	print("Infinite Loop Found!")
	#	print("Old Length:",oldlength,"New Length:",len(knowndict.keys()),"All known keys:",knowndict.keys())
	#	print("31",knowndict['31'])
	#	print("42",knowndict['42'])
	#	sys.exit("Stop!")

	if len(knowndict.keys())==len(rulesraw.keys())-3:
		alldone=True

print("At this point we have all entries except 0, 8, and 11")
print("max message length:",maxmsglen)
print("number of messages:",len(messages))
print("length of 42",len(knowndict['42'][0]),knowndict['42'][0])
print("length of 31",len(knowndict['31'][0]),knowndict['31'][0])

## My understanding:
## 8: 42 | 42 8 -> boils down to 42+
## 11: 42 31 | 42 11 31 -> boils down to 42+ 31+ because 42 31 gets continuously substituted in the middle for the 8
## 0: 8 11 -> boils down to 42+ 42+ 31+
## So we want 41+31+ where the number of 31 is < the number of 42

####
# Attempt 3: lets make a regular expression
# Admittedly read a *bunch* of reddit posts before getting to this point.
####

string42='|'.join(knowndict['42'])
string31='|'.join(knowndict['31'])

##this works for the practice example
#regall=re.compile("(^("+string42+"){2}("+string31+")$)" + "|(^("+string42+"){3}("+string31+")$)" + "|(^("+string42+"){3}("+string31+"){2}$)" + "|(^("+string42+"){4}("+string31+"){1}$)"   + #"|(^("+string42+"){4}("+string31+"){2}$)"+ "|(^("+string42+"){4}("+string31+"){3}$)"+ "|(^("+string42+"){5}("+string31+"){1}$)"+ "|(^("+string42+"){5}("+string31+"){2}$)"+ "|(^("+string42+"){5}("+string31+"){3}$)"+ #"|(^("+string42+"){5}("+string31+"){4}$)"+ "|(^("+string42+"){6}("+string31+"){1}$)"+ "|(^("+string42+"){6}("+string31+"){2}$)"+ "|(^("+string42+"){6}("+string31+"){3}$)"+ "|(^("+string42+"){7}("+string31+"){1}$)"+ #"|(^("+string42+"){7}("+string31+"){2}$)"+ "|(^("+string42+"){8}("+string31+"){1}$)"   )

regall=re.compile("(^("+string42+"){2}("+string31+")$)" + "|(^("+string42+"){3}("+string31+")$)" + "|(^("+string42+"){3}("+string31+"){2}$)" + "|(^("+string42+"){4}("+string31+"){1}$)"   + "|(^("+string42+"){4}("+string31+"){2}$)"+ "|(^("+string42+"){4}("+string31+"){3}$)"+ "|(^("+string42+"){5}("+string31+"){1}$)"+ "|(^("+string42+"){5}("+string31+"){2}$)"+ "|(^("+string42+"){5}("+string31+"){3}$)"+ "|(^("+string42+"){5}("+string31+"){4}$)"+ "|(^("+string42+"){6}("+string31+"){1}$)"+ "|(^("+string42+"){6}("+string31+"){2}$)"+ "|(^("+string42+"){6}("+string31+"){3}$)"+ "|(^("+string42+"){6}("+string31+"){4}$)"+ "|(^("+string42+"){6}("+string31+"){5}$)"+ "|(^("+string42+"){7}("+string31+"){1}$)"+ "|(^("+string42+"){7}("+string31+"){2}$)"+ "|(^("+string42+"){7}("+string31+"){3}$)"+ "|(^("+string42+"){7}("+string31+"){4}$)"+ "|(^("+string42+"){7}("+string31+"){5}$)"+ "|(^("+string42+"){8}("+string31+"){1}$)"+ "|(^("+string42+"){8}("+string31+"){2}$)"+ "|(^("+string42+"){8}("+string31+"){3}$)"+ "|(^("+string42+"){8}("+string31+"){4}$)"+ "|(^("+string42+"){9}("+string31+"){1}$)"+ "|(^("+string42+"){9}("+string31+"){2}$)"+ "|(^("+string42+"){9}("+string31+"){3}$)"+ "|(^("+string42+"){10}("+string31+"){1}$)"+ "|(^("+string42+"){10}("+string31+"){2}$)"+ "|(^("+string42+"){11}("+string31+"){1}$)"   )

print(regall)

cnt=1
outlist=[]
for i in messages:
	#print("Number",cnt,":",i)
	if len(regall.findall(i))>0:
		thematch=[x.group(0) for x in regall.finditer(i)][0]
		#print("Match:",thematch)
		outlist.append(thematch)
	cnt+=1

print("Matches:",len(outlist))
#print(outlist)


sys.exit("stop!")

####
# Attempt 1: Create a list of all the valid strings like I did in part 1
####

# So below I am trying to find all combos of 42+ 42+ 31+
# e.g. (42 dot 42) dot 31
#      ((42 dot 42) dot 42) dot 31
#      ((42 dot 42) dot 42) dot (31 dot 31)

# Seems like I'm on the right track answer wise using example input but dont get very far before memory error 


two42=[''.join(sub_list) for sub_list in list(product(knowndict['42'],knowndict['42']))]
three42=[''.join(sub_list) for sub_list in list(product(two42,knowndict['42']))]
four42=[''.join(sub_list) for sub_list in list(product(three42,knowndict['42']))]
five42=[''.join(sub_list) for sub_list in list(product(four42,knowndict['42']))]
six42=[''.join(sub_list) for sub_list in list(product(five42,knowndict['42']))]


mylist=[''.join(sub_list) for sub_list in list(product(two42,knowndict['31']))]
outlist=list(set(mylist) & set(messages))
mylist=[''.join(sub_list) for sub_list in list(product(three42,knowndict['31']))]
outlist+=list(set(mylist) & set(messages))
mylist=[''.join(sub_list) for sub_list in list(product(four42,knowndict['31']))]
outlist+=list(set(mylist) & set(messages))



sys.exit("stop!")

####
# Attempt 2: Just count the number of times valid strings match one in the message instead of keeping track of them
####

### So to avoid a memory error here's a version where every string isn't retained, it's just checked and discarded.
### Yes Im a bad person for cut and pasting all these for loops.
### On the example input where entry 42 and 31 are lists of length 16 with each string length 5 this approach would've run but it might've taken a day? or two

### On the actual input where entry 42 and 31 are lists of length 128 with each string length 8 it would've taken a lot longer
### So this isn't a great approach either

print(knowndict['42'])
sys.exit()
print("Loop 1 Starting...")	

outlist=[]

for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['31']:
			thisstring=i+j+k
			if thisstring in messages:
				outlist.append(thisstring)
				
print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 2 Starting...")	
	

for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['31']:
				thisstring=i+j+k+l
				if thisstring in messages:
					outlist.append(thisstring)

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))	
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))		
print("Loop 3 Starting...")	

					
for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['31']:
				for m in knowndict['31']:
					thisstring=i+j+k+l+m
					if thisstring in messages:
						outlist.append(thisstring)	

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 4 Starting...")


for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['31']:
					thisstring=i+j+k+l+m
					if thisstring in messages:
						outlist.append(thisstring)
						
print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 5 Starting...")	


for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['31']:
					for n in knowndict['31']:
						thisstring=i+j+k+l+m+n
						if thisstring in messages:
							outlist.append(thisstring)	

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))		
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))					
print("Loop 6 Starting...")	


for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['31']:
					for n in knowndict['31']:
						for o in knowndict['31']:
							thisstring=i+j+k+l+m+n+o
							if thisstring in messages:
								outlist.append(thisstring)		

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))		
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))						
print("Loop 7 Starting...")	


for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['31']:
						thisstring=i+j+k+l+m+n
						if thisstring in messages:
							outlist.append(thisstring)	

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))	
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 8 Starting...")	


for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['31']:
						for o in knowndict['31']:
							thisstring=i+j+k+l+m+n+o
							if thisstring in messages:
								outlist.append(thisstring)

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 9 Starting...")	

cnt=0
for i in knowndict['42']:
	print(cnt,"of",len(knowndict['42']))
	cnt+=1
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['31']:
						for o in knowndict['31']:
							for p in knowndict['31']:
								thisstring=i+j+k+l+m+n+o+p
								if thisstring in messages:
									outlist.append(thisstring)

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 10 Starting...")	

									
cnt=0
for i in knowndict['42']:
	print(cnt,"of",len(knowndict['42']))
	cnt+=1
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['31']:
						for o in knowndict['31']:
							for p in knowndict['31']:
								for q in knowndict['31']:
									thisstring=i+j+k+l+m+n+o+p+q
									if thisstring in messages:
										outlist.append(thisstring)

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 11 Starting...")	


cnt=0
for i in knowndict['42']:
	print(cnt,"of",len(knowndict['42']))
	cnt+=1
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['42']:
						for o in knowndict['31']:
							thisstring=i+j+k+l+m+n+o
							if thisstring in messages:
								outlist.append(thisstring)									

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 12 Starting...")	
										
cnt=0
for i in knowndict['42']:
	print(cnt,"of",len(knowndict['42']))
	cnt+=1
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['42']:
						for o in knowndict['31']:
							for p in knowndict['31']:
								thisstring=i+j+k+l+m+n+o+p
								if thisstring in messages:
									outlist.append(thisstring)	

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 13 Starting...")	
										
cnt=0
for i in knowndict['42']:
	print(cnt,"of",len(knowndict['42']))
	cnt+=1
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['42']:
						for o in knowndict['31']:
							for p in knowndict['31']:
								for q in knowndict['31']:
									thisstring=i+j+k+l+m+n+o+p+q
									if thisstring in messages:
										outlist.append(thisstring)									

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 14 Starting...")	
						
for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['42']:
						for o in knowndict['42']:
							for p in knowndict['31']:
								thisstring=i+j+k+l+m+n+o+p
								if thisstring in messages:
									outlist.append(thisstring)


print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 15 Starting...")	
					
for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['42']:
						for o in knowndict['42']:
							for p in knowndict['31']:
								for q in knowndict['31']:
									thisstring=i+j+k+l+m+n+o+p+q
									if thisstring in messages:
										outlist.append(thisstring)

print("Cumulative Time Elapsed:",round(time.time()-startsec,5))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))
print("Loop 16 Starting...")	
							
for i in knowndict['42']:
	for j in knowndict['42']:
		for k in knowndict['42']:
			for l in knowndict['42']:
				for m in knowndict['42']:			
					for n in knowndict['42']:
						for o in knowndict['42']:
							for p in knowndict['42']:
								for q in knowndict['31']:
									thisstring=i+j+k+l+m+n+o+p+q
									if thisstring in messages:
										outlist.append(thisstring)										
										
										
print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Total Cumulative Time Elapsed:",round(time.time()-startsec,5))

print("Number of Matching messages:",len(outlist))
print("Matching messages:",outlist)
print("Longest string length",len(max(outlist, key=len)))



print(len(mylist))

#mylist=[''.join(sub_list) for sub_list in list(product(five42,knowndict['31']))]
#outlist+=list(set(mylist) & set(messages))
#list5=[''.join(sub_list) for sub_list in list(product(sox42,knowndict['31']))]


#outlist=list1+list2+list3+list4+list5
#myintersection=list(set(outlist) & set(messages))
print("intersection length:",len(outlist),outlist)





sys.exit("stop!")