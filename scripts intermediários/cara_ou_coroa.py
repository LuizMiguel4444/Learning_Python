from random import randint

print("= " * 17)
print("= = = = = Cara ou Coroa = = = = =")
print("= " * 17)
print()

resp = input("Deseja começar o jogo (S/N)? ").upper()
while resp == "S":
  print()
  i = 1
  rod = int(input("Quantas rodadas você quer jogar? "))
  ptsJog = 0
  ptsComp = 0
  while i <= rod:
    print()
    print("Rodada %d:"%i)
    jog = int(input("Digite 1 para Cara ou 2 para Coroa: "))
    moeda = randint(1,2)
    if (jog == 1) and (moeda == 1):
     print("Deu Cara, você ganhou essa rodada!")
     ptsJog = ptsJog + 1 
    elif (jog == 1) and (moeda == 2):
     print("Deu Coroa, o computador ganhou essa rodada!")
     ptsComp = ptsComp + 1  
    elif (jog == 2) and (moeda == 2):
     print("Deu Coroa, você ganhou essa rodada!")
     ptsJog = ptsJog + 1  
    else:
     print("Deu Cara, o computador ganhou essa rodada!")
     ptsComp = ptsComp + 1   
    i = i + 1  
  print()
  print()
  print()
  print()
  print()
  print("Você fez: %d ponto(s)!"%ptsJog)
  print("O computador fez: %d ponto(s)!"%ptsComp)
  print()
  if ptsJog > ptsComp:
    print("ENTÃO VOCÊ GANHOU O JOGO!")
  elif ptsComp > ptsJog:
    print("ENTÃO O COMPUTADOR GANHOU O JOGO!")
  else:
    print("ENTÃO O JOGO TERMINOU EMPATADO!")
  print()
  print()
  print()
  print()
  print()
  resp = input("Deseja jogar novamente (S/N)? ").upper()
  
print()
print("= " * 17)
print("= = = = = Fim do Jogo!! = = = = =")
print("= " * 17)