import os

nome = input("Digite seu primeiro nome: ")
while nome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  nome = input("Digite seu primeiro nome: ")
os.system('clear')
snome = input("Digite seu segundo nome: ")
while snome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  snome = input("Digite seu segundo nome: ")
os.system('clear')
email = input("Digite seu email: ")
while True:
  if email.count("@") == 1 and email.count(".") >= 1:
    arroba = email.index("@")
    ponto = email.index(".")
    if arroba > 0 and arroba < len(email) - 1 and ponto > (arroba + 1) and len(email) - ponto >= 3:
      os.system('clear')
      break
    else:
      print("O e-mail é inválido. Por favor, digite novamente.")
      print()
      email = input("Digite seu email: ")
    os.system('clear')  
  else:
    print("O e-mail é inválido. Por favor, digite novamente.")
    print()
    email = input("Digite seu email: ")
  os.system('clear')  
print("Seu nome é: %s %s"%(nome, snome))
print("Seu email é:", email)