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
wrangled=' '.join(mylist).split("xxxx")
wrangled = [item + ' ' for item in wrangled] #make sure there's a space at the end of each list element
#print(wrangled)

#define regular expressions to match required fields
regexes= [
'byr:', 
'iyr:', 
'eyr:',
'hgt:',
'hcl:',
'ecl:',
'pid:']
combinedRegex = re.compile('|'.join('(?:{0})'.format(x) for x in regexes))

# find matches
finallist=[]
for line in wrangled:
	thematches=combinedRegex.findall(line)
	#print(thematches)
	if len(thematches)==7:#all required fields are present
		print(line)
		
		#get byr
		byrreg = re.compile("byr:([0-9]{4}) ")
		byrmatch=byrreg.findall(line)
		if len(byrmatch)>0:
			byrstatus=1920<=int(byrmatch[0])<=2002
		else:
			byrstatus=False
		print("byr: " + str(byrstatus))
		
		#get iyr
		iyrreg = re.compile("iyr:([0-9]{4}) ")
		iyrmatch=iyrreg.findall(line)
		if len(iyrmatch)>0:
			iyrstatus=2010<=int(iyrmatch[0])<=2020
		else:
			iyrstatus=False
		print("iyr: " + str(iyrstatus))
		
		#get eyr
		eyrreg = re.compile("eyr:([0-9]{4}) ")
		eyrmatch=eyrreg.findall(line)
		if len(eyrmatch)>0:
			eyrstatus=2020<=int(eyrmatch[0])<=2030
		else:
			eyrstatus=False
		print("eyr: " + str(eyrstatus))
		
		#get hgt
		hgtreg = re.compile("hgt:([0-9]{2,3}(?:cm|in)) ")
		hgtstatus0=hgtreg.findall(line)
		if len(hgtstatus0)==1:
			hgtstatus1=hgtstatus0[0]
			#print(hgtstatus1)
			if hgtstatus1[-2:]=="cm":
				#print(hgtstatus1[:-2])
				hgtstatus=150<=int(hgtstatus1[:-2])<=193
			elif hgtstatus1[-2:]=="in":
				#print(hgtstatus1[:-2])
				hgtstatus=59<=int(hgtstatus1[:-2])<=76
			else:
				hgtstatus=False
		else:
			hgtstatus=False
		print("hgt: " + str(hgtstatus))
		
		#get hcl
		hclreg = re.compile("hcl:#[0-9a-f]{6} ")
		hclstatus=len(hclreg.findall(line))>0
		print("hcl: " + str(hclstatus))
		
		#get ecl
		eclreg = re.compile("ecl:(amb |blu |brn |gry |grn |hzl |oth )")
		eclstatus=len(eclreg.findall(line))>0
		print("ecl: " + str(eclstatus))
		
		#get pid
		pidreg = re.compile("pid:[0-9]{9} ")
		pidstatus=len(pidreg.findall(line))>0
		print("pid: " + str(pidstatus))
		
		####
		#final result
		####
		if byrstatus==True and iyrstatus==True and eyrstatus==True and hgtstatus==True and hclstatus==True and eclstatus==True and pidstatus==True: 
			finallist.append(True)

print("Total Valid Passports: " + str(sum(finallist)))







