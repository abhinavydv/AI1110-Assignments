import matplotlib.pyplot as plt
import numpy as np


# Opinion: Like = 1; Dislike = 0
students = np.array([1]*135 + [0]*65)

# perform the experiment multiple times (say 10000 times) to get probability
t = 10000
pr_x_eq_0 = pr_x_eq_1 = 0

for i in range(t):
    c = np.random.choice(students)    # choose a student randomly
    if c == 0:
        pr_x_eq_0 += 1
    elif c == 1:
        pr_x_eq_1 += 1

pr_x_eq_1 /= t
pr_x_eq_0 /= t

print("Pr(X=0) = ", pr_x_eq_0)
print("Pr(X=1) = ", pr_x_eq_1)
