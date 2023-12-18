print("= " * 18)
print("= = = = = = = Olá!!!! = = = = = = = ")
print("= = = = = bem vindo à sua = = = = = ")
print("= = = = = tabuada virtual = = = = = ")
print("= " * 18)
print()
resp = input("Deseja iniciar a tabuada (S/N)? ").upper()
while resp == "S":
  print()
  num = int(input("Digite um número: "))
  print()
  i = 0
  while i <= 10:
    x = num * i
    print("%d x %d = %d"%(num, i, x))
    i = i + 1
  print()  
  resp = input("Deseja digitar outro número (S/N)? ").upper()
print()
print("= " * 18)
print("= = = = = =  Tudo bem,  = = = = = =")
print("= = = = =  até a próxima  = = = = =")
print("= " * 18)