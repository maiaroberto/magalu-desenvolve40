"""
Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir, a polícia reuniu um dos suspeitos e fez um questionário com 5 perguntas de sim ou não:

a) Telefonou para a vítima?
b) Esteve no local do crime?
c) Mora perto da vítima?
d) Devia para a vítima?
e) Já trabalhou com a vítima?

Cada resposta 'sim' dá um ponto para o suspeito. 
Suspetitos com 5 pontos são assassinos, 
4-3 pontos são cúmplices, 
2 são apenas suspetitos 
e 1-0 são liberados"""

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
    