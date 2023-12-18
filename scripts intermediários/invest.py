from PySimpleGUI import PySimpleGUI as sg
from math import log

sg.theme("Reddit")

layout = [
    [sg.Text("Quanto você deseja investir por mês? R$"), sg.Input(key="valor", size=(49,1))],
    [sg.Text("Quanto você quer possuir no final? R$"), sg.Input(key="mont", size=(51,1))],
    [sg.Text("Qual a taxa de juros mensal? (%)"), sg.Input(key="taxa", size=(55,1))],
	[sg.Button("Calcular")],
    [sg.Text("", key="Resultado")]
]

janela = sg.Window("PyInvest", layout=layout)

while True:
	eventos, valores = janela.read()
	if eventos == sg.WINDOW_CLOSED:
		break
	if eventos == "Calcular":
		try:
			i = float(valores["taxa"].replace(",",".")) / 100
			meses = log((float(valores["mont"].replace(",","."))) / float(valores["valor"].replace(",","."))) / log(1 + i)
			anos = meses / 12
		
			janela["Resultado"].update("Você precisará esperar %.0f meses ou aproximadamente %.2f anos para obter o montante desejado."%(meses, anos))

		except:
			sg.popup("Preencha todos os campos com números diferentes de zero!")