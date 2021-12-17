"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Após o usuário digitar, o programa deve mostrar na tela uma das opções: 
F - Feminino, M - Masculino ou Sexo Inválido. 
O programa deve funcionar para letras maiúsculas e minúsculas.
"""
sexo = input("Digite M=Masculino ou F=Feminino ")
if sexo == "M" or sexo == "m":
    print("Masculino")
elif sexo == "F" or sexo == "f":    
    print("Feminino")
else:    
    print("Sexo invalido")