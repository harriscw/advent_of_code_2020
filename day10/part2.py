import csv
import sys
import networkx as nx
import time
from functools import reduce

####
# The big idea is that you can separate this into smaller networks and then multiply those paths together
# e.g. if there's 5 ways to get from A to B, 1 way to get from B to C, and 3 ways to get from C to D then there are 5*1*3
####

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]

for i in range(len(lines)):
    mylist.append(int(lines[i].strip("\n")))
	
mylist.append(0)
mylist.append(max(mylist)+3)
mylist.sort()
print(mylist)

## this finds differences between nodes, ie part 1 puzzle
newlist=[]
for i in range(len(mylist)-1):
	newlist.append(mylist[i+1]-mylist[i])

print(newlist)
agglist=[]
cnt=0
for i in range(len(newlist)):
	if newlist[i]==3 or i==len(newlist):
		agglist.append(mylist[cnt+1:i+1])
		cnt=i

# get 0 and max back in there
agglist[0].insert(0,0)
agglist[-1].append(max(mylist))

#get list of tuples with all the edges
totaledges=[]
for k in range(len(agglist)):
	mylist=agglist[k]
	edgelist=[]
	for i in range(len(mylist)):
		#get all values in list that are <=3 above
		withinthree = [num for num in mylist if 0<num-mylist[i]<=3]
		#print("node: " + str(mylist[i]))
		#print(withinthree)
		for j in range(len(withinthree)):
			edgelist.append((mylist[i],withinthree[j]))
	totaledges.append(edgelist)
print(totaledges)

#Create network graph for each subset
totalpaths=[]
for i in range(len(totaledges)):
	G = nx.DiGraph()
	G.add_nodes_from(agglist[i])#add nodes
	G.add_edges_from(totaledges[i])
	pathnum=0
	start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	startsec = time.time()
	if len(totaledges[i])==0:
		pathnum=1
	else:
		for path in nx.all_simple_paths(G, source=min(agglist[i]), target=max(agglist[i])):	
			pathnum+=1
			if(pathnum % 1000000 ==0):
				print(path)
				print(pathnum)
	totalpaths.append(pathnum)
#print(totalpaths)
finalanswer=reduce(lambda x, y: x*y, totalpaths) #multiply all independent parts together
print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
print("Total paths: ",finalanswer)	

sys.exit("stop!")