'''
1) Print the following patterns using loop :

a.

*
**
***
****

b.

*
***
*****
***
*
'''

a = "*"
b = a
cont = 1
while cont < 5:
   print(b)
   b += a 
   cont +=1

print(" ")
      
b = ["*", "***", "*****", "***", "*"]
cont = 0
while cont < len(b):
   print(b[cont])
   cont += 1      

"""
#solução do Orlando
contador = 0
saida ="*"
n_linhas = 5
maximo = n_linhas//2

while contador < n_linhas:
    print(saida)
    if contador < maximo: saida += "**"
    else: saida = saida[:len(saida)-2]
    contador += 1
"""   