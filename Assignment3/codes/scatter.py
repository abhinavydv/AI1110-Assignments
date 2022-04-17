import matplotlib.pyplot as plt
from numpy import array
import numpy as np

data = array(["NumStu", "MaxTemp", "AvgRain", "NumStuProg", "NumMedals"])
classification = array(["Primary", "Secondary", "Secondary", "Secondary", "Secondary"])

plt.xlabel("Data")
plt.ylabel("Class")
plt.grid()

plt.scatter(data, classification, s=100, color="red")
plt.savefig("../figs/plot.png")
plt.show()

