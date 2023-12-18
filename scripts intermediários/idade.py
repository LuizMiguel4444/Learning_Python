import datetime
from calendar import isleap

def error():
	print("A data proposta não existe!")

print("= " * 17)
print("= = = = = = Programa: = = = = = =")
print("= = = = Qual é sua idade? = = = =")
print("= " * 17)
print()
print("Olá, seja bem vindo(a)!")
print()

dia = int(input("Digite o dia em que você nasceu: "))
mes = int(input("Digite o mês em que você nasceu: "))
ano = int(input("Digite o ano em que você nasceu: "))
dia_atual = datetime.datetime.today().day
mes_atual = datetime.datetime.today().month
ano_atual = datetime.datetime.today().year
print()

if mes == 1:
  if dia < 0 or dia >= 32:
    error()
elif mes == 2:
  if isleap(ano):
    if dia < 0 or dia >=30:    
      error()
  else:
    if dia < 0 or dia >=29:
      print("A data proposta não existe, pois Fevereiro só tem 28 dias nesse ano!")
elif mes == 3:
  if dia < 0 or dia >= 32:
    error()
elif mes == 4:
  if dia < 0 or dia >= 31:
    error()
elif mes == 5:
  if dia < 0 or dia >= 32:
    error()
elif mes == 6:
  if dia < 0 or dia >= 31:
    error()
elif mes == 7:
  if dia < 0 or dia >= 32:
    error()
elif mes == 8:
  if dia < 0 or dia >= 32:
    error()
elif mes == 9:
  if dia < 0 or dia >= 31:
    error()
elif mes == 10:
  if dia < 0 or dia >= 32:
    error()
elif mes == 11:
  if dia < 0 or dia >= 31:
    error()
elif mes == 12:
  if dia < 0 or dia >= 32: 
    error()
elif mes > 12:
	error()
  
if dia <= 0 or dia > 31:
  print("Pois o dia digitado não existe!")
if mes <= 0 or mes > 12:
  print("Pois o mês digitado não existe!")
if ano < 0:
  print("Pois o ano digitado não existe!")

# # # # # # # # # # # FEZ ANIVERSÁRIO # # # # # # # # # # #
if dia < 0 or dia >=29 or dia <= 0 or dia > 31 or mes <= 0 or mes > 12 or ano < 0:
	error()
else:	
	if dia_atual >= dia and mes_atual > mes:
	  idade1 = ano_atual - ano
	  print("Você tem %d anos e já fez aniversário em %d" %(idade1, ano_atual))
	
	elif ano > ano_atual:
	  print("Essa pessoa não nasceu ainda!")
	
	elif dia_atual < dia and mes_atual > mes:
	  idade1 = ano_atual - ano
	  print("Você tem %d anos e já fez aniversário em %d" %(idade1, ano_atual))
	
	elif dia_atual > dia and mes_atual == mes:
	  idade1 = ano_atual - ano
	  print("Você tem %d anos e já fez aniversário em %d" %(idade1, ano_atual))
	
	elif dia_atual == dia and mes_atual == mes and ano_atual == ano:
	  idade1 = ano_atual - ano
	  print("Você nasceu hoje. Parabéns!")
	
	elif dia_atual == dia and mes_atual == mes:
	  idade1 = ano_atual - ano
	  print("Você está fazendo %d anos hoje. Parabéns!" % idade1)

# # # # # # # # # # NÃO FEZ ANIVERSÁRIO # # # # # # # # # #

	elif dia_atual >= dia and mes_atual < mes:
	  idade2 = (ano_atual - ano) - 1
	  print("Você tem %d anos e ainda não fez aniversário em %d" %(idade2, ano_atual))
	
	elif dia_atual < dia and mes_atual < mes:
	  idade2 = (ano_atual - ano) - 1
	  print("Você tem %d anos e ainda não fez aniversário em %d" %(idade2, ano_atual))
	
	elif dia_atual < dia and mes_atual == mes:
	  idade2 = (ano_atual - ano) - 1
	  print("Você tem %d anos e ainda não fez aniversário em %d" %(idade2, ano_atual))

print()
print("= " * 17)
print("= = = = Fim do programa!! = = = =")
print("= " * 17)