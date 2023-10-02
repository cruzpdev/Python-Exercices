print("Qual a sua idade?")
idade = input()
if idade:
    idade = int(idade)
    if idade >= 21:
        print ("Entrada normal.")
    elif idade >= 18:
        print ("Use a pulseira.")
    else:
        print ("DE MENOR")
else:
    print ("Por favor digite sua idade correta.")