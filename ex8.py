preco = float(input("Qual o valor do produto: "))
desconto = float(input("Qual o valor do desconto: "))

valorDesconto = preco * desconto /100

precoComDesconto = preco - valorDesconto

print("Valor do desconto: ", valorDesconto)
print("Novo preco: ", precoComDesconto)