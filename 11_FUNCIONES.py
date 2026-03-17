# FUNCIONES -> Son bloques de código que realiza una tarea específica y que son reutilizables

#Función sin parámetros ni devolución de valor
def Saludar():
    print('Hola, bienvenidos al curso de Python')

#Llamada a la función sin parámetros
Saludar()
Saludar()

#Función con parámetros
def saludo(nombre):
    print('Hola '+nombre+' bienvenido a clases')

#Llamada a la función con parámetro
saludo('Helen Keilly')
saludo('Limber')

#Función que devuelve valor
def suma(a,b):
    return a+b

#Llamada a la función que devuelve valor
resultado = suma(10,4)
print("La suma es: ",resultado)

#Establecer valores por defecto para los parámetros de una función (mostrará "Estudiante" cuando no se envíe valor)
def bienvenida(nombre='Estudiante'):
    print("Bienvenido, ",nombre)

bienvenida()
bienvenida("Susana")

#Función con argumentos variables
def sumador(*args):
    return sum(args)

print(sumador(1,2,3,4,5))
print(sumador(4,5,6))
