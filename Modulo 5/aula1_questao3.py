#Blibioteca
import random

#Inicialização de dados
aux=10000

#Gerando numero
n=random.randint(1,10)



#Processamento
for i in range(aux):
    p=int(input("Digite seu palpite (1 a 10)"))
    if p==n:
        print("Correto")
        break
    elif p<n:
        print("muito baixo")
    elif p>n:
        print("muito alto")