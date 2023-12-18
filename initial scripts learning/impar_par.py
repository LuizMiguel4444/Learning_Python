# Escreva um programa em Python que gere uma lista de 20 valores
# inteiros aleatórios positivos, compreendidos no intervalo de 
# 1 a 100 (inclusive), obtidos a partir da função random. randint (a,b).
# Em seguida, a lista deve ser particionada em duas outras listas,
# a primeira apenas com os valores pares e a segunda apenas com os valores ímpares.
# Exiba as três listas e a quantidade de elementos existentes em cada uma delas.

import random

lista = []
for i in range(20):
  x = random.randint(1,100)
  lista.append(x)

pares = []
impares = []
for x in lista:
  if x % 2 == 0:
    pares.append(x)
  else:
    impares.append(x)

print("Lista original:")
print()
print(lista)
print()
print("Lista pares:")
print()
print(pares)
print()
print("Lista ímpares:")
print()
print(impares)