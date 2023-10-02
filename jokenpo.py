import random

playerwins = 0
pcwins = 0
empate = 0

print("\n...PEDRA...")
print("...PAPEL...")
print("...TESOURA...\n")

qtd_jogos = int(input("Melhor de quantas? "))

while playerwins < qtd_jogos and pcwins < qtd_jogos:
    print("\nCaso queira sair da aplicação escreva 'quit' ou 'q'")
    print (f"- SEU SCORE: {playerwins} - SCORE PC: {pcwins} - EMPATES: {empate} -\n")

    p1 = input("Escolha sua opção: ").lower()
    if p1 == "quit" or p1 == "q":
        break
    p2 = random.randint(0,2)

    if p2 == 0:
        p2 = "pedra"
    elif p2 == 1:
        p2 = "papel"
    else:
        p2 = "tesoura"

    if p1 == p2:
        print (f"\nO bot escolheu {p2}! EMPATEEE\n")
        empate += 1
    elif p1 == "tesoura":
        if p2 == "papel":
            print(f"\nO bot escolheu {p2}! Você venceu!\n")
            playerwins += 1
        elif p2 == "pedra":
            print(f"\nO bot escolheu {p2}! Você perdeu!\n")
            pcwins += 1        
    elif p1 == "papel":
        if p2 == "pedra":
            print(f"\nO bot escolheu {p2}! Você venceu!\n")
            playerwins += 1
        elif p2 == "tesoura":
            print(f"\nO bot escolheu {p2}! Você perdeu!\n")
            pcwins += 1                        
    elif p1 == "pedra":
        if p2 == "tesoura":
            print(f"\nO bot escolheu {p2}! Você venceu!\n")
            playerwins += 1
        elif p2 == "papel":
            print(f"\nO bot escolheu {p2}! Você perdeu!\n")
            pcwins += 1            
    else:
        print("\nEscreva 'pedra', 'papel' ou 'tesoura'.\n")

if playerwins == pcwins:
    print ("FIM DE JOGO! EMPATE!")
elif playerwins > pcwins:
    print("FIM DE JOGO! PARABÉNS! VOCÊ GANHOU!")
else:
    print("FIM DE JOGO! HAHA! VOCÊ PERDEU!")