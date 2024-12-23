# Python3 Program to find root of
# a function, f(x)
import math;
 
MAX_ITERATIONS = 10000;
 
# Function to calculate f(x)
def f(x):
    # Taking f(x) = x^4 - 16*x^3 + 500x^2 - 8000*x + 32000
    return (pow(x, 4) - 16*pow(x, 3) + 500*x**2 -8000*x + 32000);
 
def Muller(p0, p1, p2):
    res = 0;
    i = 0;
    while (True):
     
        # Calculating various constants
        # required to calculate x3
        f0 = f(p0); f1 = f(p1); f2 = f(p2);
        d1 = f0 - f2;
        d2 = f1 - f2;
        h1 = p0 - p2;
        h2 = p1 - p2;
        a0 = f2;
        a1 = (((pow(h1, 2) * d2) - (pow(h2, 2) * d1)) / (h1 * h2 * (h1 - h2)));
        a2 = (((h2 * d1) - (h1 * d2)) / (h1 * h2 * (h1 - h2)));

        x = ((-2 * a0) / (a1 + abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
        y = ((-2 * a0) / (a1 - abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
 
        # Taking the root which is
        # closer to x2
        if (x >= y):
            res = x + p2;
        else:
            res = y + p2;
 
        # checking for resemblance of x3
        # with x2 till two decimal places
        m = res * 100;
        n = p2 * 100;
        # floor() method in Python returns the floor of x i.e., the largest integer not greater than x.
        m = math.floor(m);
        n = math.floor(n);
        if (m == n):
            break;
        p0 = p1;
        p1 = p2;
        p2 = res;
        if (i > MAX_ITERATIONS):
            print("Root cannot be found using",
                            "Muller's method");
            break;
        i += 1;
    if (i <= MAX_ITERATIONS):
        print(math.sqrt(400 - pow(round(res, 4), 2)));

 
# Driver Code
p0 = 0;
p1 = 1;
p2 = 2;
Muller(p0, p1, p2);
