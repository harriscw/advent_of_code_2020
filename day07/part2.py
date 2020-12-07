import csv
import re
import networkx as nx
import sys

#Read data 
file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(line[i])

#print(mylist)
weightandbag = re.compile("[0-9]+ [a-z]+ [a-z]+")#regular expression for weights and two words
weightonly = re.compile("([0-9]+) [a-z]+ [a-z]+")#regular expression for weights
bagonly = re.compile("[0-9]+ ([a-z]+ [a-z]+)")#regular expression for two words

#create dictionary
mydict={}
for line in mylist:
	split1=line.split(" bags contain")[0]#get key
	mykey=split1[0]
	myvalue=weightandbag.findall(split1[1])#get two word values
	tuplelist=[]
	for myval in myvalue:#get values as 3 tuples for networkx: (node 1, node 2, weight)
		myweight=int(weightonly.findall(myval)[0])
		mybag=bagonly.findall(myval)[0]
		mytuple=(mykey,mybag,myweight)
		tuplelist.append(mytuple)
	mydict[mykey]=tuplelist

#create network graph
G = nx.DiGraph()
G.add_nodes_from(list(mydict.keys()))#add nodes
for myedges in mydict.values():#add edges
	for eachedge in myedges: #add each edge individually
		if myedges[0][1] != []:
			G.add_edge(eachedge[0], eachedge[1], weight=eachedge[2])

#find all paths to shiny gold
finallist=[]
for mynode in list(mydict.keys()):#iterate over nodes
	for path in nx.all_simple_paths(G, source='shiny gold', target=mynode):#all paths starting from shiny gold
		print(path)
		theproduct=1
		for i in iter(range(len(path)-1)):#get the weight products for each path
			theproduct *= G.edges[path[i],path[i+1]]['weight']
		finallist.append(theproduct)
	
print(sum(finallist))#get sum of all the products
sys.exit("Stop!")