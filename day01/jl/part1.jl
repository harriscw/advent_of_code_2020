ret = map(str -> parse(Int, str), readlines("input.txt"))

#print(ret)

for i in ret, j in ret
	#@show (i+j)
	if i+j == 2020.
		println("Final answer: $(i*j)")
		break
	end
end