# Manejo de texto
curso = "python para iniciantes"

print(curso.upper())       # mayúsculas
print(curso)               # texto original
print(curso.lower())       # minúsculas
print(curso.capitalize())  # primera letra mayúscula


# Búsqueda en texto
print(curso.find("h"))
print(curso.find("cia"))


# Reemplazar texto
print(curso.replace("para", "FOR"))
print(curso)


# Verificar si una palabra existe
print("for" in curso) 
print("para" in curso)
print("PARA" in curso)
