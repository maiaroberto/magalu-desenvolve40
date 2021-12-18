"""
Questão #4
Vale
20
Enunciado
Faça uma função que receba uma lista que contém números inteiros positivos e textos.

Retorne uma lista em que os primeiros elementos são os números pares ordenados em ordem crescente, seguidos pelos textos sem ordenação específica 
e depois pelos ímpares ordenados em ordem decrescente.

Não é necessário validar os dados de entrada. Assuma o enunciado.

Ex.: ['Casa', 1, 3, 'Fruta', 9, 1001, 'Escola', 8, 4, 'Aluno', 200]

Retorno: [4, 8, 200, 'Casa', 'Fruta', 'Escola', 'Aluno', 1001, 9, 3, 1]
"""
def separa(lista):
    cont = 0
    pares = []
    impar = []
    texto = []
    while cont < len(lista):
        if type(lista[cont]) == int:
            if lista[cont] % 2 == 0:
                pares.append(lista[cont])
            else:
                impar.append(lista[cont])    
        else:
            texto.append(lista[cont])    
        cont += 1   
    
    saida = sorted(pares) + texto + sorted(impar,reverse=True)
    return saida

lista = ['Casa', 1, 3, 'Fruta', 9, 1001, 'Escola', 8, 4, 'Aluno', 200]

print("Retorno: ", separa(lista))