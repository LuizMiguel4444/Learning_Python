# Escreva um programa em Python que encontre os números
# primos compreendidos entre a e b, onde os valores
# de a e b são fornecidos pelo usuário.

a = int(input("Digite o número inicial: "))
b = int(input("Digite o número final: "))
for i in range(a,b+1):
 primo = 0
 for x in range(1,i+1):
  if i%x == 0:
   primo += 1
 if primo == 2:
  print("Entre %d e %d são primos os números: %d"%(a,b,i))  