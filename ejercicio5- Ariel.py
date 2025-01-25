try:
    def crear_arreglo():
        dimension = int(input("ingrese la dimension del arreglo: "))
        arreglo = [0]*dimension
        for i in range (len(arreglo)):
            valor= int(input(f"ingrese valor{i+1}: "))
            arreglo[i]=valor
        return arreglo

    def invertir_arreglo(arreglo):
        arregloInvertido = [0]*len(arreglo)
        for i in range (len(arreglo)):
            arregloInvertido[i] = arreglo[len(arreglo)-1-i]
        return arregloInvertido


    arreglo = crear_arreglo()
    print(arreglo)
    print(invertir_arreglo(arreglo))


except ValueError:
    print("no se pudo convertir a numero")
except Exception as e:
    print("ah oxurrido un error en {e}")
finally:
    print("proceso finalizado")
