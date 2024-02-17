lista_nombres=[]

continuar1 = True

while continuar1:
    nombre1 = input('Podrías por favor ingresar el nombre a enlistar? ') 
    if nombre1 == '':
        continuar1 = False
    else:
        lista_nombres.append(nombre1)

set_nombres = set(lista_nombres) #se crea un set para que muestre una sola vez los nombres

for nombre in set_nombres: #se genera un bucle que tenga todos los nombres
    conteo=lista_nombres.count(nombre) #vamos a contar cuantas veces se tiene el nombre dentro de la lista de nombres
    if conteo > 1: #si el conteo es mayor a uno (para demostrar que se repite)
        print('El nombre', nombre,'se repite',conteo,'veces') #muestra en pantalla cuantas veces se repitió