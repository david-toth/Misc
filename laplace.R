# Laplace distribution
# PDF, CDF, random variate generator, MLE parameters
# Courtesy of Wikipedia :) 

dlaplace <- function(x, center = 0, scale = 1){
  0.5/scale * exp(-abs(x - center)/scale)
}

plaplace <- function(x, center = 0, scale = 1){
  0.5 + 0.5*sign(x-center)*(1-exp(-abs(x-center)/scale))
}

rlaplace <- function(n, center = 0, scale = 1){
  u <- runif(n, -0.5, 0.5)
  center - scale*sign(u)*log(1-2*abs(u))
}

fit.laplace <- function(x){
  center <- median(x)
  scale <- mean(abs(x - center))
  list("center" = center, "scale" = scale)
}
