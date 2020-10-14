import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

def fit_icdf(data):
    """
    Fits inverse cdf using
    an interpolator.

    data: 1D array
    """
    x = np.sort(data)
    y = np.linspace(0,1,len(x))
    f_inv = PchipInterpolator(y,x)

    return f_inv

def draw_samples(inverse_cdf, n=10000):
    """
    Draws samples given an
    inverse cdf callable object.
    """
    x = np.random.rand(n)
    sample = inverse_cdf(x)

    return sample

def main():
    """
    Example using the standard
    normal distribution.
    """
    a = np.random.randn(5000)
    f_inv = fit_icdf(a)
    samples = draw_samples(f_inv)
    plt.hist(samples, bins=100, histtype='step', density=True, label='Sample')
    plt.hist(a, bins=100, histtype='step', density=True, label='True')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    
    main()
