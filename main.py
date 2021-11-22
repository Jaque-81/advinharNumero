'''print(50 * "*")
print("Bem vindo ao jogo de Adivinhação!")
print(50 * "*")

numero_secreto = 42 #snake_case
chute = input(int("Digite seu número: ")
print("Você digitou ", chute)

if (numero_secreto == chute):
  print("Você acertou!")
else:
  print("Você errou")

print("Fim do jogo!")

Não importa o número digitado, a comparação com == envolvendo tipos diferentes resultará em falso. Isso porque a função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o numero_secreto, seja possível. Realizamos essa conversão através da função int.'''

print(50 * "*")
print("Bem vindo ao jogo de Adivinhação!")
print(50 * "*")

numero_secreto = 42
chute_str = input("Digite seu número: ")
chute = int(chute_str)
acertou = numero_secreto == chute
chute_maior = numero_secreto > chute
chute_menor = numero_secreto < chute

print("Você digitou ", chute)

if (acertou):
    print("Você acertou!")
else:
  if(chute_maior):
    print("Você errou! O chute foi maior que o número secreto.")
  elif(chute_menor):
    print("Você errou! O chute foi menor que o número secreto.")

print("Você errou")

print("Fim do jogo!")
