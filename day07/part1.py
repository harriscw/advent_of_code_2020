import csv
import re
import networkx as nx

#Read data 
file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(line[i])

combinedRegex = re.compile("[a-z]+ [a-z]+")#regular expression for two words

#create dictionary

mydict={}
for line in mylist:
	split1=line.split(" bags contain")#get key
	mykey=split1[0]
	myvalue=combinedRegex.findall(split1[1])#get two word values
	tuplelist=[]
	for myval in myvalue:#get values as tuples for networkx
		mytuple=(mykey,myval)
		tuplelist.append(mytuple)
	mydict[mykey]=tuplelist

#create directional graph
G = nx.DiGraph()
G.add_nodes_from(list(mydict.keys()))#add nodes
for myedges in mydict.values():#add edges
	if myedges[0][1] != 'no other':
		G.add_edges_from(myedges)

#find all paths to shiny gold
finalpaths=[]
for mynode in list(mydict.keys()):#iterate over nodes
	for path in nx.all_simple_paths(G, source=mynode, target='shiny gold'):
		if path[0] not in finalpaths:#if outer bag not already in list then add it
			finalpaths.append(path[0])
			
print(finalpaths)
print(len(finalpaths))