import numpy as np

num = 30

t = 100000
balls = np.array([0]*6 + [1]*(num-6))

choices = [4-np.count_nonzero(np.random.choice(balls, 4)) for i in range(t)]
print("pr(X=0) = ", choices.count(0)/t)
print("pr(X=1) = ", choices.count(1)/t)
print("pr(X=2) = ", choices.count(2)/t)
print("pr(X=3) = ", choices.count(3)/t)
print("pr(X=4) = ", choices.count(4)/t)

