"""
Questão #2
Vale
20
Enunciado
Faça um código Python que recebe uma lista e retorna uma outra lista contendo apenas os elementos que aparecem duas ou mais vezes na lista de entrada.

Não é necessário validar os dados de entrada. Assuma o enunciado.

Ex.: [1, 1, 'A', 2, 3, 3, 'B', 'B']

Retorno: [1, 3, 'B']

Ex.: [1, [1, 2], [1, 2], 4, 4, 5]

Retorno: [[1, 2], 4]
"""

def elimina(lista):
    cont = 0
    saida = []
    duplicada = []
    while cont < len(lista):

        if not lista[cont] in saida:
            saida.append(lista[cont])
        else:
            duplicada.append(lista[cont])    
        
        cont += 1
    return duplicada

lista = [1, 1, 'A', 2, 3, 3, 'B', 'B']
print("Retorno: ", elimina(lista))

lista = [1, [1, 2], [1, 2], 4, 4, 5]   
print("Retorno: ", elimina(lista))
