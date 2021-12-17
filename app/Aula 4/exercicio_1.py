"""
Faça uma função que recebe dois parâmetros: linhas e colunas e desenhe uma tabela usando os caracteres (-, |, + e espaços) com essas dimensões, exemplo:

linhas: 3 colunas: 5

-----------
| | | | | |
|-+-+-+-+-|
| | | | | |
|-+-+-+-+-|
| | | | | |
-----------
"""

def topoBase(c):
    print("-" * (c*2 + 1))
    return

def meio(c):
    texto = "|"
    n = 1    
    
    while n <= c:
        if n < c:
            texto += "-+"
        else:
            texto += "-|" 
        n += 1    
        
    print(texto)
    return

def miolo(c):
    print("|" + (" |" * c) )
    return

print("Desenha Tabela")

linha = 0
coluna = 0
while linha <= 0 or coluna <=0:
    linha = int(input("linhas  : "))
    coluna = int(input("Colunas : "))
    
i = 1
topoBase(coluna)   
while i <= linha:
    miolo(coluna) 
    i += 1
    if i <= linha:
        meio(coluna)
topoBase(coluna)    
