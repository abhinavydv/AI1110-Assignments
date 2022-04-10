import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import linalg as la

points = np.loadtxt("data.txt", dtype=np.float)

points1 = points[:len(points)//2]
points2 = points[len(points)//2:]

x1 = np.array([i[0] for i in points1])
y1 = np.array([i[1] for i in points1])
z1 = np.array([i[2] for i in points1])

x2 = np.array([i[0] for i in points2])
y2 = np.array([i[1] for i in points2])
z2 = np.array([i[2] for i in points2])


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(x1, y1, z1)
ax.plot(x2, y2, z2)
ax.annotate("(0, 0, 0)", (0, 0))
ax.plot([0], [0], [0], markersize=5, marker="o", color="black")
plt.savefig("../figs/plot.png")


# Finding the angle
m = np.array([3, 2, -6])
n = np.array([2, -12, -3])

m_dot_n = np.dot(m, n)
norm_m = la.norm(m)
norm_n = la.norm(n)

# angle in radians
theta = np.arccos(m_dot_n/(norm_m*norm_n))

print(f"Angle between the lines: {theta} radians")
