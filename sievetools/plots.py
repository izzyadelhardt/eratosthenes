import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sievetools import sieve

def plot_sieve(N, log_scale=True):
    all_nmax = np.arange(100, 5000, 100)
    all_prop = sieve.proportion_primes(N)
    plt.plot(all_nmax, all_prop)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    if log_scale:
        plt.xscale("log")
        plt.yscale("log")

