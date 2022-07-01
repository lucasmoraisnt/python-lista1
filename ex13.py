avista = float(input("Informe o valor a vista: "))
parcela = float(input("Informe o valor da parcela: "))

aprazo = parcela * 10
porcentual = 1 - avista / aprazo

print("O valor do desconto foi de ", porcentual * 100)