import os
from time import sleep

nomes = []
pesos = []
idades = []
alturas = []
sexos = []
i = 1

while i >= 0:
  print("= " * 20)
  print(" = = = = = = = =  Menu  = = = = = = = =")
  print("= " * 20)
  print(""" 
a. Cadastrar Dados
b. Exibir Dados Cadastrados
c. Exibir peso médio do grupo
d. Exibir idade média do grupo
e. Exibir altura média do grupo
f. Contagem de usuários de cada sexo
g. Nomes dos usuários com menor e maior peso do grupo
h. Nomes dos usuários com menor e maior idade do grupo
i. Nomes dos usuários com menor e maior altura do grupo
j. Relatório em ordem alfabética de todos os usuários cadastrados
k. Relatório com nome e idade dos usuários cadastrados ordenados pela idade
l. Sair
  """)
  opcao = input("Escolha uma das opções: ").lower()
  while opcao not in ["a","b","c","d","e","f","g","h","i","j","k","l"]: 
    print()
    print("Escolha uma opção válida.")
    print()
    opcao = input("Escolha uma das opções: ").lower()
  if opcao in ["a","b","c","d","e","f","g","h","i","j","k","l"]:
    os.system('clear')
    if opcao == "a":
      os.system('clear')
      nome = input("Digite seu nome: ")
      nomes.append(nome)
      print()
      peso = float(input("Digite seu peso (Kg): "))
      pesos.append(peso)
      print()
      idade = int(input("Digite sua idade: "))
      idades.append(idade)
      print()
      altura = float(input("Digite sua altura (m): "))
      alturas.append(altura)
      print()
      sexo = input("Digite seu sexo (M/F): ").upper()
      if sexo == "M":
        sexos.append("Masculino")
      elif sexo == "F": 
        sexos.append("Feminino")
      else:
        while sexo != "M" and sexo != "F":
          print()
          print("Resposta inválida. Por favor, digite novamente.")
          print()
          sexo = input("Digite seu sexo (M/F): ").upper()
          sexos.append(sexo)
      os.system('clear')
    elif opcao == "b":
      os.system('clear')
      if pesos == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      else:
        tam = len(nomes)
        for i in range(tam):
          print()
          print("Nome:",nomes[i])
          print()
          print("Peso:",pesos[i],"Kg")
          print()
          print("Idade:",idades[i],"anos")
          print()
          print("Altura:",alturas[i],"m")
          print()
          print("Sexo:",sexos[i])
          print()
          print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')  
    elif opcao == "c":
      os.system('clear')
      if pesos == []:
        print("Impossível calcular o peso médio do grupo.")
        print()
      else:
        os.system('clear')
        soma = 0
        for p in pesos:
          soma += p
        peso_medio = soma / len(pesos)
        print("O peso médio do grupo é: %.1f Kg"%peso_medio)
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')     
    elif opcao == "d":
      os.system('clear')
      if idades == []:
        print("Impossível calcular a idade média do grupo.")
        print()
      else:
        os.system('clear')
        soma = 0
        for i in idades:
          soma += i
        idade_media = soma / len(idades)
        print("A idade média do grupo é: %d anos"%idade_media)
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')     
    elif opcao == "e":
      os.system('clear')
      if alturas == []:
        print("Impossível calcular a altura média do grupo.")
        print()
      else:
        os.system('clear')
        soma = 0
        for a in alturas:
          soma += a
        altura_media = soma / len(alturas)
        print("A altura média do grupo é: %.2f m"%altura_media)
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')       
    elif opcao == "f":
      os.system('clear')
      if sexos == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      else:
        os.system('clear')
        hom = 0
        mul = 0
        for s in sexos:
          if s == "Masculino":
            hom += 1
          elif s == "Feminino":
            mul += 1
        print("Foram cadastrados %d homens e %d mulheres."%(hom,mul))
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear') 
    elif opcao == "g":
      os.system('clear')
      if pesos == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      elif len(pesos) == 1:
        print("A função não pode ser realizada, pois só tem um usuário cadastrado no sistema.")
        print()
      else:
        os.system('clear')    
        peso_menor = min(pesos)
        peso_maior = max(pesos)
        nome_do_menor = []
        nome_do_maior = []
        for n in range(len(nomes)):
          if pesos[n] == peso_menor:
            nome_do_menor.append(nomes[n])
          if pesos[n] == peso_maior:
            nome_do_maior.append(nomes[n])
        print("Usuário(s) com menor peso do grupo:", nome_do_menor, "com %.1f Kg"%peso_menor)
        print("Usuário(s) com maior peso do grupo:", nome_do_maior, "com %.1f Kg"%peso_maior) 
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')       
    elif opcao == "h":
      os.system('clear')
      if idades == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      elif len(idades) == 1:
        print("A função não pode ser realizada, pois só tem um usuário cadastrado no sistema.")
        print()
      else:
        os.system('clear')    
        idade_menor = min(idades)
        idade_maior = max(idades)
        nome_do_menor = []
        nome_do_maior = []
        for n in range(len(nomes)):
          if idades[n] == idade_menor:
            nome_do_menor.append(nomes[n])
          if idades[n] == idade_maior:
            nome_do_maior.append(nomes[n]) 
        print(nome_do_menor, "é(são) o(s) usuário(s) mais novo(s) do grupo com %d anos de idade."%idade_menor)
        print(nome_do_maior,"é(são) o(s) usuário(s) mais velho(s) do grupo com %d anos de idade."%idade_maior) 
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')       
    elif opcao == "i":
      os.system('clear')
      if alturas == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      elif len(alturas) == 1:
        print("A função não pode ser realizada, pois só tem um usuário cadastrado no sistema.")
        print()
      else:
        os.system('clear')    
        altura_menor = min(alturas)
        altura_maior = max(alturas)
        nome_do_menor = []
        nome_do_maior = []
        for n in range(len(nomes)):
          if alturas[n] == altura_menor:
            nome_do_menor.append(nomes[n])
          if alturas[n] == altura_maior:
            nome_do_maior.append(nomes[n]) 
        print(nome_do_menor, "é(são) o(s) usuário(s) mais baixo(s) do grupo com %.2f m de altura."%altura_menor)
        print(nome_do_maior,"é(são) o(s) usuário(s) mais alto(s) do grupo com %.2f m de altura."%altura_maior) 
        print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear') 
    elif opcao == "j":
      os.system('clear')
      if nomes == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      else:
        dados = sorted(zip(nomes, pesos, idades, alturas, sexos))
        for nome, peso, idade, altura, sexo in dados:        
          print("Nome:", nome, "| Peso:", peso, "Kg", "| Idade:", idade, "anos", "| Altura:", altura, "m", "| Sexo:", sexo)
          print()
          print()
          print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')
    elif opcao == "k":
      os.system('clear')
      if nomes == []:
        print("Ainda não existem dados cadastrados no sistema.")
        print()
      else:
        dadosK = sorted(zip(idades, nomes, pesos, alturas, sexos))
        for idade, nome, peso, altura, sexo in dadosK:        
          print("Idade:", idade, "anos", "| Nome:", nome, "| Peso:", peso, "Kg", "| Altura:", altura, "m", "| Sexo:", sexo)
          print()
          print()
          print()
      input("Digite qualquer tecla para voltar ao menu principal.")
      os.system('clear')    
    elif opcao == "l":
      print("Encerrando o programa...")
      print("Aguarde!")
      sleep(4)
      os.system('clear')
      break