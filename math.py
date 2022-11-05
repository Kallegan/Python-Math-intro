import numpy as np

v = np.array([
    [1],
    [2]
], dtype = np.float32)

u = np.array([
    [1],
    [-1]
], dtype = np.float32)


w = v - u



print(w)