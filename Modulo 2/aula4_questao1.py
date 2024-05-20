#Entrada do comprimento do terreno
comprimento = int(input("Digite comprimento do terreno: "))
#Entrada da largura do terreno
largura = int(input("Digite largura do terreno: "))
#Entrada valor do terreno
valor = float(input("Digite valor do terreno: "))
#Calculo da area
area = comprimento*largura
#Calculo do preço
preço = area*valor
# Impressão de resultados
print(f"O terreno possui {area}m² e custa R${preço:,.2f}")