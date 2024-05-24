#Entrada de dados
n=int(input("Digite o número de entrevistas: "))

#Inicialização de dados
cont=0
media=0

#Processamento Interativo
while cont<n:
    x=int(input("Digite a idade do entrevistado: "))
    cont=cont+1
    media=media+x
print(f"A idade média é: {media/n}")