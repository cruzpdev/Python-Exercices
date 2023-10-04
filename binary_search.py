class BuscaBinaria():

    def iteracao(self, list, item):
        # minimo e maximo acompanham em que parte da lista procurar
        minimo = 0
        maximo = len(list) -1
        
        #enquanto não tiver afunilado até um elemento...
        while minimo <= maximo:
            #...cheque o elemento do meio.
            media = (minimo + maximo)//2
            chute = list[media]
            # ao achar elemento:
            if chute == item:
                return chute
            # se o chute foi alto demais:
            if chute > item:
                maximo = media - 1
            # se o chute foi baixo demais:
            else:
                minimo = media + 1

        # o item não existe:
        return None
    
    def recursao(self, list, minimo, maximo, item):
        #cheque padrão
        if maximo > minimo:

            media = (maximo + minimo)//2
            chute = list[media]

            #se foi um chute certeiro:
            if chute == item:
                return media
            
            # caso o elemento seja menor que a media, ele tem que estar na parte esquerda da array
            elif chute > item:
                return self.recursao(list, minimo, media -1, item)
            
            # senão só pode estar na parte direita da array. 
            else:
                return self.recursao(list, media +1, maximo, item)

        else:
        # elemento não está presente na array
            return None
        
if __name__ == "__main__":
#temos que iniciar a classe para usar os metodos dessa classe
 
 bb = BuscaBinaria()

 lista = [1,3,5,7,9]

print (bb.iteracao(lista,3)) #1
pass
print (bb.iteracao(lista, -1)) #None
