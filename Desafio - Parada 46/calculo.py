def calculo(numero):
    return numero ** 2

entrada = float(input("Digite um número: "))

resultado = calculo(entrada)

print(f"O número escolhido ({entrada}) elevado ao quadrado é: {resultado:.2f}.")