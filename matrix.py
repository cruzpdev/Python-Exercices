def imprimir_matriz_binaria(linha, coluna):
    for i in range(coluna):
        for j in range(linha):
            print((i + j) % 2, end=' ')
        print()

linha = int(input("Defina o número de caracteres por linha: "))
coluna = int(input("Defina a quantidade total de caracteres: "))
imprimir_matriz_binaria(linha, coluna)