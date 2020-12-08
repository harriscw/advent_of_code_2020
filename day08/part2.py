import csv
import sys

#Read data 
file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		instrux=line[i].split(" ")
		mylist.append([instrux[0],int(instrux[1])])

#get rows where list has a "jmp" instruction
jmps = []
for i in iter(range(len(mylist))):
	if mylist[i][0]=="jmp":
		jmps.append(i)

#iteratively switch each location in instructions where "jmp" occurs to "nop"
for jmploc in jmps:
	mystep=0
	accumulator=0
	donesteps=[]
	mylist[jmploc][0]='nop'

	while True:
		if mystep==len(mylist):#if the last instruction is being executed stop everything and print accumulator
			print("Step: " + str(mystep) + " Instruction: " + " Accumulator: "+ str(accumulator))
			sys.exit("Stop!")
		try:
			if mystep not in donesteps:#only execute if the step hasnt been executed before
				donesteps.append(mystep)
				if mylist[mystep][0]=='nop':
					stepmodifier=1
				elif mylist[mystep][0]=='acc':	
					accumulator +=mylist[mystep][1]
					stepmodifier=1
				elif mylist[mystep][0]=='jmp':	
					stepmodifier =mylist[mystep][1]
				mystep += stepmodifier
			else:
				break
		except(IndexError):
			break
	mylist[jmploc][0]='jmp'#if this iteration didn't work change the instruction back to 'jmp' and start over