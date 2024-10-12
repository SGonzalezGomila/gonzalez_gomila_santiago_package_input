from validate import *

def get_int() -> int | None:
    numero = int(input("Ingrese un número entero: "))
    resultado = validate_number(
        numero,
        "Ingrese un número entero dentro del rango",
        "Error: número fuera de rango, intente de nuevo",
        10, 1, 3
    )
    return resultado



def get_float()->float|None:
    numero = float(input("ingrese un numero con decimal"))
    resultado = validate_number(
        numero,
        "Ingrese un número entero dentro del rango",
        "Error: número fuera de rango, intente de nuevo",
        10, 1, 3
    )
    return resultado


def get_string()->str|None:
    cadena = input("ingrese una cadena de texto")
    resultado = validate_string(
        cadena,
        10,1,
        "error la cadena de caracteres es demasiado corta",
        "error la cadena de caracteres es demasiado larga",
        "demasiados reintentos",
        3
    )
    return resultado

cadena = get_string()
print(cadena)