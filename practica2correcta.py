number = float(input("Dame un número: "))
if number < 17:
    resultado = 17 - number
else:
    resultado = (number - 17) * 2
print("El resultado es: ", resultado)

#Si desearia hacerla función se hace lo siguiente: 

def dif_func(number):
    if number < 17:
        return 17 - number
 #se elimina el else por que solo hay 2 opciones
    return (number - 17) * 2
    

print(dif_func(20))
print(dif_func(17))
print(dif_func(12))