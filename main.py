print(50 * "*")
print("Bem vindo ao jogo de Adivinhação!")
print(50 * "*")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
  print("Tentativa ", rodada," de ",total_tentativas)
  chute_str = input("Digite seu número: ")
  print("Você digitou: ", chute_str)
  chute = int(chute_str)
  rodada = rodada + 1

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

