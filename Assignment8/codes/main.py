import numpy as np

x2 = x = np.array([0.98, 0.02])

for i in range(99):
    x = np.convolve(x, x2)

print(x[3])     # answer calculated
print(4*np.e**-2/3)   # answer given in book
