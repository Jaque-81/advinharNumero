print(50 * "*")
print("Bem vindo ao jogo de Adivinhação!")
print(50 * "*")

numero_secreto = 42
total_tentativas = 3
rodada = 1

numero_secreto = 42
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas) :
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

acertou = numero_secreto == chute
chute_maior = numero_secreto > chute
chute_menor = numero_secreto < chute


if (acertou):
    print("Você acertou!")
else:
  if(chute_maior):
    print("Você errou! O chute foi maior que o número secreto.")
  elif(chute_menor):
    print("Você errou! O chute foi menor que o número secreto.")

print("Você errou")

print("Fim do jogo!")

