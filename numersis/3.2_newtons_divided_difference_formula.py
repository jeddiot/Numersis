# Function to find the product term.
def proterm(i, value, x): 
    pro = 1; 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro; 

# Calculating divided difference table.
def dividedDiffTable(x, y, n): 
  
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;

# Applying Newton's divided difference formula.
def applyFormula(value, x, y, n): 
    sum = y[0][0]; 
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]); 
    return sum; 
  
def printDiffTable(y, n): # Displaying divided difference table 
  
    for i in range(n): 
        for j in range(n - i): 
            print(round(y[i][j], 4), "\t", 
                               end = " "); 
        print(""); 
  
# Driver Code
# number of inputs given 
n = 6; 
y = [[0 for i in range(10)] for j in range(10)]; 
x = [ 0, 10, 20, 30, 40, 50]; 
  
y[0][0] = 179323; 
y[1][0] = 203302; 
y[2][0] = 226542; 
y[3][0] = 249633; 
y[4][0] = 281422;
y[5][0] = 308746;
  
y=dividedDiffTable(x, y, n); 
printDiffTable(y, n); 
value = -10; 
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 3))

value = 15; 
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 3))

value = 54; 
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 3))

value = 60; 
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 3))
