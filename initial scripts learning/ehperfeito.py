# Escreva um programa em Python que leia um número
# inteiro n e determine se esse número é perfeito.
# Um número é dito perfeito se o dobro dele é igual
# à soma de todos os seus divisores.
# Ex: os divisores de 6 são 1, 2, 3 e 6,
# 1 + 2 + 3 + 6 = 12, então 6 é perfeito.

a = int(input("Digite um número: "))
for i in range(1,a+1):
 ideal = 0
 for x in range(1,i+1):
			if i % x == 0:
	 			ideal += x
if (i*2) == ideal:
	print("%d é um número perfeito!"%a)
else:
	print("%d não é um número perfeito!"%a)