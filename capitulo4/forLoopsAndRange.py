"""O for e a estrutura de repeticao mais popular do python, o motivo disso e que ele e muito conveniene para percorrer
os objetos iteraveis, como as listas. Vejamos como contar de 0 a 5 com o for.
"""

for i in range(6):  # O range faz a contagem iniciando pelo 0 []
    print(i)

print("********************************************************")

"""
O range ainda aceita a definição de um valor inicial, um valor final e
um valor passo. Por exemplo, para imprimir os números ímpares de 1 a
14, temos.

"""

for x in range(1, 15, 2): #1 e por onde comeca a contagem. 15 e onde termina a contagem. E o 2 pula uma casa
    print(x)


print("********************************************************")

planetas = ["Mercurio", "Venus", "Terra", "Marte", "Jupiter", "Saturno", "Urano", "Netuno"]
for planeta in planetas:
    print(planeta)


print("********************************************************")

#Adicionando plutao a lista
print("Adicionando plutao a lista")
planetas.append("Plutao")

for planeta in planetas:
    print(planeta)


print("********************************************************")