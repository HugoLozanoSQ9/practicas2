#Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. 
#Luego, el programa debe calcular y mostrar la suma de los dígitos que componen el número
validador = True

while validador:
    
    numero = int(input('podrías darme un numero entero positivo para inicarte la suma de todos los digitos? '))
    if numero <= 0 :
        print('El numero que me diste no es positivo, podrías corroborar?')
    else:
        validador = False

contador = 0
for i in str(numero):

    contador = contador + int(i)

print('La suma de tus numeros es: ', contador)