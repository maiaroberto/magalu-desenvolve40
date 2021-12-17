#4) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma:
#
# 𝑎𝑥2+𝑏𝑥+𝑐 
# O programa deverá pedir os valores de a, b e c, 
# informando ao usuário nas seguintes situações: 
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
# e o programa não deve fazer pedir os demais valores, sendo encerrado; 
# Se o delta calculado for negativo, a equação não possui raizes reais. 
# Informe ao usuário e encerre o programa; 
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; 
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

 print("Equação do 2° Grau")

a = float(input("Valor a = "))

if a != 0:
   b = float(input("Valor b = "))
   c = float(input("Valor c = "))
    
   delta = b**2 -4*a*c
   
   if delta < 0: 
      print("A equação não possui raizes Reais") 
   elif delta == 0:       
      x1 = (-b) / (2*a)
      print(f"x = {x1:.4f}")     
   else: 
      x1 = (-b - (delta)**(1/2)/(2*a))     
      x2 = (-b + (delta)**(1/2)/(2*a))
      print(f"x1 = {x1:.4f}")     
      print(f"x2 = {x2:.4f}")     
else:              
   print("Não é uma equação do 2° Grau")