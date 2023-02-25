#if comum
print("if comum")
umidade = int(input("Digite o valor da umidade "))
umidadeMedia = 50


if umidade >= umidadeMedia:
    print("Umido")
else:
    print("Seco")

print("*****************************************")

#Com operador ternario
print("Com operador ternario")
umidade = int(input("Digite o valor da umidade "))
umidadeMedia = 50

print("Umido") if umidade >= umidadeMedia else print("Seco")