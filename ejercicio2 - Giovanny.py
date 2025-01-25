# Ejercicio 2: Buscar el número más grande y más pequeño en un arreglo bidimensional
# Descripción: Escribe una función que reciba una matriz y retorne el número más grande y el más pequeño.
# Debe tener la función para crear la matriz e imprimirlo.
# No se pueden usar funciones propias de listas

try: 
    def crear_matriz(filas, columnas):
        # crea una matriz vacia
        matriz = [[0] * columnas for _ in range(filas)]  # cre una matriz de ceros
        
        for i in range(filas):
            for j in range(columnas):
                valor = int(input(f"Ingresa el valor para la posición ({i+1}, {j+1}): "))
                matriz[i][j] = valor  # Asignamos el valor en la posición correspondiente
        return matriz

    # funcion para encontrar el numero mas grande y el más pequeño de la matriz
    def encontrar_extremos(matriz):
        # inicializamos los extremos con el primer valor de la matriz
        max_num = matriz[0][0]
        min_num = matriz[0][0]
        
        # Recorre la matriz para encontrar el mayor y menor
        for fila in matriz:
            for valor in fila:
                if valor > max_num:
                    max_num = valor
                if valor < min_num:
                    min_num = valor
                    
        return max_num, min_num

    # Función para imprimir
    def imprimir_matriz(matriz):
        for fila in matriz:
            print(fila)

    # funcion principal 
    def main():
        filas = int(input("Ingresa el número de filas de la matriz: "))
        columnas = int(input("Ingresa el número de columnas de la matriz: "))
        
        matriz = crear_matriz(filas, columnas)  # Crea la matriz
        imprimir_matriz(matriz)  # Imprime la matriz
        
        # Encontra el numero del mas grande al mas pequeño
        max_num, min_num = encontrar_extremos(matriz)
        
        print(f"El número más grande es: {max_num}")
        print(f"El número más pequeño es: {min_num}")

    # llama a la funcion principal
    main()
except ValueError:
    print("no es un valor numerico")
except Exception as e:
    print(f"ha ocurrido un error al convertir {e}")
finally:
    print("proceso finalizado")