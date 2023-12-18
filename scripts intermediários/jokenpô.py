from random import randint

print("= " * 20)
print("= = = = Pedra, papel ou tesoura = = = =")
print("= " * 20)
print()

resp = input("Deseja iniciar o jogo (S/N)? ").upper()
while resp == "S":
  print()
  i = 1
  n = int(input("Quantas rodadas você deseja jogar? "))
  ptsJog = 0
  ptsComp = 0
  while i <= n:
    print()
    print("Rodada %d:"%i)
    esc = int(input("Escolha '1' para pedra, '2' para papel e '3' para tesoura: " ))
    esc1 = randint(1,3)
    print()
    
    # # # # # # # # # # # JOGADOR # # # # # # # # # # # # #
    if esc == 1:
      print("O jogador escolheu pedra!")
    elif esc == 2:
      print("O jogador escolheu papel!")
    elif esc == 3:
      print("O jogador escolheu tesoura!")
    # # # # # # # # # # # # MÁQUINA # # # # # # # # # # # #
    if esc1 == 1:
      print("A máquina escolheu pedra!")
    elif esc1 == 2:
      print("A máquina escolheu papel!")
    elif esc1 == 3:
      print("A máquina escolheu tesoura!")
    print()  
    # # # # # # # # # # # RESULTADO # # # # # # # # # # # #
    if (esc ==1 ) and (esc1 == 3):
      print("ENTÃO, O JOGADOR GANHOU A RODADA!")
      ptsJog = ptsJog + 1
    elif (esc == 2) and (esc1 == 1):
      print("ENTÃO, O JOGADOR GANHOU A RODADA!")
      ptsJog = ptsJog + 1
    elif (esc == 3) and (esc1 == 2):
      print("ENTÃO, O JOGADOR GANHOU A RODADA!")
      ptsJog = ptsJog + 1
    elif esc == esc1:
      print("ENTÃO, ESSA RODADA DEU EMPATE!")
    else: 
      print("ENTÃO, A MÁQUINA GANHOU A RODADA!")
      ptsComp = ptsComp + 1
    i = i + 1
  print()
  print()
  print()
  print()
  print("*" * 32)
  print("O Jogador ganhou %d rodada(s)!"%ptsJog)
  print("A máquina ganhou %d rodada(s)!"%ptsComp)
  print()
  if ptsJog > ptsComp:
    print("ENTÃO, O JOGADOR GANHOU O JOGO!")
  elif ptsComp > ptsJog:  
    print("ENTÃO, A MÁQUINA GANHOU O JOGO!")
  else:
    print("ENTÃO, O JOGO EMPATOU!")
  print("*" * 32)
  print() 
  print()
  print()
  print()
  resp = input("Deseja jogar novamente (S/N)? ").upper()
print()
print("= " * 20)
print("= = = = = = = Fim do jogo = = = = = = =")
print("= " * 20)