# 2) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" 
# e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

telefonou = input("Telefonou para a vítima?")
esteve = input("Esteve no local do crime?")
mora = input("Mora perto da vítima?")
devia = input("Devia para a vítima?")
trabalhou = input("Já trabalhou com a vítima?")

classifica = 0

if telefonou == 'S' or telefonou == 's': classifica +=1 
if esteve == 'S' or esteve == 's': classifica +=1 
if mora == 'S' or mora == 's': classifica +=1 
if devia == 'S' or devia == 's': classifica +=1 
if trabalhou == 'S' or trabalhou == 's': classifica +=1 

if classifica == 5:
    print("Assasino")
elif classifica >=3:
    print("Cumplice")
elif classifica >=2:
    print("Suspeita")
else:
    print("Inocente")