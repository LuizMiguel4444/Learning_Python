# O número 3025 possui a seguinte característica:
# 30 + 25 = 55 e 55**2 = 3025. Escreva um programa em Python
# que encontre os outros números que possuem a citada característica.

print("Os números com essa característica entre 0 e 10000 são:")
for i in range(1, 9999):
    parte1 = i // 100
    parte2 = i % 100
    if i == (parte1 + parte2) ** 2 and i != 1:
        print(i, end=" ")
