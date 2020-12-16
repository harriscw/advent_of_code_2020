import time
import sys

bus_string=['17','x','13','19']

offsets=[0]
xcnt=1
for i in range(1,len(bus_string)):
	print(i)
	if bus_string[i]=='x':
		xcnt+=1
	else:
		offsets.append(offsets[-1]+xcnt)
		xcnt=1
		
print(offsets)

cyclelist=[]
for i in range(0,len(bus_string)):
	if bus_string[i] != 'x':
		cyclelist.append(['D'] + ['x']*(int(bus_string[i])-1))
print(cyclelist)

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()

i=0
outlist=[]
seen=False
while seen == False:
	
	bus0char=cyclelist[0][(i+offsets[0]) % len(cyclelist[0])]
	bus1char=cyclelist[1][(i+offsets[1]) % len(cyclelist[1])]
	bus2char=cyclelist[2][(i+offsets[2]) % len(cyclelist[2])]
	
		
	#print(bus0char,bus1char,bus2char)
	#print(i)

	if i!=-1 and bus0char=="D" and bus1char=="D" and bus2char=="D":
		#outlist.append(i)
		print("got it: ", i)
		print(bus0char,bus1char,bus2char)
		seen=True
	#print(outlist)
	i+=1
	
	
print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))


sys.exit("Stop!")
