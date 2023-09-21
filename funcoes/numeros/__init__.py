def somar(*nums):
    """
    Retorna a soma dos números fornecidos, independentemente se passados como argumentos individuais,
    em uma lista ou em uma tupla.

    :param nums: Números que deseja somar. Pode ser uma sequência de números ou vários argumentos.
    :return: Valor da soma de todos os números.
    :rtype: int ou float
    """
    soma = 0

    for seq in nums:
        if isinstance(seq, (list, tuple)):
            soma += sum(seq)
        else:
            soma += seq

    return soma
