"""
Faça um programa que peça para o usuário digitar o nome de um aluno, a idade dele e o número de provas que esse aluno fez.

Depois disso o programa deve pedir para o usuário digitar as notas de cada prova do aluno.

Ao final o programa deve imprimir uma lista contendo:

a. Nome do aluno na posição 0

b. Idade do aluno na posição 1

c. Uma lista com todas as notas na posição 2

d. A média do aluno na posição 3

e. True ou False, caso a média seja maior que 5 ou não, na posição 4

"""
aluno = input("Aluno: ")
idade = int(input("Idade: "))
prova = int(input("Provas: "))

cont = 1
notas = []

notas.append(aluno)
notas.append(idade)

provas =[]
while cont < prova+1: 
    provas.append(int(input(f"Digite {cont}º nota: " )))
    cont +=1

notas.append(provas) 
media = sum(provas)/len(provas)
notas.append(media)
notas.append(media>5)
print(notas)    
