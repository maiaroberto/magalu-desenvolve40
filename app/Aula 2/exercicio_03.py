#3) Faça um Programa que leia um número inteiro menor que 1000 
# e imprima a quantidade de centenas, dezenas e unidades do mesmo. 
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

numero = int(input("Digite um número menor que 1000: "))

num = (numero * -1) if numero < 0 else numero
  
c = num // 100
d = (num - (c*100)) // 10
u = num - (c*100) - (d*10)

texto = f"{numero} = "
liga = ""
if c > 0:
   texto += f"{c} Centena" if c == 1 else f"{c} Centenas"
   liga = ", " 
if d > 0: 
  texto += liga + (f"{d} dezena" if d == 1 else f"{d} dezenas")
  liga = " e " 

if u > 0: 
  texto += liga + (f"{u} unidade" if u == 1 else f"{u} unidades")

print(texto)
