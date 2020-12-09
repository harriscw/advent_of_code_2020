import csv
import sys
import itertools

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
    mylist.append(int(lines[i].strip("\n")))

print(mylist)

#507622668
for i in range(len(mylist)):
	for j in range(len(mylist)):
		if sum(mylist[i:j])==507622668:	
			finallist=mylist[i:j]
			finallist.sort()
			print("Found it!")
			print(finallist)
			print(sum(finallist))
			print(finallist[0]+finallist[-1])
			sys.exit("Stop! ")
	