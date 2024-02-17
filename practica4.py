#Escript que calcule cuantas veces se repite un nombre en una lista de nombres determinada por el usuario

nombres = []

continuar = True

while continuar:
    nombre1 = input('Podrías por favor ingresar el nombre a enlistar? ') 
    if nombre1 == '':
        continuar = False
    else:
        nombres.append(nombre1)
 
consulta = input('Podrías por favor indicarme ¿Qué nombre quieres corroborar si se encuentra dentro de la lista?')

repeticiones = nombres.count(consulta) #count sirve para contar cuantos elementos se tiene (consulta) en la lista
#De forma general .count sirve para contar cuantas veces se repite un elemento en una lista (este elemento puede darlo el usuario o ser estático)


if repeticiones > 1:
    print('El nombre', consulta, 'si se encuentra en la lista y se repite:', repeticiones, 'veces') 
else:
    print('El nombre', consulta, 'no se encuentra en la lista') 

####################################################################3
lista_nombres=[]

continuar1 = True

while continuar1:
    nombre1 = input('Podrías por favor ingresar el nombre a enlistar? ') 
    if nombre1 == '':
        continuar1 = False
    else:
        lista_nombres.append(nombre1)

set_nombres = set(lista_nombres)

for nombre in set_nombres:
    conteo=lista_nombres.count(nombre)
    if conteo > 1:
        print('El nombre', nombre,'se repite',conteo,'veces')