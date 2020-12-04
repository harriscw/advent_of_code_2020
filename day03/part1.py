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
catnum=math.ceil((mywidth/3)*(mylength/mywidth))

print("Number of consecutive strings needed: " + str(catnum))

newlist = []
for i in iter(range(len(mylist))):
	newlist.append(catnum*mylist[i])

# go down the slope over 3 down 1
xcoord=0
trees=[]
for i in iter(range(len(newlist))):
	trees.append(newlist[i][xcoord]=="#")
	xcoord += 3
	
print("Number of trees: " + str(sum(trees)))