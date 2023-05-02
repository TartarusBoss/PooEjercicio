class ProductFinder:
    def largest_product(self, nums):
        #Acá se comprueba si la lista tiene más de 3 elementos, si no, forzamos un error
        if len(numeros) < 3:
            raise ValueError("La lista debe contener minimo 3 elementos")
        try:
            #Acá se ordena la lista de numeros descendentemente
            numeros_ordenados = sorted(numeros, reverse=True)
            #Acá se multiplican los 3 números mayores
            producto_maximo = numeros_ordenados[0] * numeros_ordenados[1] * numeros_ordenados[2]
            #Acá recorremos la lista de numeros ordenados desde el 3 elemento
            for i in range(2, len(numeros_ordenados)):
                #Acá calculamos el producto de los 3 numeros seguidos
                producto = numeros_ordenados[i] * numeros_ordenados[i-1] * numeros_ordenados[i-2]
                #Acá se comparan ambos productos para ver cual es mayor
                if producto > producto_maximo:
                    #Acá actualizamos con el valor del producto mayor
                    producto_maximo = producto
            #Se retorna el producto maximo
            return producto_maximo
        #Si se coloca un valor distinto a un entero, forzamos el error
        except TypeError:
            raise ValueError("La lista debe contener solo numeros enteros")

# Test
#Lista de los numeros
numeros = [5, 3, 2, 1, 6, -1]
#Asigno una instancia a la variable test
test = ProductFinder()
#Se llama al metodo largest product y el argumento es la lista de numeros
result = test.largest_product(numeros)
#Color verde
color_verde = "\033[32m"
#Resultado
print("\033[32m" + f"El producto máximo de la lista {numeros} es: {result}")

