def quicksort(array):
    if len(array) < 2:
        #caso-base. arrays com 0 ou 1 elementos já estão classificadas.
        return array
    else:
        #caso recursivo
        pivo = array[0]
        #todos os elementos menores que pivo vão para esq
        esq = [i for i in array[1:] if i<= pivo]
        #todos os elemenots maiores que o pivo vao para dir
        dir = [i for i in array[1:] if i > pivo]
        return quicksort(esq) + [pivo] + quicksort(dir)

print (quicksort([171, 69, 666, 42]))        
        
