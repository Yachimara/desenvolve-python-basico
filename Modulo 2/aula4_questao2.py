#Entrada de graus em Fahrenheit
f = int(input("Digite a temperatura em Fahrenheit: "))
#Conversão em graus Celsius
c = (f-32)*(5/9)
#Conversão Celsius para inteiro
c =int(c)
#impressão
print(f"{f} graus Fahrenheit são {c} graus Celsius." )