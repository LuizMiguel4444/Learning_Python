import os
from time import sleep

print("Bem-vindo(a) a urna eletrôica.")
print()
print("O objetivo dessa votação é apurar qual é o héroi da marvel favorito do público. Os personagens incluídos nessa votação são: Homem de ferro, Capitão América, Homem Aranha, Hulk e Thor.")
print()
print("A urna recebe apenas um voto por pessoa.")
print()
print("Até então 0 pessoas votaram, portanto, os votos estão todos zerados.")
print()

votantes = int(input("Quantas pessoas irão votar? "))
print()
print("Ok...")
print()

if votantes >= 1:
  cmc = input("Pressione qualquer letra para começar a votação...")
  i = 0
  c = 0
  s = 0
  h = 0
  t = 0
  n = 0
  os.system('cls')
  cpf = {}
  for pessoas in range(1, votantes + 1):
    print("Entrevistando a %dª pessoa:"%pessoas)
    print()
    cpfx = input("Digite seu cpf: ")
    print()
    while cpfx in cpf:
      print("O cpf digitado já foi utilizado.")
      print()
      print("Obrigado e até a próxima.")
      delay = 8
      sleep(delay)
      os.system('cls')
      print("Entrevistando a %dª pessoa:"%pessoas)
      print()
      cpfx = input("Digite seu cpf: ")
      print()
    cpf[cpfx] = True
    voto = input("Digite 'I' para votar no Homem de ferro, 'C' para votar no Capitão América, 'S' para votar no Homem Aranha, 'H' para votar no Hulk, 'T' para votar no Thor, ou digite 'N' para votar em nenhuma das opções: ").lower()
    while voto.lower() not in ["i", "c", "s", "h", "t", "n"]:
      print()
      print("Você votou em uma opção inválida! Por favor, vote novamente em uma opção válida.")
      print()
      voto = input("Digite 'I' para votar no Homem de Ferro, 'C' para votar no Capitão América, 'S' para votar no Homem Aranha, 'H' para votar no Hulk, 'T' para votar no Thor, ou digite 'N' para votar em nenhuma das opções: ").lower()
    if voto.lower() == "i":
      print()
      print("Você votou no Homem de Ferro!")
      i += 1
      print()
      print("Seu voto já foi computado. Obrigado por ter votado.")
    elif voto.lower() == "c":
      print()
      print("Você votou no Capitão América!")
      c += 1
      print()
      print("Seu voto já foi computado. Obrigado por ter votado.")
    elif voto.lower() == "s":
      print()
      print("Você votou no Homem Aranha!")
      s += 1
      print()
      print("Seu voto já foi computado. Obrigado por ter votado.")
    elif voto.lower() == "h":
      print()
      print("Você votou no Hulk!")
      h += 1
      print()
      print("Seu voto já foi computado. Obrigado por ter votado.")
    elif voto.lower() == "t":
      print()
      print("Você votou no Thor!")
      t += 1
      print()
      print("Seu voto já foi computado. Obrigado por ter votado.")
    elif voto.lower() == "n":
      print()
      print("Você votou em nenhuma das opções!")
      n += 1
      print()
      print("Seu voto já foi computado. Obrigado por ter votado.")
    delay = 8
    sleep(delay)
    os.system('cls')
  print("A votação foi encerrada!")
  print()
  print("Foram entrevistadas %d pessoas."%pessoas)
  print()

  # EU NÃO CONSEGUI PENSAR EM UMA LÓGICA COMPUTACIONAL
  # EFICIENTE PARA REALIZAR ESSA PARTE ENTRE OS '#', QUE SERIA
  # DESTINADA A PRINTAR OS RESULTADOS EM ORDEM DECRESCENTE.
  # ENTÃO PEDI AJUDA AOS UNIVERSITÁRIOS. (CHATGPT).

  ##########
  pers = {
    "Homem de Ferro": i,
    "Capitão América": c,
    "Homem Aranha": s,
    "Hulk": h,
    "Thor": t,
    "Nenhuma opção": n
  }
  voto = sorted(pers.items(), key=lambda x: x[1], reverse=True)
  ##########

  for heroi, votos in voto:
    porc = votos / pessoas * 100
    print("%d pessoa(s) escolheu(ram) %s."%(votos, heroi))
    print("A porcentagem dos votos para o %s foi de: %.1f"%(heroi, porc), "% do total.")
    print()
  print("*" * 60)
  print()
  print("O número de votos predefinido foi atingido. (%d)"%votantes)
print("Encerrando a urna eletrônica...")
print()
des = input("Pressione qualquer letra para desligar a urna...")
os.system('cls')