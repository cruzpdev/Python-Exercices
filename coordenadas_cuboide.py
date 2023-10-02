x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Lista de compreensão para gerar as coordenadas
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# Filtrar as coordenadas onde a soma não é igual a n
filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

# Imprimir a lista filtrada em ordem lexicográfica crescente
print(sorted(filtered_coordinates))
