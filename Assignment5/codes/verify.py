import numpy as np
import pandas as pd


df = pd.read_excel("../tables/Fish.xlsx")
s = df["Number"]

# Tyep: Male = 0 ,  Female = 1
fish = np.array([0]*s[0] + [1]*s[1])

# perform the experiment multiple times (say 10000 times) to get probability
t = 10000
choice = np.random.choice(fish, size=t)
unique, count = np.unique(choice, return_counts=True)
zero_one = dict(zip(unique, count))

print("Pr(X = 0) = ", zero_one[0]/t)
