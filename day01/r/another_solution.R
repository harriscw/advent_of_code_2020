#can we do this without loops

#read data
input = as.numeric(unlist(read.delim("input.txt", header = FALSE)))

# input=c(
#   1721,
#   979,
#   366,
#   299,
#   675,
#   1456
# )

#lets use matrix addition
m1 = matrix(rep(input,length(input)),nrow=length(input)) #matrix where each col is your input
m2 = t(m1) #matrix where each row is your input
mat = m1+m2

#find the elements that = 2020
res = which(mat==2020, arr.ind=TRUE)

#multiply them together
input[res[1,1]]*input[res[1,2]]



# part 2

#now you would need to do this as addition of 2 tensors (3d matrices)
#you could add each item of the input to each element of the matrix
#you got in part 1 where each cell represents the addition of two
# elements from the input.

# so you would need to create tensor A which is mat from part 1 repeated
# as many times as the input.  And tensor B which is the input vector repeated
# multiple times into the same dimensions as tensor A.

# so for the sample input of length 6, 'mat' from part 1 is 6x6.  
# so tensor A is 6x6.  
# and to tensor B is the length 6 input vector reshaped into a 6x6x6 tensor.

#add tensor A to tensor B.  Find where the sum is 2020.  backtrack to individual
# components.

m1b=array(rep(mat,length(input)),rep(length(input),3)) #make an nxnxn cube by stacking your solution to p1
dim(m1b)

# You want to add each element of input to your previous answer
# so create a 3D matrix where each slice is one number from input
vec=sort(rep(input,length(input)^2))
m2b=array(vec,rep(length(input),3))
m2b
dim(m2b)

mat2=m1b+m2b #add them
res=which(mat2==2020, arr.ind=TRUE) # get indices
res
# mat2[5,2,2]
# m1b[,,2] #original part 1 solution

input[77]+input[62]+unique(vec)[1]
input[77]*input[62]*unique(vec)[1]
