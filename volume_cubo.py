def calculo_volume_cubo(l):
    if l <= 0:
        raise ValueError('O valor do lado do cubo deve ser um número real positivo.')
    if type(l) not in [int, float]:
        raise TypeError('O valor do lado do cubo deve ser um número real ou inteiro')
    return (l*l*l)
