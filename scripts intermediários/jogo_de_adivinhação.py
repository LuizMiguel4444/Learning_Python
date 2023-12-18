from random import randint

print("= " * 18)
print("= = = = = Acerte o Número = = = = =")
print("= " * 18)
print()
resp = input("Deseja iniciar o jogo (S/N)? ").upper()
while resp == "S":
  range = int(input("Acerte o número de 1 a quanto? "))
  num = randint(1,range)
  i = 1
  while i <= 3:
    print()
    print("%dª tentativa:"%i)
    chute = int(input("Digite o número que você acha que foi escolhido: "))
    if chute == num:
      if i == 1:
        print("VOCÊ TEVE MUITA SORTE!")
        print()
      elif i == 2:
        print("VOCÊ JOGA BEM, MAS AINDA CONTOU COM A SORTE!")
        print()
      else:
        print("VOCÊ É UM EXCELENTE ESTRATEGISTA!")  
        print()
      break
    elif chute != num:  
      if i == 3:
        print("ANALISE MELHOR SUA ESTRATÉGIA E TENTE JOGAR NOVAMENTE!")
        print()
      elif chute < num:
        print("DIGITE UM NÚMERO MAIOR!")
      else:
        print("DIGITE UM NÚMERO MENOR!")
    i = i + 1
  resp = input("Deseja jogar novamente (S/N)? ").upper()
print() 
print("= " * 18)
print("= = = = = = Fim do Jogo = = = = = =")
print("= " * 18)