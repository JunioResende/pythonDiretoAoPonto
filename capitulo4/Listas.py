planetas = ["Mercurio", "Venus", "Jupiter"] #Listagem dos planetas.

print("Listagem Original")
print(planetas[0]) #seleciona o intice 0 da lista, onde esta localizado o planeta mercurio
print(planetas[1]) #seleciona o intice 1 da lista, onde esta localizado o planeta Venus
print(planetas[2]) #seleciona o intice 2 da lista, onde esta localizado o planeta Jupiter

print("**************************************************************************************")

print("Adicionando o planeta Terra")
planetas[1] = "Terra"
print(planetas)

print("**************************************************************************************")

print("Exibindo os valores apos a atualizacao ")
print(planetas[0]) #seleciona o intice 0 da lista, onde esta localizado o planeta mercurio
print(planetas[1]) #seleciona o intice 1 da lista, onde esta localizado o planeta Terra
print(planetas[2]) #seleciona o intice 2 da lista, onde esta localizado o planeta Jupiter
