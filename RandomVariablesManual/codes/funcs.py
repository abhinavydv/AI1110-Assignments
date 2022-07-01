import mpmath


def qfunc(x):
    return mpmath.erfc(x/mpmath.sqrt(2))/2
