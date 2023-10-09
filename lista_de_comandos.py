if __name__ == '__main__':
    l = []  # LISTA
    N = int(input()) # QUANTIDADE DE COMANDOS
    for i in range(N):
        command, *args = input().split() #LÊ O INPUT E SEPARA O COMANDO DOS ARGUMENTOS
        if command == 'print':
            print(l)
        else:
            getattr(l, command)(*map(int, args)) #getattr: obtem o atributo do objeto, no caso, o comando na lista 'l'. isso permite chamar o comando como uma função com base no input
            #*map(int, args) = converte os argumentos para inteiros e os passa como argumentos para a função    
