# Ejercicio 6: Encontrar números pares en un arreglo
# Descripción: Escribe las siguientes funciones
#  - función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números pares.
#  - función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números impares.
# Debe tener la función para crear el arreglo e imprimirlo.
# No se pueden usar funciones propias de listas
def crear_arreglo():
    entrada = input("Ingrese números separados por espacios: ")
    arreglo = []
    num_actual = ""
    
    # Procesamiento manual sin funciones de listas
    for caracter in entrada:
        if caracter == " ":
            if num_actual:
                try:
                    arreglo += [int(num_actual)]  # Concatenación en lugar de append()
                except:
                    print("Error: Solo se permiten números enteros")
                    return None
                num_actual = ""
        else:
            num_actual += caracter
    
    # Último número
    if num_actual:
        try:
            arreglo += [int(num_actual)]
        except:
            print("Error: Solo se permiten números enteros")
            return None
    
    if not arreglo:
        print("Error: No se ingresaron números")
        return None
    
    print("\nArreglo original:", arreglo)
    return arreglo

def numeros_pares(arreglo):
    pares = []
    i = 0
    # Recorrido con índice manual
    while i < len(arreglo):
        if arreglo[i] % 2 == 0:
            pares += [arreglo[i]]  # Concatenación para añadir elementos
        i += 1
    return pares

def numeros_impares(arreglo):
    impares = []
    i = 0
    while i < len(arreglo):
        if arreglo[i] % 2 != 0:
            impares += [arreglo[i]]
        i += 1
    return impares

# Programa principal
if __name__ == "__main__":
    mi_arreglo = crear_arreglo()
    if mi_arreglo:
        print("Números pares:", numeros_pares(mi_arreglo))
        print("Números impares:", numeros_impares(mi_arreglo))