dist = float(input("Digite a distância que você percorreu em quilômetros: "))
tempo1 = float(input("Digite quantas horas o seu percurso durou (sem minutos): "))
tempo2 = float(input("Digite quantos minutos o seu percurso durou (sem horas): "))


if tempo1 == 0:
  tempo = tempo2

if tempo2 == 0:
  tempo = tempo1

if tempo2 > 0:
  tempo = tempo1 + (tempo2 / 60)

vel1 = dist / tempo
vel2 = vel1 / 3.6

print()
print("Sua velocidade média foi de: %.2f Km/h"%vel1 , "ou %.2f m/s"%vel2 ) 