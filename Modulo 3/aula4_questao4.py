#Entrada de dados
d=float(input("Digite a distancia em km: "))
p=float(input("Digite o peso em Kg: "))

#processamento
if p>9:
    t=10
else:
    t=0

#Impressão
if d<101:
    print(f"R$ {(1*p)+t}")
if d>100 and d<301:
    print(f"R$ {(1.5*p)+t}")
if d>299:
    print(f"R$ {(2*p)+t}")    
