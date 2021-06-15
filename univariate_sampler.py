"""
Program to model a one-dimensional sample
in order to generate new samples from the
empirical distribution.
"""
import numpy as np
from scipy.interpolate import PchipInterpolator

class UnivariateSampler:
    def __init__(self, x):
        self.original_sample = x
        self.sample_size = len(x)
        self.y_vals = np.linspace(0,1,self.sample_size)
        self.inverse_cdf = PchipInterpolator(self.y_vals,
                                            np.sort(self.original_sample))
        self.rng = np.random.default_rng()

    def sample(self, size=5000):
        u = self.rng.random(size)
        return self.inverse_cdf(u)
