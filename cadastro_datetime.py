from datetime import datetime
import random

cartoes = ['R$50,00', "R$250,00", "R$120,00"]

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
bonus = random.choices(cartoes)
data = datetime.now()
aniversário = datetime.now().strftime("%d/%m/%Y")
print (f"Olá {nome}, seu registro foi concluído com êxito na data {data.day}/{data.month}/{data.year} às {data.strftime('%H:%M')}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {bonus}")
