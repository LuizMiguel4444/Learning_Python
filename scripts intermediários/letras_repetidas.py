palavra = input("Digite uma palavra: ")
palavra = palavra.upper()
print()
print("A palavra que você digitou foi:", palavra)
print()
dic = {}
for letra in palavra:
  if letra not in dic:
    dic[letra] = 1
  else:
    dic[letra] += 1
print("A palavra", palavra, "possui:")   
print()
lista = []
for letra, quantidade in dic.items():
  print("%s = %sx"%(letra, quantidade))