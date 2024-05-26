#Entrada de dados
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))

#Inicialização dos dados
m= (n1+n2+n3)/3

#Processamento 
if m>=60:
    print("Aprovado")
    print("Fim")
elif m>=40:
    print("Recuperação")
    print("Fim")
else:
    print("Reprovado")
    print("fim")        