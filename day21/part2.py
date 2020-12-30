import sys

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
mealdict=dict()
cnt=0
for i in range(len(lines)):
	theline=lines[i].strip("\n").replace("(","").replace(")","").split(" contains ")
	ingredients=theline[0].split(" ")
	allergens=theline[1].split(", ")
	mealdict[cnt]={"ingredients":ingredients,"allergens":allergens}
	cnt+=1
#print(mealdict)
print(len(mealdict.keys()))

# get a list of unique allergens
allergenlist=[]
inglist=[]
for i in range(len(mealdict.keys())):
	allergenlist += mealdict[i]['allergens']
	inglist.append(len(mealdict[i]['ingredients']))
	
print(list(set(allergenlist)))
print(min(inglist))
#iterate through and see if there's one ingredient that is in all dishes labelled with a certain allergen

allergendict=dict()
for theallergen in list(set(allergenlist)):
	allergenlist=[]
	for i in range(len(mealdict.keys())):
		if theallergen in mealdict[i]['allergens']:
			allergenlist.append(mealdict[i]['ingredients'])
	allergendict[theallergen]=list(set.intersection(*map(set,allergenlist)))
	print(theallergen,"suspects:",set.intersection(*map(set,allergenlist)))
#print(allergendict)

#unknownallergens=list(allergendict.keys())
#print(unknownallergens)
#knowndict=dict()
#while len(unknownallergens)>0:
#	for key in unknownallergens:
#		if len(allergendict[key])==1:
#			knowndict[key]=allergendict[key][0]
#			for i in unknownallergens:
#			#unknownallergens.replace(key,"")
#print(knowndict)
	
#shellfish: clg
#peanuts: lxjtns
#sesame: vzzz
#nuts: knprxg
#fish: ncjv
#eggs: prxmdlz
#soy: cxfz
#wheat: qdfpq

#knownallergens =['mxmxvkd','sqjhc','fvjkl']
knownallergens =['clg','lxjtns','vzzz','knprxg','ncjv','prxmdlz','cxfz','qdfpq']

cnt=0
for i in mealdict.keys():
	for j in mealdict[i]["ingredients"]:
		if j not in knownallergens:
			cnt+=1
			
print(cnt)
