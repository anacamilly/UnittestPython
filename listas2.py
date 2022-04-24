def menor_elemento_lista(lista):
    for elemento in lista:
        if type(elemento) not in [int, float]:
            raise TypeError('O valor do elemento deve ser um número real ou inteiro')
    for i in range(len(lista)):
        if (i==0):
            menor_elemento = lista[i]
            indice = i
        elif (lista[i] < menor_elemento):
            menor_elemento = lista[i]
            indice = i
    return menor_elemento, indice