# script que defina la diferencia entre un número dado y 17 y que imprima el resultado


continuar = True

while continuar:
    num = float(
        input(
            "¿Podrías indicarme el número al que le vamos a sacar la diferencia de 17 "
        )
    )

    if num > 17:
        res = num - 17
        print("la diferencia entre tu numero", num, " y 17 es: ", res)

    elif num < 17:
        res = 17 - num
        print("la diferencia entre tu numero", num, " y 17 es: ", res)

    else:
        print("la diferencia entre tu numero", num, " y 17 es: 0")

    x = input("Deseas volver a realizar otra validación? s/n ")
    if x in ["No", "n", "NO", "no", "N"]:
        continuar = False
