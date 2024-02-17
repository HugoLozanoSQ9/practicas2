""" 
#forma correcta

letter = input('Dame una letra:')
vocals = ['a','e','i','o','u','A','E','I','O','U']
if letter in vocals:
    print('Tu letra', letter, 'Es vocal')
else:
    print('Tu letra',letter,' no es vocal')
"""
def is_vocal(letter):
    """ Funcion para saber si la letra dada por el usuario es vocal 

    Args:
        letter (str): Debe ser una letra
    """

    vowell = ['a','e','i','o','u','A','E','I','O','U']
    return letter in vowell

print(is_vocal('a'))
print(is_vocal('e'))
print(is_vocal('d'))
print(is_vocal('b'))

