def validate_number(numero: int|float, mensaje: str, mensaje_error: str, maximo: int, minimo: int, reintentos: int) -> int | None:
    """Valida que el número ingresado esté dentro del rango especificado.

    Args:
        numero (int): Número a validar.
        mensaje (str): Mensaje que se muestra para pedir un número.
        mensaje_error (str): Mensaje que se muestra al finalizar todos los reintentos.
        maximo (int): Valor máximo aceptado.
        minimo (int): Valor mínimo aceptado.
        reintentos (int): Número de intentos permitidos.

    Returns:
        int | None: El número validado o None si no se validó.
    """
    resultado = None
    contador_reintentos = 0
    
    while numero < minimo or numero > maximo:
        print(mensaje_error)
        contador_reintentos += 1
        if numero == "":
            resultado =  None

        if contador_reintentos == reintentos:
            resultado = None
            break
        
        numero = int|float(input(mensaje))
    
    if minimo <= numero and numero <= maximo:
        resultado = numero
    
    return resultado


def validate_string(cadena:str,longitud_maxima:int, longitud_minima:int,mensaje_error_minimo:str,mensaje_error_maximo:str,mensaje_error:str,reintentos:int)->str|None:
    """Valida una cadena de caracteres en un rango de caracteres especifico

    Args:
        cadena (str): Es la cadena de caracteres a ingresar
        longitud_maxima (int): es la longitud maxima de la cadena de caracteres
        longitud_minima (int): es la longitud minima de la cadena de caracteres
        mensaje_error_minimo (str): mensaje de error para cuando la cadena de caracteres no supera el minimo de caracteres posible
        mensaje_error_maximo (str): mensaje de error para cuando la cadena de caracteres no supera el maximo de caracteres posible
        mensaje_error (str): mensaje de error para cuando se supera los reintentos
        reintentos (int): cantidad maxima de reintentos

    Returns:
        str|None: retorna cadena de caracteres o NONE
    """
   
   
    resultado = None
    cadena 
    contador_reintentos = 0

    while len(cadena) < longitud_minima or len(cadena) > longitud_maxima:
        cadena
        if contador_reintentos == reintentos:
            print(mensaje_error)
            resultado = None
            break

        if len(cadena) > longitud_maxima:
            print(mensaje_error_maximo)
            cadena 
            contador_reintentos +=1
            resultado

        elif len(cadena) < longitud_minima:
            print(mensaje_error_minimo)
            cadena 
            contador_reintentos+=1
            resultado
            
        else:
            print(cadena)
            resultado == cadena
    
    return resultado