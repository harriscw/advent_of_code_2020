text_file = open("input.txt", "r")
lines = text_file.readlines()
mylist=[]
for i in range(len(lines)):
    mylist.append(int(lines[i].strip("\n")))
print(mylist)