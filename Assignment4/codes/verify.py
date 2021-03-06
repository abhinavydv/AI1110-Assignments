import numpy as np
import pandas as pd


df = pd.read_excel("../tables/opinion.xlsx")
s = df["Number of Students"]

# Opinion: Like = 1; Dislike = 0
students = np.array([1]*s[0] + [0]*s[1])

# perform the experiment multiple times (say 10000 times) to get probability
t = 10000
choice = np.random.choice(students, size=t)
unique, count = np.unique(choice, return_counts=True)
zero_one = dict(zip(unique, count))

print("Pr(X = Like) = ", zero_one[1]/t)
print("Pr(X = Dislike) = ", zero_one[0]/t)