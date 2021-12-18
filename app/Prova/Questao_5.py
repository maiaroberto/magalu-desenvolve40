"""
Questão #5
Vale
20
Enunciado
Faça uma função que recebe uma lista de números inteiros positivos. 
O objetivo da função é identificar quais valores da lista são picos.

Picos são valores que estão entre dois valores menores que ele. 

Sua função deve retornar uma lista com a posição de todos os picos.

Exemplo:

Ex1: [1, 4, 3]

Retorno: [1]

Nesta lista, o valor na posição 1 (com valor 4) é um pico.
Ex2: [1, 2, 3, 4, 2, 3, 1, 2, 2]

Retorno: [3, 5]

Nesta lista os valores nas posições 3 e 5 (com valores 4 e 3) são picos.
Ex3: [1, 2, 2, 2, 4, 5]

Retorno: []

Nesta lista, nenhum valor é pico.
Ex4: [1, 3, 3, 3, 1]

Retorno: []

Nesta lista, nenhum valor é pico.
Obs.: O primeiro e último elemento da lista nunca são picos.

Não é necessário validar os dados de entrada. Assuma o enunciado.
"""
def pico(lista):
    cont = 1
    listaPicos = []
    while cont < len(lista)-1:
        if lista[cont] > lista[cont-1] and lista[cont] > lista[cont+1]: 
           listaPicos.append(cont)  
        cont += 1
        
    return listaPicos       

ex1 = [1, 4, 3]    
print("Retorno 1: ", pico(ex1))

ex2 = [1, 2, 3, 4, 2, 3, 1, 2, 2]
print("Retorno 2: ", pico(ex2))

ex3 = [1, 2, 2, 2, 4, 5]
print("Retorno 3: ", pico(ex3))

ex4 = [1, 3, 3, 3, 1]
print("Retorno 4: ", pico(ex4))

ex5 = [9, 2, 1, 4, 2, 6, 5]
print("Retorno 4: ", pico(ex5))
