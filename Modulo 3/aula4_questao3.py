#Entrada de dados
a=int(input("Digite o ano com 4 digitos(Ex: 1986): "))

#Processamento
if (a%4==0 and a%100!=0) or (a%400==0):
    print("Bissexto")
else:
    print("Não é bissexto")