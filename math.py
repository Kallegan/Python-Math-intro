import numpy as np
import pyrr
import math

v = np.array([1, 2], dtype = np.float32)

u = np.array([
    [1],
    [-1]
], dtype = np.float32)

norm = pyrr.vector.length(v)
norm2 = math.sqrt(v[0]**2 + v[1]**2)
print(norm)
print(norm2)
print(math.sqrt(5))

v_hat = v / norm
print(v_hat)
v_hat_norm = pyrr.vector.length(v_hat)
print(v_hat_norm)