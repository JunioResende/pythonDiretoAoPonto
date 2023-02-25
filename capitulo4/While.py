x = 0

while x < 10:
    print(x)
    x = x + 1

# Loop infinito e break
capital = "Ottawa"
while True:
    resposta = input("Qual a capital do canada? ")
    if resposta == capital:
        print("Certa resposta!")
        break
    else:
        print("Resposta incorreta. Tente Novamente!")

# Continue
while True:
    username = input("username? ")
    if username != "neo":
        print("Nunca nem vi")
        continue
    senha = input("Qual a senha? ")
    if senha == "1234":
        print("Bem vindo, {}".format(username))
        print("Aceita um cafe")
        break
