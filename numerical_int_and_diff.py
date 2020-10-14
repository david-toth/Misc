import numpy as np

def integrate(f, a, b, dx):
    """
    Numerical integration.

    b
    --
    \
    /    f(x) dx
    --
    x=a
    
    Args:
    -----
    f    function to integrate
         (should be able to accept arrays
         as input)

    a    lower limit of integral

    b    upper limit of integral

    dx   step size (for precision)

    Rets:
    -----
    Approximate integral
    """
    x = np.arange(a, b+dx, dx)

    return np.sum(dx*f(x))

def differentiate(f, x, h):
    """
    Numerical differentiation.

    f(x + h) - f(x)
    --------------- , h -> 0
           h

    Args:
    -----
    f   function to differentiate

    x   point at which to differentiate

    h   step size (for precision)

    Rets:
    ----
    Approximation of f'(x)
    """
    return (1/h)*(f(x+h) - f(x))
    
