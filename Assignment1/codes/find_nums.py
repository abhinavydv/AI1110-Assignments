"""
    Python code to find the numbers described in the question:
        The product of two consecutive natural numbers which are multiples
        of 3 is equal to 810. Find the two numbers.
"""


from numpy import array, linspace, roots, round, zeros
import matplotlib.pyplot as plt


def my_sum(*args):
    """
    Returns sum of the provided arguments
    """
    s = 0
    for i in args:
        s += i
    return s


def plot(coeffs, roots):
    """
        Plots the given polynomial so that all roots are covered.

        Parameters
        ----------
        `coeffs`: An array of coefficients of polynomial
        `roots`: An array of roots of polynomial
    """

    x = linspace(1.2*min(roots), 1.2*max(roots), 1000)
    x_axis = zeros(1000)

    temp = [coeffs[i]*x**i for i in range(len((coeffs)))]
    y = array(list(map(my_sum, *temp)))
    plt.plot(x, y)
    plt.plot(x, x_axis, color="black")  # x-axis

    y_axis = linspace(1.2*min(y), 1.2*max(y), 1000)
    plt.plot(x_axis, y_axis, color="black")

    points = [(0, 0), *[(i, 0) for i in roots]]
    for i in points:
        plt.annotate(str(i), i, xytext=(i[0]+0.5, i[1]+20))

    plt.savefig("../images/plot.png")

    plt.show()


def find_consecutive_nums(multiple_of, product):
    """
        Parameters
        ----------
        `multiple_of`: The number whose multiple the desired numbers are
        `product`: The product of the two desired numbers

        Returns
        -------
        two consecutive natural numbers which are multiples of `multiple_of`
        and whose product is `product`
    """

    # equation :  (multiple_of)**2*x**2 + (multiple_of)**2*x - (product) = 0

    coefficients = [multiple_of**2, multiple_of**2, -product]

    n1, n2  = roots(coefficients)
    n1, n2 = round((n1, n2))
    n1, n2 = int(n1), int(n2)

    plot(coefficients[::-1], (n1, n2))

    if (n1>0):
        return multiple_of*n1, multiple_of*(n1+1)
    else:
        return multiple_of*n2, multiple_of*(n2+1)


if __name__ == "__main__":
    multiple_of = 3
    product = 810
    n1, n2 = find_consecutive_nums(multiple_of, product)

    try:
        # Verification
        assert n1>0 and n2>0
        assert n1%multiple_of == 0 and n2%multiple_of == 0
        assert n2-n1 == multiple_of
        assert n1*n2 == product
        print(
            f"The consecutive natural numbers n1 and n2 s.t.\n"
            f"n1 % {multiple_of} == 0  and  n2 % {multiple_of} == 0 and n1*n2 == {product} are:\n"
            f"{n1=}\t{n2=}"
        )
    except AssertionError:
        # if verification failed
        print("No such numbers found")
