"""
Faça uma função maxLista que faz a mesma coisa que a funcão max faz ao receber uma lista (Sem usar o max ou sort)
"""

def maxLista(lista):
    maximo = lista[0]
    cont = 0
    while cont < len(lista):
        if lista[cont] > maximo: maximo = lista[cont] 
        cont += 1    
    return maximo

lista = [-1, -32, -4, -110, -9, 111]

print(maxLista(lista))
