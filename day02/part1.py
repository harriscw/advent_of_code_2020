import csv
from pandas import DataFrame


file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(line[i])
		
df_raw = DataFrame (mylist,columns=['raw'])
print(df_raw)

df_pw = df_raw['raw'].str.split(pat=": ",expand=True)
print(df_pw)
df_criteria = df_pw[0].str.split(pat=" ",expand=True)
print(df_criteria)