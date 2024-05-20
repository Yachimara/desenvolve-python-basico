#Entrada de dados dos Produtos
Pd1 = (input("Digite o nome do produto 1: "))
v1 = float(input("Digite o preço unitário do produto 1: "))
q1 = int(input("Digite a quantidade do produto1: "))
Pd2 = (input("Digite o nome do produto 2: "))
v2 = float(input("Digite o preço unitário do produto 2: "))
q2 = int(input("Digite a quantidade do produto2: "))
Pd3 = (input("Digite o nome do produto 3: "))
v3 = float(input("Digite o preço unitário do produto 3: "))
q3 = int(input("Digite a quantidade do produto3: "))  

#Processamento das entradas
t=(v1*q1)+(v2*q2)+(v3*q3)

#Impressão
print(f"Total: R$ {t:,.2f}")