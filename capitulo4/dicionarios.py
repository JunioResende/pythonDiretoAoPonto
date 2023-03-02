cliente = {"nome": "Junio", "idade": 32, "sexo": "masculino"}

print(cliente["nome"])

print("**********************************************************")

skills = {"sabedoria": 8, "coragem": 7, "força": 9}

for sk in skills:
    print(sk)

print("**********************************************************")

for sk, values in skills.items():
    print(sk, values)

print("**********************************************************")