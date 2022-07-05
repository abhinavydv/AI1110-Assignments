import matplotlib.pyplot as plt
import numpy as np

y = np.loadtxt("maximul.dat", dtype="float")

x = np.random.random(1000000)

plt.scatter(x, y)
plt.savefig("../figs/maximul_scatter.png")
# plt.savefig("../figs/maximul.pdf")
# plt.savefig("../figs/maximul.eps")
plt.show()
