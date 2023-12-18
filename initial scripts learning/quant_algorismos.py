# Escreva um programa em Python que leia um número inteiro positivo
# lido a partir do teclado e determine o número de algarismos deste número.

a = int(input("Digite um número: "))
alg = 0
while a > 0:
	a = a // 10
	alg += 1
print("O número de algarismos desse número é:",alg)