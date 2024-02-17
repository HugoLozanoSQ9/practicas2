"""
Escribe un script que le pregunte al usuario varios nombres hasta que el usuario especifique que ya no desea ingresar más
Cómo resultado deberá mostrar al usuario una lista, una tupla y un set con todos los nombres que ingresó el usuario 
"""

# Se puede ocupar break --> esta palabra reservada rompe el bucle padre (se puede ocupar para romper el while)

names = []

while True:

    name = input("Ingresa un nombre: ")

    if name in "":
        break
    names.append(name)

print(names)
print(tuple(names))
print(set(names))
