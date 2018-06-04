import string

# Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 que consista
# de las dos primeras letras del primer string y las últimas dos letras del segundo.
# Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".


def mezclador(string1, string2):
    if len(string1) > 2 and len(string2) > 2:
        sub_string1 = string1[0:2]
        sub_string2 = string2[len(string2) - 2: len(string2)]
        new_string = sub_string1 + sub_string2
        return new_string


# Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, pero
# con el segundo string intercalado entre cada letra del primero.
# Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"

def intercalar(string1, string2):
    indice = 0
    new_string = ""
    while indice < len(string1):
        new_string = new_string + string1[indice] + string2
        indice += 1
    return new_string


# Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos
# menos la cantidad de ocurrencias de ceros.
# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)

def ocurrencias(string):
    unos = 0
    ceros = 0
    # Recorremos to do el string
    for i in string:
        if i == "1":
            unos += 1
        else:
            ceros += 1

    return unos - ceros


# Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el
# elemento en el índice n.
# Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".
# Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.

def remover_enesimo(string, number):

    if number >= len(string) or number < 0:
        return "Indice no encontrado"
    elif number == len(string) - 1:
        sub_string1 = string[:number]
        return sub_string1
    elif number == 0:
        sub_string2 = string[number + 1:]
        return sub_string2
    else:
        sub_string1 = string[:number]
        sub_string2 = string[number + 1:]
        return sub_string1 + sub_string2


# Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en
# mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.
# Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".

def reemplazo(cadena):
    for i in cadena:
        if i in string.ascii_uppercase:
            cadena = cadena.replace(i, "$")

    return cadena


# ---------------------------------------------------------------------------------------------------------------------#



