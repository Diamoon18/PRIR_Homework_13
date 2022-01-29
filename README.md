# PRIR_Homework_13
#### Task -> find and describe another parallel programming library.
## Parallel Programming In R - ```parallel``` library
The R program developed many parallel processing solutions.\
Over time, solutions from good and developed packages such as ```snow``` and ```multicore```,\
have found their way into the ```parallel``` library.
### Types of clusters
Parallel processing typically takes place in the following sequence of steps:
1. Build a cluster - initiate the R process on different nodes/processors/cores.
2. Send data/code from the root node to the remaining nodes.
3. Execute code in parallel, with or without communication between nodes (preferably without communication).
4. Collect the results from the working nodes.
5. Collapse the cluster, free up resources.

How tasks are processed and results collected depends on the type of cluster. \
Three types of cluster:
 - PSOCK (Parallel Socket Cluster), a socket-based cluster. It can be built on any operating system, including Windows.
 - FORK, a cluster based on Unix systems (also OSX), in which processes can fork, i.e. create (quickly) their copies. Does not work on Windows.
 - MPI, cluster based on the MPI communication protocol, Message Passing Interface. The advantage is that processes can communicate while running.
 
The ```apply()``` family of R functions to apply that function to all of the members of a set.\
```lapply()```, which applies a function to each of the members of a list.\
Parallel library:\
```parLapply()``` function, that can work with PSOC, FORK and other clusters.\
```mclapply()```, can work only with FORK.
### Example lapply() and parLapply()
We have a list containing four large vectors.\
For each of the four large vectors, we want to calculate the mean.\
Below, the calculation of mean is implemented using a conventional lapply approach.
```r
# Generate data
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
```
Time result:\
![image](https://user-images.githubusercontent.com/72127610/151669676-1c340b49-7fec-4855-a8a6-1fac3d22d16c.png) \
This calculation took 15.87 seconds. \
By default, most functions in R run on a single processing core.\
With the multi-core processors in most systems today, the potential for reduced run time by simply dividing tasks onto multiple cores is very significant.
The library ```parallel``` helps us achieve that.
```r
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
```
Time result:\
![image](https://user-images.githubusercontent.com/72127610/151670082-eb675932-0402-49c1-aee2-148b27325507.png) \
This calculation took 4.88 seconds.\
Summarizing, with this library it was possible to get the code speed up in 3 times or even more.
## Parallel Programming In Python - ```threading``` + ```turtle``` library 
### Result image without anu threads
![image](https://user-images.githubusercontent.com/72127610/151676794-02c41afd-9137-4cab-9a36-4adbfcea32da.png) \
Time result: \
![image](https://user-images.githubusercontent.com/72127610/151676803-1888bdff-01b1-4a75-9098-ab74f04d0657.png) 
### Result image with ```threading``` library
![image](https://user-images.githubusercontent.com/72127610/151676686-c3d999b8-ef8b-4e5c-ae4e-d47d378fbd48.png) \
Time result: \
![image](https://user-images.githubusercontent.com/72127610/151676696-d6a14f46-da8d-461e-8220-8110b6abad64.png)
## Sources:
1. https://towardsdatascience.com/getting-started-with-parallel-programming-in-r-d5f801d43745
2. https://pbiecek.gitbooks.io/przewodnik/content/Programowanie/pazury/rownolegle.html
3. https://programmierkonzepte.ch/engl/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=anhang/parallelverarbeitung.inc.php
