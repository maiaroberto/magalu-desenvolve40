"""
Crie uma função que receba uma lista e retorne uma nova lista com os elementos únicos da primeira lista. 
Ex: [1, 1, 2, 2, 2, 3, 4, 4, 5, 5] Retorna: [1, 2, 3, 4, 5]
"""
def unica(lista):
    cont = 0
    saida = []
    while cont < len(lista):
        if not lista[cont] in saida:
            saida.append(lista[cont])
        cont += 1
    return saida

lista = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5]

print(unica(lista))    
