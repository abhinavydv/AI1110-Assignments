"""
    Python code to find the numbers described in the question:
        The product of two consecutive natural numbers which are multiples
        of 3 is equal to 810. Find the two numbers.
"""


from math import floor, sqrt


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

    temp = product/multiple_of**2
    n = floor(sqrt(temp))

    return multiple_of*n, multiple_of*(n+1)


if __name__ == "__main__":
    multiple_of = 3
    product = 810
    n1, n2 = find_consecutive_nums(multiple_of, product)

    try:
        # Verification
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
