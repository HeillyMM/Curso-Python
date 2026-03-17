# DICCIONARIO -> Almacena pares de clave-valor

mi_diccionario = {'nombre':'Bruno Diaz','edad':25,'Ciudad':'La Paz'}

#Imprimir todo el diccionario
print(mi_diccionario)
#Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['Ciudad'])
#Agregar un elemento
mi_diccionario['profesion'] = 'Ingeniero'
#Eliminar elemento
del mi_diccionario['Ciudad']
print(mi_diccionario)
#Obtener las claves del diccionario
print(mi_diccionario.keys())
#Obtener los valores del diccionario
print(mi_diccionario.values())
#Verificar si una clave existe
if 'edad' in mi_diccionario:
    print('Clave encontrada')
if 'ciudad' in mi_diccionario:
    print('Clave encontrada')
#Recorrido de un diccionario
for clave,valor in mi_diccionario.items():
    print('clave: ',clave,' valor: ',valor)
