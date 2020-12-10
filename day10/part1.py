import csv
import sys

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

newlist=[]
for i in range(len(mylist)-1):
	newlist.append(mylist[i+1]-mylist[i])

print(newlist)
print("1s: " + str(newlist.count(1)))
print("2s: " + str(newlist.count(2)))
print("3s: " + str(newlist.count(3)))
print("Answer: " + str(newlist.count(1)*newlist.count(3)))