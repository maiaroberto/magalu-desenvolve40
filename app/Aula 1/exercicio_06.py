""" 
6) Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam 80,00 reais ou em galões de 3,6 litros, que custam 25,00 reais.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

Comprar apenas latas de 18 litros;
Comprar apenas galões de 3,6 litros;
Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
(É possível fazer isso com o que aprendemos até agora?)

"""
print("LOJA DE TINTAS")

coberturaTinta = 6.0
lataLitro = 18.0
galaoLitro = 3.6
precoLata = 80.00
precoGalao = 25.00

area = float(input("Digite a área (m2) a ser pintada: "))

litros = area / coberturaTinta

lata  = litros // lataLitro
galao = litros // galaoLitro
  
valorLatas = lata * precoLata
valorGaloes= galao * precoGalao

litros *= 1.1
mixLata  = litros // lataLitro 

resto = (litros - (mixLata * lataLitro)) 
mixGalao = round( resto / galaoLitro) 

valorMix = (mixGalao * precoGalao) + (mixLata * precoLata)

print("As opções são:")
print(f"1a. Comprar {lata} lata(s) de {lataLitro} Litros, ao custo de {precoLata:.2f} por Lata, dá um total de {valorLatas:.2f}" )
print(f"2a. Comprar {galao} galão(ões) de {galaoLitro} Litros, ao custo de {precoGalao:.2f} por galão, dá um total de {valorGaloes:.2f}")
print(f"3a. Comprar {mixLata} lata(s) + {mixGalao} galão(ões), em um total de {valorMix:.2f}")