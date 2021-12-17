"""
Faça um programa que imprima o maior número da lista sem usar a função max()

"""
lista = [34, 2, 5, 8, 8, 8, -37] 
lista_ordenada = sorted(lista) 
print(lista_ordenada[-1])

maior = lista[0]
cont = 1
while cont < len(lista): 
    if lista[cont] > maior: maior = lista[cont]
    cont += 1
print(maior)    