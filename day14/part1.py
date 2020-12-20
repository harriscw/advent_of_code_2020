import sys
import re

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
instrux=[]
for i in range(len(lines)):
	instrux.append(lines[i].strip("\n"))

combinedRegex = re.compile("[0-9]+")#regular expression any strong of numbers on the LHS

mem=dict() #store numbers in a dictionary
for i in instrux:
	#print(i)
	if "mask" in i:
		changeinds=dict()
		cnt=0 #counter for index
		for j in list(i.split(" = ")[1]):#iterate over mask and find indicies that should change
			if j != 'X':
				changeinds[cnt]=j #index:value it should change to
			cnt+=1
	else:
		#get memory address applying regular expression
		memloc=int(combinedRegex.findall(i.split(" = ")[0])[0])
		
		#get binary value
		toconvert=int(i.split(" = ")[1])
		converted="{0:b}".format(toconvert)
		liststring=list(('0'*(36-len(converted)))+converted) #append a bunch of zeroes
		
		#make changes specified by mask
		for key in changeinds:
			liststring[key]=changeinds[key]
		outnum=int(''.join(liststring),2)
		
		#write result to dictionary
		mem[memloc]=outnum

print("Final Answer:",sum(mem.values())) #sum all values in the dictionary
sys.exit("Stop!")