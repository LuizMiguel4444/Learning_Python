# Escreva um programa em Python que leia um número inteiro
# e verifique se o valor lido é um número primo.

x = int(input("Digite um número: "))
primo = 0
for i in range(1, x+1):
    if x % i == 0:
        primo += 1
if primo == 2:
    print("O número %d é primo!" % x)
else:
    print("O número %d não é primo!" % x)
