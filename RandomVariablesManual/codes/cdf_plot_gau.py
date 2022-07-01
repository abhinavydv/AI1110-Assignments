# Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath
from funcs import qfunc


# if using termux
#import subprocess
#import shlex
# end if


def gau_cdf(x):
    return 1-qfunc(x)


x = np.linspace(-4, 4, 30)  # points on the x axis
simlen = int(1e6)  # number of samples
err = []  # declaring probability list
#randvar = np.random.normal(0,1,simlen)
# randvar = np.loadtxt('uni.dat', dtype='double')
randvar = np.loadtxt('gau.dat', dtype='double')
# randvar = np.loadtxt('ln.dat', dtype='double')
for i in range(0, 30):
    err_ind = np.nonzero(randvar < x[i])  # checking probability condition
    err_n = np.size(err_ind)  # computing the probability
    err.append(err_n/simlen)  # storing the probability values in a list

vec_gau_cdf = np.vectorize(gau_cdf)

plt.plot(x.T, err, "o")  # plotting the CDF
plt.plot(x, vec_gau_cdf(x))
plt.grid()  # creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical", "Theory"])

# if using termux
# plt.savefig('../figs/uni_cdf.pdf')
# plt.savefig('../figs/uni_cdf.eps')
# plt.savefig('../figs/ln_cdf.pdf')
# plt.savefig('../figs/ln_cdf.eps')
# plt.show()
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
# if using termux
plt.savefig('../figs/gauss_cdf.pdf')
plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
# else
plt.show()  # opening the plot window
