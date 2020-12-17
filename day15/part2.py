import sys
import time

mylist=[0,3,6]
mylist=[0,3,6]
mylist=[1,3,2]
mylist=[2,1,3]
mylist=[1,2,3]
mylist=[2,0,1,9,5,19]

# Instead of using a for loop every iteration just create a growing dictionary
# key is a number when its seen, value is the last step it was seen at

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()

spoken=dict() #initialize dict
for i in range(len(mylist)):
	spoken[mylist[i]]=i+1

i=len(mylist) #initialize counter
currentnum=mylist[-1]
while i <=30000000:
	if i % 1000000==0:#feedback while running
		print(i)
	if i==30000000:#print when you get the answer
		print("Step: ",i,"Current Num: ", currentnum)
	elif i == len(mylist):#this handles the handoff from the initial numbers to the while loop
		currentnum=0
	elif currentnum not in spoken.keys():#if its not in the dictionary add it with the step youre on
		spoken[currentnum]=i
		currentnum=0 #set current number to 0
	elif currentnum in spoken.keys(): #if it is in the dictionary update the value with the current step and find diff as needed
		thediff=i-spoken[currentnum]
		spoken[currentnum]=i
		currentnum=thediff
	i+=1

print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
sys.exit("Stop!")

				
	

