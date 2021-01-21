ret = readlines("input.txt") #reads as an array

valid=0
for item in ret
	newitem=split(replace(item, ":" => "")) #replace : with missing then split on spaces
	
	theletter=newitem[2][1]
	checkstring=newitem[3]
	myrange=split(newitem[1],"-")
	mymin=parse(Int64, myrange[1])
	mymax=parse(Int64, myrange[2])
	
	#thecount=length(collect(eachmatch(Regex(theletter), checkstring))) #get the letter count
	#println("Min: $mymin Max: $mymax Count: $thecount")
	
	pos1=checkstring[mymin]
	pos2=checkstring[mymax]
	
	if (pos1==theletter && pos2!=theletter)|(pos1!=theletter && pos2==theletter)
		global valid+=1
	end
end

print("Final solution: $valid")