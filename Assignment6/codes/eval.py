import numpy as np


# It's given that chosen student is a girl,
#  so consider only girls for the experiment
g = np.array([0]*387 + [1]*43)
# 0 represents that girl is not in 12th and 1 represents that girl is in 12th

# Out of 387 0's and 43 1's choose a student many (say 1000000) 
# times to get approximate probabilty

t = 1000000
num = np.count_nonzero(np.random.choice(g, t))

prob = num/t
print(prob)

