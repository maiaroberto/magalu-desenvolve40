# Solução do Brian

area_pintada = float(input("Qual a área a ser pintada? "))
qtnde_litros = area_pintada/6

latas = qtnde_litros/18

galoes = qtnde_litros/3.6
qtnde_litros = qtnde_litros * 1.1 # qtnde_litros *= 1.1
latas_mista = qtnde_litros//18
galoes_mista = (qtnde_litros%18)/3.6
print(f"Você precisa comprar {latas } latas pagando R${latas*80}")
print(f"Você precisa comprar {galoes} galoes pagando R${galoes*25}")
print(f"Você precisa comprar {latas_mista} latas e {galoes_mista} galoes pagando R${galoes_mista*25 + latas_mista*80}")
