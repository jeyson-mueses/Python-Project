try:
    def crear_arreglo():
        dimension= int(input("ingresa la dimension de tu arreglo porfa: "))

        arreglo=[0]*dimension
        for i in range (dimension):
            valor= int(input(f"ingrese el numero {i+1}: "))
            arreglo[i] = valor
        
        return arreglo

    def suma_valores_arreglo(arreglo):
        suma =0
        for i in range (len(arreglo)):
            suma += arreglo[i]
        return suma
        
    def imprimir(arreglo):
        print("arreglo:", arreglo)

    arreglo = crear_arreglo()
    suma= suma_valores_arreglo(arreglo)
    print(imprimir(arreglo))
    print("la suma del arreglo es:", suma)
except ValueError:
    print("no se pudo convertir a numero")
except Exception as e:
    print("ah oxurrido un error en {e}")
finally:
    print("proceso finalizado")

###
