print("Hola mundo desde python!!")

# VARIABLES EN PYTHON

# entero
Edad = 20

# decimal
Precio = 50.5

# texto
Nombre = "Helen Keilly"

# booleano
Bandera = True


# Mostrar datos
print("Nombre: ", Nombre)
print("Edad: ", Edad)
print("Precio: " + str(Precio))

# Entrada de datos
Nombre = input( "Introduce tu nombre: ")
print("Hola "+ Nombre)

# Suma de dos números ingresados (Los inputs siempre devuelven cadenas)
Num1 = input("Ingresa el primer número: ")
Num2 = input("Ingresa el segundo número: ")
Suma = Num1 + Num2
print("La suma es: ", Suma)
Suma = float(Num1) + float(Num2)
print("La suma es:", Suma)