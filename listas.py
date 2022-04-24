def ordenar_lista(lista):
    for elemento in lista:
        if type(elemento) not in [int, float]:
            raise TypeError('O valor do elemento deve ser um número real ou inteiro')
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    temp = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temp
    return lista
