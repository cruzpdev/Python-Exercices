def solution(s):
    if len(s) % 2 != 0:     # Se o comprimento da string for ímpar, adicionamos um underscore no final
        s += "_"
    return [s[i:i+2] for i in range(0,len(s),2)] 
#para os indices na posição de 0 até o final da string -1, no incremento 2, SLICE a string, de i até i+2(exclusivo) 