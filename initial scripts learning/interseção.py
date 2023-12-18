# Escreva um programa em Python que leia dois conjuntos de valores inteiros,
# cada um com 10 elementos, e armazene-os em duas listas A e B. Em seguida,
# o programa deverá construir o conjunto UNIÃO, que representa a união das
# listas A e B, e o conjunto INTERSECÇÃO, que inclui apenas os elementos que
# estão simultaneamente nas duas listas A e B. Lembre-se que conjuntos
# não devem possuir elementos repetidos.

import random 

listaA = []
listaB = []
i = 0
while i < 10:
  x = random.randint(1,99)
  if x not in listaA:
    i += 1
    listaA.append(x)

i = 0
while i < 10:
  x = random.randint(1,99)
  if x not in listaB:
    i += 1
    listaB.append(x)

uniao = []
for x in listaA:
  uniao += [x]
for x in listaB:
  if x not in uniao:
    uniao += [x]

inter = []
for x in listaA:
  if x in listaB:
    inter += [x]

print("Conjunto A:")
print()
print(sorted(listaA, key=int))
print()
print("Conjunto B:")
print()
print(sorted(listaB, key=int))
print()
print("Conjunto União:")
print()
print(sorted(uniao, key=int))
print()
print("Conjunto Interseção:")
print()
print(sorted(inter, key=int))