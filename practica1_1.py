"""
Escribe un script que le pregunte al usuario varios nombres hasta que el usuario especifique que ya no desea ingresar más
Cómo resultado deberá mostrar al usuario una lista, una tupla y un set con todos los nombres que ingresó el usuario 
"""

continues = True

names=[]

while continues:
    add = input('Deseas agregar nombres? s/n: ')
    if add in ['si','SI','s','sI','Si','S']:
        name= input('ingresa el nombre que deseas agregar a la lista: ')
        names.append(name)
    elif add in ['No', 'no','nO','NO','n','N']:
        continues = False
    else: 
        print('Perdona pero no entendí tu desición escribe s/n ')


print('lista: ',names)
print(tuple('tupla',names))
print('set',set(names))