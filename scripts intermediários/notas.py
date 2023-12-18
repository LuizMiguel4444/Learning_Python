soma = 0
i = 1
n = int(input("Quantas notas deseja inserir para o cálculo da média? "))
m = int(input("Qual é a nota média geral da instituição? "))
print()
while i <= n:
 nota = float(input("Informe a %d° nota: "%i))
 soma = soma + nota
 i = i + 1
media = soma / n
print()
print("Sua média geral foi: %.1f"%media)
if media >= m:
 print("Parabéns! Você foi aprovado!")
else:
 print("Infelizmente, você foi reprovado!")
print()  
print("Fim do Programa")