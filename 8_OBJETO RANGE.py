# OBJETO RANGE

#Crea como una secuencia inmutable de numeros (inicio,final,paso)
numeros = range(3)
#Podemos transformarle en lista
numeros = list(range(3))

#Iteración en range
for item in numeros:
    print(item)
#Iteración en secuencia especifica (del 5 al 9)
for item in range(5,10):
    print(item)
#Iteración sobre secuencia con saltos
for item in range(10,20,2):
    print(item)

print(numeros)
