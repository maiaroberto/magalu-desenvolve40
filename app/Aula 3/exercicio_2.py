"""
Faça um algoritmo que recebe uma lista encadeada de números inteiros 
e retorna uma lista sem repetições, ou seja, uma lista onde cada número apareça apenas uma vez. 
Exemplo:

12, 5, -7, 8, 5, 9, 12, 1, 8
®: 12, 5, -7, 8, 9, 1
"""
lista = [12, 5, -7, 8, 5, 9, 12, 1, 8]

cont = 0
saida = []
while cont < len(lista):

    if lista[cont] in saida:
        pass
    else:
        saida.append(lista[cont])
    
    cont += 1
    
print(saida)    