#Entrada de dados
n=int(input("Digite seu número: "))

#Inicialização
maior = 0

#Processamento interativo
while n>0:
    x=int(input("Digite seu número: "))
    if x>maior:
        maior=x
        n=n-1
    else:
        n=n-1
print(maior)
