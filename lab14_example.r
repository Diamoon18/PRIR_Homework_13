rm(list = ls())

#Generate data
data <- 1:1e9
data_list <- list("1" = data,
                  "2" = data,
                  "3" = data,
                  "4" = data)
# Single core
time_benchmark <- system.time(
  lapply(data_list, mean)
)
time_benchmark

library(parallel)
# Detect the number of available cores and create cluster-1
cl <- makeCluster(detectCores()-1)

# Run parallel computation
time_parallel <- system.time(
  parLapply(cl, data_list, mean)
)
time_parallel
# Close cluster
stopCluster(cl)

