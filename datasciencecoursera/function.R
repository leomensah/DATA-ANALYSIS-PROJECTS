x <- matrix(1:6, 2, 3)

for(i in seq_len(nrow(x))){
  for(j in seq_len(ncol(x))){
    print(x[i, j])
  }
}

above10 <- function(x, n){
  use <- x > n
  x[use]
}

columnmean <- function(y, removeNA = TRUE){
  nc <- ncol(y)
  means <- numeric(nc)
  for (i in nc) {
    means[i] <- mean(y[, i])
    
  }
    means
}