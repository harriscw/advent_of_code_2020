import sys

mylist=[0,3,6]
mylist=[1,3,2]
mylist=[2,1,3]
mylist=[1,2,3]
mylist=[2,0,1,9,5,19]

i=len(mylist)+1 #initialize counter
spoken=mylist #initialize list
while i <=2020:
	lastnum=spoken[-1] #get last number in list
	if spoken.count(lastnum)==1: #if its new append 0
		spoken.append(0)
	else:
		#find difference between last and second to last occurence
		lastind=len(spoken)
		secondtolastind=len(spoken)
		seen=False
		for k,l in reversed(list(enumerate(spoken))): #iterate backwards through list
			if spoken[k]==lastnum and seen ==False:
				lastind=k
				seen=True
			elif spoken[k]==lastnum and seen ==True:
				secondtolastind=k
				break
		thediff=lastind-secondtolastind #get difference as intructed
		#print("last: ",lastind," second to last: ",secondtolastind," Difference: ",thediff)
		spoken.append(thediff)	
	print("iteration: ",i," Prior Number: ",lastnum," Spoken this turn: ",spoken[-1])
	i+=1



sys.exit("Stop!")

				
	

