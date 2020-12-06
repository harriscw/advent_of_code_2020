import csv

#Read data 
file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	if line==[]:
		line=["XXXX"]#Differentiate groups
	for i in range(len(line)):
		mylist.append(line[i])

print(mylist)

#get everything in one line
#To get person counts separate people by an identifiable string
mystring="ZZZZ"
for line in mylist:
	mystring+=(line+"ZZZZ")

print(mystring)

#get each group as own element of list
grouplist=mystring.split("XXXX")
print(grouplist)

#Get a person count in each group
#Count the number of times where the occurence of a given letter equals the person count
outlist=[]
for line in grouplist:
	personcnt = line.count("ZZZZ")-1 #get person count per group
	newstring = line.replace("ZZZZ","") #remove the string that separates people
	countall=[]
	for letter in set(line.replace("ZZZZ","")): #iterate over unique letters per group
		countall.append(newstring.count(letter)==personcnt)#get a letter count per group
	outlist.append(sum(countall)) #find the total number of times when a letter count = person count in a given group	
	
print(outlist)
print(sum(outlist))