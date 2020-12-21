import sys
import re

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

#define some regular expressions
innerparens = re.compile("\([^()]+\)") #find the inner most parentheses (have open and close with no other parens in between)
anyplus = re.compile("([0-9]+ \+ [0-9]+)") #find additions
starttimes = re.compile("^([0-9]+ \* [0-9]+)") #find multiplications

#write a function to resolve a string with no parentheses from left to right
def resolvestring(string):
	thestring=string
	keepgoing=True
	cnt=1
	while keepgoing==True:	#keep going until the string is completely resolved
		#print("Step",cnt)
		#print("Original String",thestring)
		plusmatch=anyplus.findall(thestring)
		#print("Match List:",plusmatch)
		if len(plusmatch)>0:
			firstmatch=plusmatch[0] #need to do this one at a time for only the first match
			thematch=anyplus.findall(thestring)[0] #grep
			resolved=str(eval(thematch)) #resolve
			#print(thestring)
			thestring=thestring.replace(firstmatch,resolved)
			#print(thestring)
		else:
			keepgoing=False
		cnt+=1
	
	thestring=str(eval(thestring))#once all the + are gone just evaluate the string
	return(thestring)	


outlist=[]
for eachstring in mylist: #iterate through each equation in the problem set
	#print(eachstring)
	thisstring=eachstring
	
	#First resolve inner parentheses
	mykeepgoing=True
	mycnt=1
	while mykeepgoing==True: #iteratively resolve nested parentheses
		#print("Step",mycnt)
		parenmatch = innerparens.findall(thisstring) #match inner parentheses
		#print("matches",parenmatch)
		if len(parenmatch)>0:#if there's a match
			myresolved=[]
			for i in parenmatch: #iterate over each match
				myresolved=resolvestring(i.replace("(","").replace(")","")) #resolve the match
				#print("initial string",thisstring)
				#print("match",i)
				#print("resolved val",myresolved)
				thisstring=thisstring.replace(i,myresolved) #put the resolved number back in the original string
				#print("updated string",thisstring)
		else:
			mykeepgoing=False
		mycnt+=1
				
	#When no inner parentheses exist anymore just resolve the string
	outlist.append(int(resolvestring(thisstring)))

print("Solution:",sum(outlist))