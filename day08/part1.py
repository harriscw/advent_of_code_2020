import csv
import sys

#Read data 
file=open("input0.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		instrux=line[i].split(" ")
		mylist.append([instrux[0],int(instrux[1])])

print(mylist)

mystep=0
accumulator=0
donesteps=[]
while True:
	print("Step: " + str(mystep) + " Instruction: " + str(mylist[mystep][0]) + "," + str(mylist[mystep][1]) + " Accumulator: "+ str(accumulator))
	if mystep not in donesteps:
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
		sys.exit("Stop!")