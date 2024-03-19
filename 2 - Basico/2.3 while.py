import random

numero_sorteado = random.randint(1,100)

chute = 0
print("Jogo de adivinhacao - advinhe um numero entre 1 e 100")

while numero_sorteado != chute:
    chute = int(input("Advinhe o numero: "))

    if chute < numero_sorteado:
        print("Seu numero menor, tente nov")
    elif chute > numero_sorteado:
        print("Seu numero é maior, tente nov")
    else:
        print("PArabéns! vocÊ acertou o número: " + str(chute))
        break
