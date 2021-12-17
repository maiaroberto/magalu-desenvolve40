"""
5) Seguindo a mesma ideia do exercício 4, faça a soma da seguinte sequência:

11!+12!+13!+14!+15!+16!+...+1100!

"""
# fatorial de um número
def fatorial(num):
  if num <= 1:
    return 1
  else:
    return num * fatorial(num - 1)
 

def main():
   soma = 0.0
   cont = 1
   while cont < 11:
      print(cont)
      soma += 1/ fatorial(cont)
      cont += 1
   print(soma)
  
if __name__== "__main__":
  main()