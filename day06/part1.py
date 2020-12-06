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
mystring=""
for line in mylist:
	mystring+=line

print(mystring)

#get each group as own element of list
grouplist=mystring.split("XXXX")
print(grouplist)

#Count unique characters in each list element
outlist=[]
for line in grouplist:
	outlist.append(len(set(line)))
	
print(outlist)
print(sum(outlist))