import csv
import math


#Read data 
mylist = [
"..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]

file=open("input2.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(line[i])

### expand trees as needed
mywidth=len(mylist[0])
mylength=len(mylist)
catnum=math.ceil((mywidth/7)*(mylength))

print("Number of consecutive strings needed: " + str(catnum))

newlist = []
for i in iter(range(len(mylist))):
	newlist.append(catnum*mylist[i])
	
def treefinder(overnum,myby):
	trees=[]
	xcoord=0
	for i in range(0, len(newlist), myby):
		trees.append(newlist[i][xcoord]=="#")
		xcoord += overnum
	print("Number of trees in R" + str(myby) + "D" + str(overnum) + ": " + str(sum(trees)))
	return(sum(trees))
		
print(treefinder(overnum=1,myby=1)*treefinder(overnum=3,myby=1)*treefinder(overnum=5,myby=1)*treefinder(overnum=7,myby=1)*treefinder(overnum=1,myby=2))
		
		