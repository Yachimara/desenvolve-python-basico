#Solicitação de dados
g=input("Digite seu genero (M ou F): ")
i=int(input("Digite sua idade: "))
t=int(input("Digite seu tempo de serviço: "))
#Processamento 
mulher=(g=="F")and((i>60)or(t>29)or((i>59) and (t>24)))
homen=(g=="M")and((i>65)or(t>29)or((i>59) and (t>24)))
#impressão
print(f"Você já pode se aposentar: {homen or mulher}")