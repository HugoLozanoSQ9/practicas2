# escribe un script que calcule la suma de 3 números dados por el usuario
# si los valores son iguales deberá imprimir la suma dmultiplicada por 3

num1 = int(input('podrías darme el primer número '))
num2 = int(input('podrías darme el segundo número '))
num3 = int(input('podrías darme el tercer número '))

if num1 == num2 and num2 == num3: # tambien se puede if num1 == num2 == num3
    x = (num1 + num2 + num3)*3
    print('El resultado es: ', x)
else: 
    x = (num1 + num2 + num3)
    print('Tu resultado es: ', x)


###############################################################

# Si fuera función


def sum(num1, num2, num3):
    """suma 3 numeros

    Args:
        num1 (float): numero 1
        num2 (float): numero 2
        num3 (float): numero 3
    """
    if num1 == num2 and num2 == num3:
        return (num1 + num2 + num3) * 3
    return num1 + num2 + num3


print(sum(10, 10, 10))

###############################################################33

lista_de_numeros = []
for i in range(3):
    numero = int(input('Ingrese un número: '))
    lista_de_numeros.append(numero)

if lista_de_numeros[0] == lista_de_numeros [1] == lista_de_numeros [2]:
    suma = (lista_de_numeros[0] + lista_de_numeros[1]+ lista_de_numeros[2])*3
    print('La suma de los números *3 es:', suma)
else:
    suma = (lista_de_numeros[0] + lista_de_numeros[1]+ lista_de_numeros[2])
    print('La suma de los 3 números es:', suma)