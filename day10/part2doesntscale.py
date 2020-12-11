import csv
import sys
import networkx as nx
import time

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

#get list of tuples with all the edges
edgelist=[]
for i in range(len(mylist)):
	#get all values in list that are <=3 above
	withinthree = [num for num in mylist if 0<num-mylist[i]<=3]
	#print("node: " + str(mylist[i]))
	#print(withinthree)
	for j in range(len(withinthree)):
		edgelist.append((mylist[i],withinthree[j]))

print(edgelist)

#create directional graph
G = nx.DiGraph()
G.add_nodes_from(mylist)#add nodes
G.add_edges_from(edgelist)

#pathnum=list(nx.all_simple_paths(G, source=0, target=max(mylist)))
#print(list(pathnum))
pathnum=0
start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()
for path in nx.all_simple_paths(G, source=0, target=max(mylist)):	
	pathnum+=1
	if(pathnum % 1000000 ==0):
		print(path)
		print(pathnum)
	#print(path)
	
print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
print("Total paths: " + str(pathnum))	
		