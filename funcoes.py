import math


def funcao(d, a):
    """
    Função do Tema 1:
    f(d) = a*d - d*ln(d)
    """

    return a * d - d * math.log(d)

def derivada(d, a):
    """
    Derivada da função do Tema 1:
    f'(d) = a - ln(d) - 1
    """

    return a - math.log(d) - 1