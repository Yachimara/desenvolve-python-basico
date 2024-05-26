#Entrada de dados
N=int(input("Digite o número de experimentos: "))

#Inicialização de dados
s=0
r=0
c=0
cont=0
total=0

#Processamento
while cont<N:
    quantia=int(input("Digite a quantidade de cobaias : "))
    e=input("Digite o tipo: ")
    if e=="c":
        c=c+quantia
    elif e=="r":
        r=r+quantia
    elif e=="s":
        s=s+quantia
    cont=cont+1
    total=total+quantia

print(f"Total: {total}") 
print(f"Total de coelhos: {c}")
print(f"Total de sapos: {s}")
print(f"Total de ratos: {r}")
print(f"Percentual de coelhos: {c/total} %")
print(f"Percentual de sapos: {s/total} %")
print(f"Percentual de ratos: {r/total} %")