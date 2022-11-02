import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List
from math import *

def iteration(given_function, x0, min_error=0.001, max_iteration=4) -> Tuple[float, List]:
    i = 0
    error = 1
    xp = []
    x = None
    while error > min_error and i < max_iteration:
        x = given_function(x0)
        error = abs(x0 - x)
        x0 = x
        xp.append(x0)
        i += 1
    print(xp)
    return x, xp
    
def main():
    fx = input("Write function: ")
    given_function = lambda x: eval(fx)

    x_start = 1
    xf, xp = iteration(given_function, x_start)

    """plot(xf, xp, x_start, given_function)"""

if __name__ == '__main__': main()
