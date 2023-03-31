#read data
input = as.numeric(unlist(read.delim("input.txt", header = FALSE)))

#lets use matrix addition
m1 = matrix(rep(input,length(input)),nrow=length(input)) #matrix where each col is your input
m2 = t(m1) #matrix where each row is your input
mat = m1+m2

#find the elements that = 2020
res = which(mat==2020, arr.ind=TRUE)

#multiply them together
input[res[1,1]]*input[res[1,2]]
