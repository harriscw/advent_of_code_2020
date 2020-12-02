import csv
import pandas as pd

# Read data

mylist = [
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc']

file=open("input.csv", "rt")
reader = csv.reader(file)
mylist = []
for line in reader:
	for i in range(len(line)):
		mylist.append(line[i])

#wrangle into pandas df
df_raw = pd.DataFrame(mylist,columns=['raw']) #get raw string
df_pw = df_raw['raw'].str.split(pat=": ",expand=True) #get pw string
df_letter = df_pw[0].str.split(pat=" ",expand=True)#get letter
df_minmax = df_letter[0].str.split(pat="-",expand=True)#get min/max
#concatenate together
df = pd.concat([df_minmax[0],df_minmax[1],df_letter[1],df_pw[1],df_raw],axis=1)
df.columns = ['min', 'max','letter','pw','raw']

#get counts
keepers=[]
for i in iter(range(len(df.index))):
	thecount=df['pw'][i].count(df['letter'][i])
	keepers.append(int(df['min'][i])<=thecount<=int(df['max'][i]))

print(keepers)
print(len(df[keepers].index))
