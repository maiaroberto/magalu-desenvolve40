"""
Crie uma função que recebe uma lista e retorna True se todos os elementos forem do mesmo tipo e False caso contrário.
"""

def mesmoTipo(lista):
    tipo = type(lista[0])
    retorno = True
    cont = 1
    while cont < len(lista):
        if type(lista[cont]) != tipo:
             return False
        cont += 1
    return True

lista = [True, False, True]

print(mesmoTipo(lista))
 