from random import randint

print("= " * 15)
print("= = = = Jogo de Dados = = = =")
print("= " * 15)
print()

resp = input("Deseja começar o jogo (S/N)? ").upper()
while resp == "S":
  print()
  i = 1
  n = int(input("Quantas rodadas você deseja jogar? " ))
  ptsJog = 0
  ptsComp = 0
  while i <= n:
    jog = randint(1,6)
    comp = randint(1,6)
    print()
    print("Rodada %d:"%i)
    print("Jogador tirou:", jog)
    print("Computador tirou:", comp)
    print()
    if jog > comp:
     print("O Jogador Ganhou!")
     ptsJog = ptsJog + 1 
    elif comp > jog:
     print("O Computador Ganhou!")
     ptsComp = ptsComp + 1 
    else:
     print("Deu Empate!")
    i = i + 1
  print()
  print()
  print()
  print()
  print()
  print("O Jogador fez: %d ponto(s)!"%ptsJog)
  print("O Computador fez: %d ponto(s)!"%ptsComp)
  print()

  if ptsJog > ptsComp:
    print("ENTÃO O JOGADOR GANHOU O JOGO!")
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
print("= " * 15)
print("= = = = Fim do Jogo!! = = = =")
print("= " * 15)