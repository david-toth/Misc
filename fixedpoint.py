import numpy as np
import matplotlib.pyplot as plt
from time import time

def fixed_point(f, x0, tol, maxiter=1000):
    x = f(x0)
    
    for i in range(maxiter):
        xn = f(x)
        
        if(abs(xn - x) < tol):
            return xn
        
        else:
            x = xn
            
    return xn

def main():
    t0 = time()
    f = lambda x: np.cos(x)
    x0 = 0
    tol = 1e-6
    xn= fixed_point(f, x0, tol)
    print("Fixed point: {}".format(xn))

if __name__ == "__main__":
    main()
    
    
        
