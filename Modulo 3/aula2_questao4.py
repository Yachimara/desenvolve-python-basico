#Solicitação de dados
cl=input("Digite a classe da personagem (guerreiro, mago ou arqueiro: ")
f=int(input("Digite os pontos de força: "))
m=int(input("Digite os pontos de magia: "))
#Processamento
guerreiro=(cl=="guerreiro")and(f>14)and(m<11)
mago=(cl=="mago")and(f<11)and(m>14)
arqueiro=(cl=="arqueiro")and((f and m)>5)and((f and m)<15)
#Impressão
print(f"Pontos de atributo consistentes com a classe escolhida: {guerreiro or mago or arqueiro}")