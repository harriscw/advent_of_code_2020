library(dplyr)

input = read.delim("input.txt", header = FALSE) %>% pull()

for (i in input) {
  for (j in input) {
    for (k in input) {
      if (i + j + k == 2020) {
        print(i)
        print(j)
        print(k)
        print(paste("Final Answer:", i * j * k))
        break
      }
    }
  }
}