rm = int(input("Informe o RM: "))

soma = 0

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

digito = rm % 10
soma = soma + digito
rm = rm // 10

print("A soma é ", soma)