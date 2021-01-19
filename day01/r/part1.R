library(dplyr)

input = read.delim("input.txt", header = FALSE) %>% pull()

for (i in input) {
  for (j in input) {
    if (i + j == 2020) {
      print(i)
      print(j)
      print(paste("Final Answer:", i * j))
      break
    }
  }
}