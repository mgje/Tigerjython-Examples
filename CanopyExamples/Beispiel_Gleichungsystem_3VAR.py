import numpy as np
# Defining the matrices
A = np.matrix([[3, 6, -5],
[1, -3, 2],
[5, -1, 4]])
B = np.matrix([[12],
[-2],
[10]])
# Solving for the variables, where we invert A
X = A ** (-1) * B
print(X)
# matrix([[ 1.75],
# [ 1.75],
# [ 0.75]])