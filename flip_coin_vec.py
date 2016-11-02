#!/usr/bin/env python3

import numpy as np

"""
Vectorized implementation for simulating a coin flip n times
"""

def flip(n, b = 0.5):
    """
    Parameters:
    -----------
        n: int
            number of flips to use, dimension of the np array return
        b: float
            bias, increasing this value will make it more likely to land on heads

    Returns:
    --------
        h: np.array[booleans]
            array of boolean values for whether the flip resulted in heads
    """
    flips = np.random.random_sample((n,))                   #Generates list of floats to determine result of flip
    h = np.where(flips < b, 0, 1)                           #Tests the floats in flips against bias, 0 => heads, 1 => tails
    return(h)

def test_flip():
    assert true

def main(n, b):
    print(flip(n, b))

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    if len(sys.argv) == 3:
        b = float(sys.argv[2])
    else:
        b = 0.5
    main(n, b)
