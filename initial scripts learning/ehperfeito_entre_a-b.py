# Escreva um programa em Python que leia dois valores a e b
# e encontre os números perfeitos compreendidos dentro desse intervalo.

a = int(input("Digite o valor inicial: "))
b = int(input("Digite o valor final: "))
for i in range(a,b+1):
 ideal = 0
 for x in range(1,i+1):
  if i % x == 0:
   ideal += x
 if (i*2) == ideal:
  print("%d é um número perfeito!"%i)