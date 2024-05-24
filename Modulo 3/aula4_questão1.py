#Entrada de dados
n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))

#Processamento
r=(n1+n2)%2

#impressão
if r > 0:
    print("impar")
else: # not r>0
    print("par")