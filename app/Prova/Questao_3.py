"""
Questão #3
Vale
20
Enunciado
Faça um código que receba uma lista de números inteiros e exiba os elementos da última metade na frente dos elementos da primeira metade.

Não é necessário validar os dados de entrada. Assuma o enunciado.

Ex1: [1, 2, 3, 4, 5]

Retorna: [4, 5, 3, 1, 2]

Ex2: [1, 2, 3, 4, 5, 6]

Retorna: [4, 5, 6, 1, 2, 3]
"""
def inverte(lista):
    metade = len(lista) // 2
    if len(lista) % 2 != 0: metade +=1
    return lista[0:metade] + lista[metade:]

lista1 = [4, 5, 3, 1, 2]
lista2 = [1, 2, 3, 4, 5, 6]
print("Retorna: ", inverte(lista1))
print("Retorna: ", inverte(lista2))