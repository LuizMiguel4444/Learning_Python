# Escreva um programa em Python que
# encontre os números primos entre 100 e 500.

for i in range(100, 501):
    primo = 0
    for x in range(1, i+1):
        if i % x == 0:
            primo += 1
    if primo == 2:
        print("O número %d é primo!" % i)
