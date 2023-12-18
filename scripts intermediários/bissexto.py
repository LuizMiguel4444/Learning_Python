ano = int(input("Digite o ano que você deseja saber se é bissexto: "))
print()
if (ano % 4 == 0) and (ano % 100 != 0):
  print("%d é bissexto."%ano)
elif (ano % 400 == 0):
  print("%d é bissexto."%ano)
else:
  print("%d não é bissexto."%ano)