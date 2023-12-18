def val_sexo():
	sexo = input("Pode me falar seu sexo, por favor? (M/F) ").upper()
	while sexo not in ["M", "F"]:
		print()
		print("Opção inválida. Por favor, digite novamente.")
		print()
		sexo = input("Pode me falar seu sexo, por favor? (M/F) ").upper()
	return sexo	

print("Oi, seja bem-vindo(a) !")
print()
sexo = val_sexo()
alt = float(input("Digite sua altura em centímetros: "))
print()

if sexo == "M":
	peso_ideal_h = (alt - 100) - ((alt - 150) / 4)
	print("Seu peso ideal é:", peso_ideal_h, "Kg")
else:
	peso_ideal_m = (alt - 100) - ((alt - 150) / 2)
	print("Seu peso ideal é:", peso_ideal_m, "Kg")