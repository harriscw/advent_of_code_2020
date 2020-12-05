import csv

#Read data 

#mylist=[
#"FBFBBFFRLR",
#"BFFFBBFRRR",
#"FFFBBBFRRR",
#"BBFFBBFRLL"
#]

file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(line[i])

outlist=[]
for line in mylist:
	#print(line)
	myrange=range(127)
	for letter in line[0:7]: #iterate over first 7 FB characters
		if letter=="F":
			myrange=myrange[0:int((len(myrange))/2)]
		elif letter=="B":
			myrange=myrange[int((len(myrange)+1)/2):int((len(myrange)))]
		lastnum=myrange.start
		#print(letter + " " + str(myrange) + " last:" + str(lastnum))
		
	myrange2=range(7)
	for letter2 in line[7:10]: #iterate over last 3 RL characters
		if letter2=="L":
			myrange2=myrange2[0:int((len(myrange2))/2)]
		elif letter2=="R":
			myrange2=myrange2[int((len(myrange2)+1)/2):int((len(myrange2)))]
		lastnum2=myrange2.start
		#print(letter2 + " " + str(myrange2) + " last:" + str(lastnum2))
		
	outlist.append(lastnum*8+lastnum2)#do the required final math
	
print(max(outlist))
