ret = map(str -> parse(Int, str), readlines("input.txt"))

#print(ret)

for i in ret, j in ret, k in ret
	#@show (i+j)
	if i+j+k == 2020.
		println("Final answer: $(i*j*k)")
		break
	end
end