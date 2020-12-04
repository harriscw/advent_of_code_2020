import csv
import re

#Read data 
file=open("input2.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	if line==[]:
		line=["xxxx"]
	for i in range(len(line)):
		mylist.append(line[i])

#make each passport a single string in a list
wrangled=''.join(mylist).split("xxxx")

#define regular expressions to match
regexes= ['byr', 'iyr', 'eyr','hgt','hcl','ecl','pid','cid']
combinedRegex = re.compile('|'.join('(?:{0})'.format(x) for x in regexes))

# find matches
finallist=[]
for line in wrangled:
	thematches=combinedRegex.findall(line)
	if (len(thematches)==8)|(len(thematches)==7 and "cid" not in thematches):#either all there or all but cid
		finallist.append(True)

print("Total Valid Passports: " + str(sum(finallist)))
