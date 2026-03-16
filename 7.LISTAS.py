# LISTAS

frutas = ['Manzanas','Fresas','Naranjas','Peras','Maracuyás']
#Imprime toda la lista
print(frutas)
#Imprime solo el primer elemento de la lista
print(frutas[0])
#Sale error porqué no se encuentra en el rango de la lista
#print(frutas[5])
#Imprime el penúltimo elemento de la lista
print(frutas[-2])
#Imprime los elementos en ese rango (no se imprime el 3ero)
print(frutas[1:3])

#MÉTODOS DE LAS LISTAS
numeros = [1,2,3,4,5]

#Adiciona elemnto a la lista
numeros.append(6)
#Adiciona en esa posición el elemento
numeros.insert(0,-1)
numeros.insert(1,0)
#Eliminar elemento específico(en su primera posición
numeros.remove(1)
#Verificar si un elemento se encuentra en la lista (devuelve un valor booleano)
print(3 in numeros)
#Mostrar tamaño de la lista
print(len(numeros))
#Elimina todo el contenido de la lista
numeros.clear()
print(numeros)
