import numpy as np
import matplotlib.pyplot as plt


def mark_points(points, marker='o', markersize=5, color='black'):
    """
    Marks the given points on the plot and annotates their coordinates
    """

    for i in points:
        plt.plot(i[0], i[1], marker=marker, markersize=markersize, color=color)
        plt.annotate(str(i), i, xytext=(i[0]+0.5, i[1]+20))


def plot(file_path):
    """
    Plots points from given text file
    """

    data = np.loadtxt(file_path, np.float)
    roots, *data = data
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    x_axis = np.zeros(1000)
    y_axis = np.linspace(1.2*min(y), 1.2*max(y), 1000)

    points = [(0, 0), *[(i, 0) for i in roots]]
    mark_points(points)

    plt.grid()
    plt.plot(x, y)
    plt.plot(x, x_axis, color="black")
    plt.plot(x_axis, y_axis, color="black")
    plt.savefig("../figs/plot.png")
    plt.show()


if __name__ == "__main__":
    plot("data.txt")
