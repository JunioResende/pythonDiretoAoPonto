import random

guess = random.randint(0, 5)
input("Me faça uma pergunta: ")

if guess== 0:
    print("Sim, com certeza!")
elif guess == 1:
    print("Parece bom!")
elif guess == 2:
    print("Melhor nao te dizer!")
elif guess == 3:
    print("Nao posso prever agora!")
elif guess == 4:
    print("Nao conte com isso")
elif guess == 5:
    print("Minhas fontes dizem nao!")
