#Blibliotecas:
import random, math

#Inicialização de dados:
r=0

#Entrada de dados:
n=int(input("Insira a quantidade de valores a serem geradas: "))

#Processamento:
for i in range(n):
    aux=(random.randint(0,100))
    r=r+aux
    print(aux,r)
f=math.sqrt(r)
print(f)




