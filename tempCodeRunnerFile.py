lista_numeros=[]

for n in range(5):
    num = input('Informe o número: ')
    lista_numeros.append (num) # adiciona 

  
print(lista_numeros[0])
lista_numeros[0] = 22 #altera a índice 0
lista_numeros.pop() #pop deleta o último
lista_numeros.pop(-2) #pop deleta o penúltimo
lista_numeros.remove (30) # deleta o determinado valor / indice específico 
del lista_numeros[0]
print(lista_numeros)