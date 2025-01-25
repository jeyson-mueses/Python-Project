# Ejercicio 3: Promedio de un arreglo
# Descripción: Crea una función que reciba un arreglo de números enteros y retorne el promedio de los elementos.
# Debe tener la función para crear la matriz e imprimirlo.
# No se pueden usar funciones propias de listas


def crear_arreglo():
    entrada = input("Ingrese números separados por espacios: ")
    arreglo = []
    num_actual = ''
    
    for caracter in entrada:
        if caracter == ' ':
            if num_actual:
                try:
                    arreglo += [int(num_actual)]  # Intenta convertir a número
                except:
                    print("Error: Solo se permiten números")
                    return None
                num_actual = ''
        else:
            num_actual += caracter
    
    # Agregar último número
    if num_actual:
        try:
            arreglo += [int(num_actual)]
        except:
            print("Error: Solo se permiten números")
            return None
    
    if not arreglo:
        print("Error: No se ingresaron números")
        return None
    
    print("Arreglo:", arreglo)
    return arreglo

def promedio(arreglo):
    suma = 0
    count = 0
    
    # Recorrer con while simple
    i = 0
    while i < len(arreglo):
        suma += arreglo[i]
        count += 1
        i += 1
    
    if count == 0:
        return 0
    return suma / count

# Programa principal
arreglo = crear_arreglo()
if arreglo:
    prom = promedio(arreglo)
    print("Promedio:", prom)
else:
    print("No se pudo calcular el promedio")