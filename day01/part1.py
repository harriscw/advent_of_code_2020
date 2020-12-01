import numpy as np
import csv

mylist=[
1721,
979,
366,
299,
675,
1456
]

file=open("part1.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(int(line[i]))

for i in iter(range(len(mylist))):
	mylist2 = np.add(mylist,mylist[i])
	gotit=any(x ==2020 for x in mylist2)
	if(gotit==True):
		theindex = np.where(mylist2 == 2020)[0][0]
		print(str(mylist[i]) + str("+") + str(mylist[theindex]) + str("=") + str(mylist[i]+mylist[theindex]))
		print(str(mylist[i]) + str("*") + str(mylist[theindex]) + str("=") + str(mylist[i]*mylist[theindex]))
		
		break