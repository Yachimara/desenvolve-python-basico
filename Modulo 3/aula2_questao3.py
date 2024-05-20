#solicitação de dados
i=int(input("Digite sua idade: "))
n=int(input("Quantos jogos você já jogou? "))
v=int(input("Em quantas partidas você venceu? "))
  
#Processamento de condicionantes
print(f"Apto para ingressar no clube de jogos de tabuleiro:{(i>15)and(i<19)and(n>2)and(v>0)}")