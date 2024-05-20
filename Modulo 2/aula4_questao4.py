#Entrada de dados
Valor = int(input("Digite um valor em dinheiro (não digite centavos)"))

#Processamento

n100 = Valor//100
sobra = Valor%100
n50 = sobra//50
sobra %=50
n20 = sobra//20
sobra %=20
n10 = sobra//10
sobra %=10
n5 = sobra//5
sobra %= 5
n2 = sobra//2
sobra %=2
n1 = sobra//1
print(f"{n100} nota(s) de R$100,00")
print(f"{n50} nota(s) de R$50,00")
print(f"{n20} nota(s) de R$20,00")
print(f"{n10} nota(s) de R$10,00")
print(f"{n5} nota(s) de R$5,00")
print(f"{n2} nota(s) de R$2,00")
print(f"{n1} nota(s) de R$1,00")