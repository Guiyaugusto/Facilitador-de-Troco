print("Virgulas ou pontos nao sao necessarios. Os ultimos 2 algarismos sao obrigatoriamente centavos. Exemplo:\n1234 sao equivalentes a 12 reais e 34 centavos.")
Valor_conta = int(input("Valor da conta: "))
Valor_recebido = int(input("Valor dado pelo clinte: "))
Valor_troca = Valor_conta - Valor_recebido
if Valor_troca<= 0:
	print("Troco nao necessario!")
else:

	resp0=Valor_troca
	resto0=Valor_troca 

	resp1 = resp0 //10000
	resto1 = resto0 % 10000
	print(resp1 , "nota(s) de 100,00.")

	resp2 = resto1 //5000
	resto2 = resto1 % 5000
	print(resp2 , "nota(s) de 50,00.")

	resp3 = resto2 // 2000
	resto3 = resto2 % 2000
	print(resp3 , "nota(s) de 20,00.")

	resp4 = resto3 //1000
	resto4 = resto3 % 1000
	print(resp4 , "nota(s) de 10,00.")

	resp5 = resto4 //500
	resto5 = resto4 % 500
	print(resp5 , "nota(s) de 5,00.")

	resp6 = resto5 //200
	resto6 = resto5 % 200
	print(resp6 , "nota(s) de 2,00.")

	resp7 = resto6 // 100
	resto7 = resto6 % 100
	print(resp7 , "moeda(s) de 1,00.")

	resp8 = resto7 // 50
	resto8 = resto7 % 50
	print(resp8 , "moeda(s) de 0,50.")

	resp9 = resto8 // 25
	resto9 = resto8 % 25
	print(resp9 , "moeda(s) de 0,25.")

	resp10 = resto9 // 10
	resto10 = resto9 % 10
	print(resp10 , "moeda(s) de 0,10.")

	resp11 = resto10 // 5
	resto11 = resto10 % 5
	print(resp11 , "moeda(s) de 0,05.")


















