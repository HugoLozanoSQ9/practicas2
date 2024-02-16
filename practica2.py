#Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. 
#Luego, el programa debe contar y mostrar la cantidad de dígitos que contiene el número ingresado

validador = True

while validador:
    
    numero = int(input('podrías darme un numero entero positivo para inicarte cuantos digitos tiene por favor? '))
    if numero <= 0 :
        print('El numero que me diste no es positivo, podrías corroborar?')
    else:
        validador = False

contador = 0 

for i in str(numero):
    contador +=1


print('El numero de dígitos en tu número es: ', contador)
   



