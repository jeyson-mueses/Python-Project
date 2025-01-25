# Contar ocurrencias de un número en un arreglo
# Descripción: Crea una función que reciba un arreglo y un número, y retorne cuántas veces aparece ese número en el arreglo.
# Debe tener la función para crear el arreglo e imprimirlo.
# No se pueden usar funciones propias de listas
# Función para crear el arreglo


# Función para crear el arreglo
try:
    def crear_arreglo():
        n = int(input("Ingresa el número de elementos en el arreglo: "))
        arreglo = [0] * n  # area un arreglo del tamaño que el usuario elija
        for i in range(n):
            valor = int(input(f"Ingresa el valor para el elemento {i + 1}: "))
            arreglo[i] = valor  # asigna el valor en el indice correspondiente
        return arreglo

    # funcion para contar las ocurrencias del numero del arreglo que el usuario elija
    def contar_ocurrencias(arreglo, numero):
        contador = 0
        for i in range(len(arreglo)):
            if arreglo[i] == numero:
                contador += 1
        return contador

    # funcion para imprimir el arreglo que el usuario escogio
    def imprimir_arreglo(arreglo):
        print("Arreglo:", arreglo)

    # funcion principal 
    def main():
        arreglo = crear_arreglo()
        imprimir_arreglo(arreglo)
        numero = int(input("Ingresa el número que deseas contar: "))
        ocurrencias = contar_ocurrencias(arreglo, numero)
        print(f"El número {numero} aparece {ocurrencias} vez/veces en el arreglo.")

    # llama a la funcion principal
    main()
except ValueError:
    print("no es un valor numerico")
except Exception as e:
    print(f"ha ocurrido un error al convertir {e}")
finally:
    print("proceso finalizado")