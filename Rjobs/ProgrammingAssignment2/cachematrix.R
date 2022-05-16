## This functions cache's the inverse of a matrix by using lexical scooping
## This matrix create a specific matrix and calculates the inverse of the matrix

## Write a short comment describing this function

makeCacheMatrix <- function(x = matrix()) {
  invert <- NUL
  set <- function(y){
    x <<- v
    inv <<- NULL
  }
  get <- function() x
  inverseSet <- function(matrixSolver) invert <<- matrixSolver
  inverseGet <- function() invert
  list(set = set, get = get, inverseSet = inverseSet, inverseGet = inverseGet)
}


## This function calculates and returns the inverse of the matrix 'x'
cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
  invert <- x$inverseGEt()
  if(!is.null(invert)){
    message("getting cached data")
    return(invert)
  }
  df <- x$get()
  invert <- solve(df)
  x$inverseSet(invert)
  invert
}
