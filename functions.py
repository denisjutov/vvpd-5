import math

def exponential(x, n_terms=10):
    """
    Вычисляет экспоненту e^x с использованием ряда Тейлора.
    :param x: Значение, для которого вычисляется экспонента.
    :param n_terms: Количество членов ряда (по умолчанию 10).
    :return: Значение e^x.
    """
    result = 0
    for n in range(n_terms):
        result += x**n / math.factorial(n)
    return result

def hyperbolic_sine(x, n_terms=10):
    """
    Вычисляет гиперболический синус sh(x) с использованием ряда Тейлора.
    :param x: Значение, для которого вычисляется sh(x).
    :param n_terms: Количество членов ряда (по умолчанию 10).
    :return: Значение sh(x).
    """
    result = 0
    for n in range(n_terms):
        result += x**(2*n + 1) / math.factorial(2*n + 1)
    return result