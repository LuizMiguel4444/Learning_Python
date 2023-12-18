print("=" * 36)
print("======== Calculadora de IMC ========")
print("=" * 36)
print()

peso = float(input("Digite seu peso corporal em quilogramas: "))
alt = float(input("Digite sua altura em metros: "))

imc = peso / alt**2

print()
print("Seu IMC é: %.1f"%imc)

if imc <= 18.5:
  print("Você está abaixo do peso ideal !")

elif imc >= 18.6 and imc <= 24.999:
  print("Você está saudável !")

elif imc >= 25 and imc <= 29.999:
  print("Você está com sobrepeso !")

elif imc >= 30 and imc <= 34.999:
  print("Você está com obesidade de grau I !!!")

elif imc >= 35 and imc <= 39.999:
  print("Você está com obesidade de grau II !!!")

else:
  print("Você está com obesidade de grau III !!!")