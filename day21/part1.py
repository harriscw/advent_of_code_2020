import sys

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
mealdict=dict()
cnt=0
for i in range(len(lines)): #create a dictionary of dictionaries. Key is line number, subentries are ingredients and allergens
	theline=lines[i].strip("\n").replace("(","").replace(")","").split(" contains ")
	ingredients=theline[0].split(" ")#get ingredients
	allergens=theline[1].split(", ")#get allergens
	mealdict[cnt]={"ingredients":ingredients,"allergens":allergens}#create a dictionary of dictionaries.
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
for theallergen in list(set(allergenlist)):#iterate over each unique allergen
	allergenlist=[]
	for i in range(len(mealdict.keys())):#for each meal
		if theallergen in mealdict[i]['allergens']: #if the allergen is in that meal
			allergenlist.append(mealdict[i]['ingredients'])#add it to a list of list
	allergendict[theallergen]=list(set.intersection(*map(set,allergenlist)))#get the intersection of each sublist
	print(theallergen,"suspects:",set.intersection(*map(set,allergenlist)))

#it was faster to eyeball this than do it programmatically.  Maybe I am a bad person.
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
for i in mealdict.keys(): #now iterate over each meal's ingredients
	for j in mealdict[i]["ingredients"]:
		if j not in knownallergens:#if the ingredient is not in the allergen list add 1
			cnt+=1		
print(cnt)