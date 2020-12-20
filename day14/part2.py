import sys
import re
import itertools

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
instrux=[]
for i in range(len(lines)):
	instrux.append(lines[i].strip("\n"))

combinedRegex = re.compile("[0-9]+")#regular expression for any string of numbers on the LHS

mem=dict() #store numbers in a dictionary
for i in instrux:
	if "mask" in i:
		mymask=list(i.split(" = ")[1])
	else:
		#get value to write
		theval=int(i.split(" = ")[1])
	
		#get memory address applying regular expression
		memloc=int(combinedRegex.findall(i.split(" = ")[0])[0])
		converted="{0:b}".format(memloc)
		liststring=list(('0'*(36-len(converted)))+converted)
		
		#apply mask
		for i in range(len(mymask)):
			if mymask[i]=="1":#if mask is 1 change to 1
				liststring[i]="1"
			elif mymask[i]=="X":#if mask is X change to X
				liststring[i]="X"
		
		#get all indicies with Xs
		myindices = [i for i, x in enumerate(liststring) if x == "X"]
		
		#get all possible permutations of 0,1 where length is the number of Xs you have
		#for example 2 Xs: 00,01,11,10
		#3 Xs: 000,001,011,...
		combos=[p for p in itertools.product([0,1], repeat=len(myindices))]
		allpossible=[]

		#now create a list of your string filling in Xs with all the permutations
		for combo in combos:#create a new string per combo
			newstring=liststring
			cnt=0
			for myind in myindices:#iteratively change each location of an X to 0 or 1
				newstring[int(myind)]=str(combo[cnt])
				cnt+=1
			outnum=int(''.join(newstring),2)#convert result from binary to integer
			allpossible.append(outnum)#append to list of all possible strings based on the number of permutations
			
		#Finally write each to memory
		for myloc in allpossible:
			mem[myloc]=theval
		
print("Final Answer:",sum(mem.values())) #sum all values in the dictionary
sys.exit("Stop!")