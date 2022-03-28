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

    if product <= 0 or multiple_of<=0:
        return 0, 0

    temp = product/multiple_of**2
    n = floor(sqrt(temp))

    if n*(n+1) != temp:
        return 0, 0

    return multiple_of*n, multiple_of*(n+1)


if __name__ == "__main__":
    multiple_of = 5
    product = 750
    n1, n2 = find_consecutive_nums(multiple_of, product)

    if n1:
        print(
            f"The consecutive natural numbers n1 and n2 s.t.\n"
            f"n1 % {multiple_of} == 0  and  n2 % {multiple_of} == 0 and n1*n2 == {product} are:\n"
            f"{n1=}\t{n2=}"
        )
    else:
        print(
            f"No consecutive natural numbers n1 and n2 found s.t.\n"
            f"n1 % {multiple_of} == 0  and  n2 % {multiple_of} == 0 and n1*n2 == {product}"
        )
