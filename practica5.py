#como se determina si una letra es vocal o no 

continuar = True

while continuar:
    letra = input('Podrías por favor ingresar la letra a revisar? ') 
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('Tu letra', letra, 'Es vocal')
    elif letra == '':
        continuar = False
    else:
        print('Tu letra',letra,' no es vocal')

