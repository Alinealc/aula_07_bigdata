lista_numeros=[]

for n in range(5):
    num = input('Informe o número: ')
    lista_numeros.append (num) # adiciona 

  
print(lista_numeros[0])
lista_numeros[0] = 22
lista_numeros.pop() #pop deleta o último
print(lista_numeros)
