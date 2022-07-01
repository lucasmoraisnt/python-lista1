salarioAnt = float(input("Salario antes do aumento: "))
salarioAtual = float(input("Salario depois do aumento: "))

porcentual = salarioAtual / salarioAnt - 1

print("O aumento foi de ", porcentual * 100)