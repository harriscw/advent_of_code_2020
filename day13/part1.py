import sys
import pandas as pd

#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
	mylist.append(lines[i].strip("\n"))

thetime=int(mylist[0]) #time after which you want to know the next bus
bus_string=mylist[1].split(",")
bus_string[:] = [int(x) for x in bus_string if x != "x"] #ignore the x's

print(bus_string)

#get patterns for each bus as a dictionary
mydict={}
for i in bus_string:
	print(i)
	mydict[i]=['D']
	counter=0
	for j in range(thetime+100):#go to the time of interest +100 arbitrarily
		counter+=1
		if counter==i:
			mydict[i].append("D")
			counter=0
		else:
			mydict[i].append(".")


pd.set_option("display.max_rows", None, "display.max_columns", None) #so you can print out the entire data frame
print(pd.DataFrame.from_dict(mydict)[thetime:])#just look and do the math manually because its faster

sys.exit("Stop!")

				
	

